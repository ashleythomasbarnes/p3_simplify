import argparse
import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from astropy.io import fits
from astropy.table import Table
from astroquery.eso import Eso
from bs4 import BeautifulSoup

ALLOWED_INPUT_MAPPING = {
    "IMAGE": "IMAGE (single) MEF format",
    "IMAGE.ASSOCIATED": "IMAGE (single) associated file format",
    "MEFIMAGE": "MEFIMAGE (mosaic) MEF format",
}

# User-facing descriptions that differ from the current CSV column names.
TABLE_COLUMN_ALIASES = {
    "IMAGE (single) associated file format": "IMAGE (single)",
}

# Add one ESO header URL here for each product type that has an example.
EXAMPLE_HEADER_URLS = {
    "SPECTRUM":                 "https://archive.eso.org/hdr?DpId=ADP.2026-07-13T03:27:49.375",
    "IMAGE":                    "https://archive.eso.org/hdr?DpId=ADP.2026-07-16T08:33:58.442",
    "IMAGE.ASSOCIATED":         "https://archive.eso.org/hdr?DpId=ADP.2016-07-29T07:24:33.571",
    "IMAGE.FLUXMAP":            "https://archive.eso.org/hdr?DpId=ADP.2024-07-12T08:07:39.447",
    "MEFIMAGE":                 "https://archive.eso.org/hdr?DpId=ADP.2025-12-09T09:08:02.822",
    "CUBE.IFS":                 "https://archive.eso.org/hdr?DpId=ADP.2026-01-19T14:23:01.707",
    "VISIBILITY":               "https://archive.eso.org/hdr?DpId=ADP.2026-06-24T10:22:30.103",
    "SRCTBL":                   "https://archive.eso.org/hdr?DpId=ADP.2026-05-18T11:41:29.594",
    "MCATALOG":                 "https://archive.eso.org/hdr?DpId=ADP.2025-07-30T14:32:33.277",
    "CATALOGTILE":              "https://archive.eso.org/hdr?DpId=ADP.2025-07-30T14:32:28.959",
    "CATALOG":                  "https://archive.eso.org/hdr?DpId=ADP.2025-05-14T09:12:30.235",

}
ANSI_BOLD_GREEN = "\033[1;32m"
ANSI_RESET = "\033[0m"

TABLE_DIR = Path(__file__).resolve().parent / "data" / "p3sdpstd_v8_tables"

table_primary = Table.read(TABLE_DIR / "table_primary.csv")
table_extension = Table.read(TABLE_DIR / "table_extension.csv")
table_footnotes = Table.read(TABLE_DIR / "table_footnotes.csv")
table_legend = Table.read(TABLE_DIR / "table_legend.csv")

# These CSV files currently contain a UTF-8 byte-order mark before "key".
table_footnotes.rename_column(table_footnotes.colnames[0], "key")
table_legend.rename_column(table_legend.colnames[0], "key")


# Codes present in the keyword tables but not currently defined in
# table_legend.csv.
LEGACY_LEGEND = {
    "M": "Keyword mandatory.",
    "RC": "Keyword recommended.",
    "SU": "Contact Phase 3 support to determine whether the keyword is required.",
}


def _input_product_mapping(primary_table, extension_table):
    """Map accepted user inputs to descriptions and keyword-table columns."""
    extension_types = set(extension_table.colnames[2:])
    table_types = [
        product_type
        for product_type in primary_table.colnames[2:]
        if product_type in extension_types
    ]

    mapping = {}
    mapped_table_types = set()
    for input_name, description in ALLOWED_INPUT_MAPPING.items():
        table_type = TABLE_COLUMN_ALIASES.get(description, description)
        if table_type in table_types:
            mapping[input_name] = {
                "description": description,
                "table_type": table_type,
            }
            mapped_table_types.add(table_type)

    for table_type in table_types:
        if table_type not in mapped_table_types:
            mapping[table_type] = {
                "description": table_type,
                "table_type": table_type,
            }
    return mapping


