#!/usr/bin/env python3
"""Generate plain-text and Markdown ESO header keyword reports."""

from __future__ import annotations

import argparse
import io
from contextlib import redirect_stdout
from pathlib import Path
from typing import Callable, Iterable

import get_header_keywords as header_keywords


DEFAULT_OUTPUT_DIR = (
    Path(__file__).resolve().parent / "generated" / "header_keyword_reports"
)


def available_product_types() -> list[str]:
    """Return product types supported by both bundled keyword tables."""
    return header_keywords._available_product_types(
        header_keywords.table_primary, header_keywords.table_extension
    )


def _markdown_text(value: object) -> str:
    """Escape text for use outside Markdown code blocks."""
    return (
        str(value)
        .replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("`", "\\`")
        .replace("\r\n", "<br>")
        .replace("\n", "<br>")
        .replace("\r", "<br>")
    )


def _requirement_meanings(entry: dict) -> str:
    return "; ".join(
        header_keywords._format_requirement_detail(detail)
        for detail in entry["requirement_details"]
    )


def _render_checklist(lines: list[str], entries: list[dict]) -> None:
    if not entries:
        lines.append("No mandatory keywords are defined for this HDU.")
        lines.append("")
        return

    for entry in entries:
        keyword = header_keywords._format_keyword_spec(entry["keyword"])
        lines.append(f"- [ ] **{_markdown_text(keyword)}**")
    lines.append("")


def _render_requirements_table(lines: list[str], entries: list[dict]) -> None:
    if not entries:
        lines.append("No applicable keyword requirements are defined for this HDU.")
        lines.append("")
        return

    lines.extend(
        [
            "| Keyword | Requirement | Meaning |",
            "| --- | --- | --- |",
        ]
    )
    for entry in entries:
        keyword = header_keywords._format_keyword_spec(entry["keyword"])
        if header_keywords._is_mandatory(entry):
            keyword = f"**{_markdown_text(keyword)}**"
        else:
            keyword = _markdown_text(keyword)
        lines.append(
            f"| {keyword} | `{_markdown_text(entry['requirement'])}` | "
            f"{_markdown_text(_requirement_meanings(entry))} |"
        )
    lines.append("")


def _render_example_headers(lines: list[str], result: dict) -> None:
    example_headers = result.get("example_headers")
    if not example_headers:
        lines.append("No archive example is available for this product type.")
        lines.append("")
        return

    lines.append(
        "Lines prefixed with `*` are mandatory, mandatory for ESO files, "
        "or mandatory when applicable."
    )
    lines.append("")
    for hdu in example_headers:
        lines.append(
            f"### HDU {hdu['number']} — {_markdown_text(hdu['name'])}"
        )
        lines.append("")
        entries = result["primary"] if hdu["number"] == 0 else result["extension"]
        mandatory_specs = [
            entry["keyword"]
            for entry in entries
            if header_keywords._is_mandatory(entry)
        ]
        lines.append("```text")
        for keyword, value in hdu["header"].items():
            mandatory = any(
                header_keywords._keyword_matches_spec(keyword, specification)
                for specification in mandatory_specs
            )
            marker = "*" if mandatory else " "
            lines.append(f"{marker} {keyword:<20} = {value!r}")
        lines.extend(["```", ""])


def render_markdown(result: dict) -> str:
    """Render one ``get_values`` result as a standalone Markdown report."""
    product_name = _markdown_text(result["product_name"])
    description = _markdown_text(result["product_description"])
    lines = [f"# {product_name} header keyword report", ""]

    if result["product_description"] != result["product_name"]:
        lines.extend([f"**Product format:** {description}", ""])

    source_url = result.get("example_header_url")
    if source_url:
        lines.extend([f"**Archive example:** [ESO header page]({source_url})", ""])

    lines.extend(
        [
            "Mandatory checklists include keywords that are always mandatory, "
            "mandatory for ESO files, or mandatory when applicable. The placeholder "
            "`i` denotes a numbered series.",
            "",
            "## Mandatory keyword checklists",
            "",
            "### Primary HDU",
            "",
        ]
    )
    _render_checklist(lines, result["mandatory_primary"])
    lines.extend(["### Extension HDU", ""])
    _render_checklist(lines, result["mandatory_extension"])

    lines.extend(["## All keyword requirements", "", "### Primary HDU", ""])
    _render_requirements_table(lines, result["primary"])
    lines.extend(["### Extension HDU", ""])
    _render_requirements_table(lines, result["extension"])

    lines.extend(["## Referenced footnotes", ""])
    if result["footnotes"]:
        for footnote in result["footnotes"]:
            lines.append(
                f"{footnote['number']}. {_markdown_text(footnote['text'])}"
            )
        lines.append("")
    else:
        lines.extend(["No footnotes are referenced by this product type.", ""])

    lines.extend(["## Example archive FITS headers", ""])
    _render_example_headers(lines, result)
    return "\n".join(lines).rstrip() + "\n"


