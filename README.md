# ESO Phase 3 header keyword guide

`get_header_keywords.py` is a command-line helper for finding the FITS header
keywords required for an ESO Phase 3 data product. It combines the primary-HDU
and extension-HDU requirement tables with the ESO legend and footnotes, then
shows a live example header from the ESO Science Archive.

The report includes:

- mandatory keyword checklists for the primary and extension HDUs;
- all applicable requirements, with ESO requirement codes translated into
  plain language;
- referenced footnotes;
- a live archive example for every supported product type.

Mandatory keywords are bold green by default. Indexed placeholders such as
`OBIDi` represent a numbered series (`OBID1`, `OBID2`, and so on).

## Requirements

- Python 3
- `astropy`
- `astroquery`
- `beautifulsoup4`
- `html5lib`
- internet access to `archive.eso.org`

Install the Python dependencies with:

```bash
python -m pip install astropy astroquery beautifulsoup4 html5lib
```

The script reads the ESO Phase 3 standard keyword tables from
`data/p3sdpstd_v8_tables`:

```text
table_primary.csv
table_extension.csv
table_footnotes.csv
table_legend.csv
```

## Usage

Run the script with an ESO product type:

```bash
python get_header_keywords.py IMAGE.FLUXMAP
```

For plain output without ANSI colour codes:

```bash
python get_header_keywords.py IMAGE.FLUXMAP --no-color
```

Show command-line help with:

```bash
python get_header_keywords.py --help
```

Supported product types are:

```text
IMAGE
IMAGE.ASSOCIATED
MEFIMAGE
IMAGE.FLUXMAP
SPECTRUM
CUBE.IFS
VISIBILITY
SRCTBL
MCATALOG
CATALOGTILE
CATALOG
```

Product names are case-sensitive.

## How the archive example works

For each supported product type, the script stores the URL of one example ESO
archive product. At runtime it requests the archive's header page and parses
all HDUs from the returned FITS header text. It does not download the FITS data
file. `COMMENT` and `HIERARCH` cards are omitted from the displayed example.

Because this is a live request, the command can fail if the ESO archive is
unavailable or the machine has no network connection.

## Use from Python

The same information is available as a dictionary:

```python
from get_header_keywords import get_values

result = get_values("SPECTRUM", print_summary=False, use_color=False)

print(result["mandatory_primary"])
print(result["mandatory_extension"])
print(result["footnotes"])
```

Calling `get_values()` still performs the live archive-header request when
`print_summary=False`; that option only suppresses terminal output.

## Local check

From the repository root, check that the script and bundled tables load with:

```bash
python -c "import get_header_keywords"
```

## Smoke test

Run the end-to-end smoke test for every supported product type with:

```bash
python tests/smoke_test_get_header_keywords.py
```

The smoke test makes live ESO archive requests and may take several seconds.

## Generate report files

Use the report wrapper to save both plain-text and Markdown versions for every
supported product type:

```bash
python generate_header_keyword_reports.py
```

To generate only selected product types, list them after the command:

```bash
python generate_header_keyword_reports.py SPECTRUM IMAGE
```

The default output layout is:

```text
generated/header_keyword_reports/
├── text/
│   ├── IMAGE.txt
│   └── SPECTRUM.txt
└── markdown/
    ├── index.md
    ├── IMAGE.md
    └── SPECTRUM.md
```

The Markdown index links to both formats. Choose another destination with:

```bash
python generate_header_keyword_reports.py --output-dir /path/to/reports
```

Report generation uses the same live ESO archive requests as the original
command. If one product type fails, the wrapper continues with the remaining
types, records the failure in `markdown/index.md`, and exits with a nonzero
status after all requested types have been attempted. It does not write a
partial report for the failed type.