def _available_product_types(primary_table, extension_table):
    """Return the accepted user-facing product-type names."""
    return list(_input_product_mapping(primary_table, extension_table))


def _validate_product_name(product_name, primary_table, extension_table):
    """Return the table column for a supported user-facing product name."""
    mapping = _input_product_mapping(primary_table, extension_table)
    if product_name not in mapping:
        choices = []
        for input_name, details in mapping.items():
            choice = f"  - {input_name}"
            if details["description"] != input_name:
                choice += f" [{details['description']}]"
            choices.append(choice)
        choices_text = "\n".join(choices)
        raise ValueError(
            f"Unknown ESO product type {product_name!r}.\n"
            f"Available product types are:\n{choices_text}"
        )
    return mapping[product_name]["table_type"]


def _get_legend_lookup(legend_table):
    legend = {
        str(key).strip(): str(meaning).strip()
        for key, meaning in zip(legend_table["key"], legend_table["meaning"])
    }
    return {**LEGACY_LEGEND, **legend}


def _describe_requirement(requirement, legend_lookup):
    """Expand a code such as ``MA65`` into a meaning and footnote number."""
    descriptions = []
    for code in requirement.split():
        match = re.fullmatch(r"([A-Z]+)(\d*)", code)
        if match is None:
            descriptions.append({"code": code, "meaning": "Unknown requirement code"})
            continue

        legend_key, number = match.groups()
        description = {
            "code": code,
            "legend_key": legend_key,
            "meaning": legend_lookup.get(
                legend_key, f"Unknown requirement code {legend_key!r}"
            ),
        }
        if number:
            description["footnote"] = int(number)
        descriptions.append(description)
    return descriptions


def _format_requirement_detail(detail):
    """Format a decoded requirement for the human-readable report."""
    meaning = detail["meaning"].rstrip(".")
    if "footnote" in detail:
        # The footnote marker printed below makes this clause redundant.
        meaning = meaning.split(", refer to the table footnotes", 1)[0]
        meaning += f" [footnote {detail['footnote']}]"
    return meaning


def _is_mandatory(entry):
    """Return whether an entry is mandatory or mandatory when applicable."""
    return any(
        detail.get("legend_key") in {"M", "MM", "ME", "MA"}
        for detail in entry["requirement_details"]
    )


def _style_keyword(keyword, mandatory, use_color):
    if mandatory and use_color:
        return f"{ANSI_BOLD_GREEN}{keyword}{ANSI_RESET}"
    return keyword


def _format_keyword_token(token):
    """Explain an indexed placeholder such as OBIDi with concrete examples."""
    if token.endswith("i"):
        stem = token[:-1]
        examples = ", ".join(f"{stem}{number}" for number in range(1, 4))
        return f"{token} (for example: {examples}, etc.)"
    return token


def _format_keyword_spec(specification):
    """Turn compact table notation into a non-expert-friendly description."""
    tokens = specification.split()
    if len(tokens) == 1:
        return _format_keyword_token(tokens[0])

    connector = " and " if specification == "RA DEC" else " or "
    return connector.join(_format_keyword_token(token) for token in tokens)


def _keyword_matches_spec(keyword, specification):
    """Match a FITS keyword against entries such as ``PROG_ID PROGIDi``."""
    for token in specification.split():
        pattern = re.escape(token).replace("i", r"\d+")
        if re.fullmatch(pattern, keyword):
            return True
    return False