def render_index(successes: Iterable[str], failures: dict[str, str]) -> str:
    """Render the index for one generation run."""
    successful_types = list(successes)
    lines = [
        "# ESO Phase 3 header keyword reports",
        "",
        "## Generated reports",
        "",
    ]
    if successful_types:
        lines.extend(
            [
                "| Product type | Markdown | Plain text |",
                "| --- | --- | --- |",
            ]
        )
        for product_type in successful_types:
            name = _markdown_text(product_type)
            lines.append(
                f"| {name} | [{name}]({product_type}.md) | "
                f"[plain text](../text/{product_type}.txt) |"
            )
        lines.append("")
    else:
        lines.extend(["No reports were generated successfully.", ""])

    lines.extend(["## Failures", ""])
    if failures:
        lines.extend(["| Product type | Error |", "| --- | --- |"])
        for product_type, error in failures.items():
            lines.append(
                f"| {_markdown_text(product_type)} | {_markdown_text(error)} |"
            )
        lines.append("")
    else:
        lines.extend(["All requested reports were generated successfully.", ""])
    return "\n".join(lines).rstrip() + "\n"


def generate_reports(
    product_types: Iterable[str],
    output_dir: Path,
    *,
    value_getter: Callable = header_keywords.get_values,
) -> tuple[list[str], dict[str, str]]:
    """Generate reports and return successful types and failure messages."""
    output_dir = Path(output_dir)
    text_dir = output_dir / "text"
    markdown_dir = output_dir / "markdown"
    text_dir.mkdir(parents=True, exist_ok=True)
    markdown_dir.mkdir(parents=True, exist_ok=True)

    successes: list[str] = []
    failures: dict[str, str] = {}
    for product_type in product_types:
        print(f"Generating {product_type} ...", flush=True)
        captured = io.StringIO()
        try:
            with redirect_stdout(captured):
                result = value_getter(
                    product_type, print_summary=True, use_color=False
                )
            plain_text = captured.getvalue()
            markdown = render_markdown(result)
            (text_dir / f"{product_type}.txt").write_text(
                plain_text, encoding="utf-8"
            )
            (markdown_dir / f"{product_type}.md").write_text(
                markdown, encoding="utf-8"
            )
        except Exception as error:  # Continue so every requested type is attempted.
            failures[product_type] = str(error) or type(error).__name__
            print(f"FAILED {product_type}: {failures[product_type]}", flush=True)
        else:
            successes.append(product_type)
            print(f"Generated {product_type}", flush=True)

    (markdown_dir / "index.md").write_text(
        render_index(successes, failures), encoding="utf-8"
    )
    return successes, failures


def build_parser(product_types: list[str]) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Generate plain-text and Markdown header keyword reports. "
            "All supported product types are generated when none are specified."
        )
    )
    parser.add_argument(
        "product_types",
        metavar="PRODUCT_TYPE",
        nargs="*",
        choices=product_types,
        help="Product types to generate (default: all supported types).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Report directory (default: {DEFAULT_OUTPUT_DIR}).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    supported = available_product_types()
    args = build_parser(supported).parse_args(argv)
    selected = args.product_types or supported
    successes, failures = generate_reports(selected, args.output_dir)

    print()
    print(f"Generated {len(successes)}/{len(selected)} requested report(s).")
    print(f"Output directory: {args.output_dir.resolve()}")
    if failures:
        print("Failed product types: " + ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