def _parse_archive_header_page(header_text):
    """Parse every END-delimited FITS header from an ESO header page."""
    header_blocks = []
    current_lines = []

    for raw_line in header_text.splitlines():
        # The archive's HTML view can let comments run past the FITS
        # 80-character card boundary.  Astropy interprets that overflow as a
        # malformed long-string card, so restore the FITS boundary first.
        line = raw_line[:80].rstrip()
        if not line.strip():
            continue

        # These cards are intentionally excluded from the printed examples.
        if line.startswith("COMMENT") or line.startswith("HIERARCH"):
            continue

        current_lines.append(line)
        if line[:8].strip() != "END":
            continue

        header = fits.Header.fromstring("\n".join(current_lines), sep="\n")
        number = len(header_blocks)
        name = "PRIMARY" if number == 0 else header.get("EXTNAME", "EXTENSION")
        header_blocks.append(
            {
                "number": number,
                "name": name,
                "header": {
                    card.keyword: card.value
                    for card in header.cards
                    if card.keyword not in {"", "COMMENT"}
                },
            }
        )
        current_lines = []

    if current_lines:
        raise ValueError("ESO header response ended before an END card")
    if not header_blocks:
        raise ValueError("ESO header response did not contain a FITS header")
    return header_blocks


def _get_example_headers(product_name, eso=None):
    """Retrieve and parse all HDU headers without downloading the FITS data."""
    url = EXAMPLE_HEADER_URLS.get(product_name)
    if not url:
        return None

    product_ids = parse_qs(urlparse(url).query).get("DpId")
    if not product_ids:
        raise ValueError(f"Example header URL has no DpId parameter: {url}")

    eso = Eso() if eso is None else eso
    response = eso._request("GET", url, cache=False)
    response.raise_for_status()
    root = BeautifulSoup(response.content, "html5lib")
    header_block = root.select_one("pre")
    if header_block is None:
        raise RuntimeError(f"ESO returned no header for {product_ids[0]}")
    return _parse_archive_header_page(header_block.text)


def _print_example_headers(
    product_name,
    example_headers,
    primary_entries,
    extension_entries,
    use_color,
    source_url,
):
    if example_headers is None:
        return

    print("-" * 30)
    print(f"{product_name} - Example archive FITS headers")
    print(f"Source: {source_url}")
    print("-" * 30)
    for hdu in example_headers:
        entries = primary_entries if hdu["number"] == 0 else extension_entries
        mandatory_specs = [
            entry["keyword"] for entry in entries if _is_mandatory(entry)
        ]
        print(f"HDU {hdu['number']} - {hdu['name']}")
        for keyword, value in hdu["header"].items():
            mandatory = any(
                _keyword_matches_spec(keyword, specification)
                for specification in mandatory_specs
            )
            displayed_keyword = _style_keyword(keyword, mandatory, use_color)
            print(f"{displayed_keyword:<20} = {value!r}")
        print()


def _get_keyword_entries(product_name, table, legend_lookup):
    """Return the applicable keyword entries for one product column."""
    entries = []
    for name, requirement in zip(table["Column Name"], table[product_name]):
        requirement = str(requirement).strip()
        if requirement != "NA":
            entries.append(
                {
                    "keyword": str(name).strip(),
                    "requirement": requirement,
                    "requirement_details": _describe_requirement(
                        requirement, legend_lookup
                    ),
                }
            )
    return entries


def _get_footnotes(entries, footnote_table):
    """Return footnotes referenced by requirement codes such as MA65 or M33."""
    referenced_numbers = {
        int(number)
        for entry in entries
        for number in re.findall(r"\d+", entry["requirement"])
    }
    footnote_lookup = {
        int(key): str(text).strip()
        for key, text in zip(footnote_table["key"], footnote_table["footnote"])
    }

    return [
        {"number": number, "text": footnote_lookup[number]}
        for number in sorted(referenced_numbers)
        if number in footnote_lookup
    ]


def _print_mandatory_checklist(product_name, heading, entries, use_color):
    """Print a compact checklist containing only mandatory keyword entries."""
    print("-" * 30)
    print(f"{product_name} - {heading} mandatory keyword checklist")
    print("-" * 30)
    for entry in entries:
        keyword = _format_keyword_spec(entry["keyword"])
        print(_style_keyword(keyword, True, use_color))
    print()


def _print_report_header(product_name, product_description):
    """Print a clear introduction to the requested keyword report."""
    print()
    print("-" * 60)
    print("ESO Phase 3 header keyword guide")
    print(f"Requested data product type: {product_name}")
    if product_description != product_name:
        print(f"Product format: {product_description}")
    print("-" * 60)
    print()


def get_values(
    product_name,
    primary_table=table_primary,
    extension_table=table_extension,
    footnote_table=table_footnotes,
    legend_table=table_legend,
    *,
    print_summary=True,
    use_color=True,
):
    """Return keyword requirements and referenced footnotes for a product type.

    Entries whose table value is ``NA`` are omitted. Requirement codes are kept
    in the result so that mandatory, optional, recommended, and other entries
    remain distinguishable.
    """
    table_product_name = _validate_product_name(
        product_name, primary_table, extension_table
    )
    product_description = _input_product_mapping(
        primary_table, extension_table
    )[product_name]["description"]
    legend_lookup = _get_legend_lookup(legend_table)
    primary = _get_keyword_entries(table_product_name, primary_table, legend_lookup)
    extension = _get_keyword_entries(
        table_product_name, extension_table, legend_lookup
    )
    mandatory_primary = [entry for entry in primary if _is_mandatory(entry)]
    mandatory_extension = [entry for entry in extension if _is_mandatory(entry)]
    footnotes = _get_footnotes(primary + extension, footnote_table)
    example_headers = _get_example_headers(product_name)
    example_header_url = EXAMPLE_HEADER_URLS.get(product_name)

    result = {
        "product_name": product_name,
        "product_description": product_description,
        "table_product_name": table_product_name,
        "primary": primary,
        "extension": extension,
        "mandatory_primary": mandatory_primary,
        "mandatory_extension": mandatory_extension,
        "footnotes": footnotes,
        "legend": legend_lookup,
        "example_headers": example_headers,
        "example_header_url": example_header_url,
    }

    if print_summary:
        _print_report_header(product_name, product_description)
        print(
            "Checklist note: this includes keywords that are always mandatory, "
            "mandatory for ESO files, or mandatory when applicable."
        )
        print(
            'The placeholder "i" means a numbered series; include the numbered '
            "keywords needed for your data.\n"
        )
        _print_mandatory_checklist(
            product_name, "Primary HDU", mandatory_primary, use_color
        )
        _print_mandatory_checklist(
            product_name, "Extension HDU", mandatory_extension, use_color
        )

        for heading, entries in (
            ("Primary HDU", primary),
            ("Extension HDU", extension),
        ):
            print("-" * 30)
            print(f"{product_name} - {heading}")
            print("-" * 30)
            for entry in entries:
                descriptions = [
                    _format_requirement_detail(detail)
                    for detail in entry["requirement_details"]
                ]
                keyword = _style_keyword(
                    _format_keyword_spec(entry["keyword"]),
                    _is_mandatory(entry),
                    use_color,
                )
                print(f"{keyword}: {'; '.join(descriptions)}")
            print()

        print("-" * 30)
        print(f"{product_name} - Referenced footnotes")
        print("-" * 30)
        for footnote in footnotes:
            print(f"{footnote['number']}: {footnote['text']}")
        print()

        _print_example_headers(
            product_name,
            example_headers,
            primary,
            extension,
            use_color,
            example_header_url,
        )

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Show the header keyword requirements for an ESO product type."
    )
    parser.add_argument(
        "product_name",
        metavar="PRODUCT_TYPE",
        help="Product type to inspect, for example SPECTRUM or IMAGE.FLUXMAP.",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable bold and coloured terminal output.",
    )
    args = parser.parse_args()
    try:
        _validate_product_name(args.product_name, table_primary, table_extension)
    except ValueError as error:
        parser.error(str(error))
    get_values(args.product_name, use_color=not args.no_color)


if __name__ == "__main__":
    main()
