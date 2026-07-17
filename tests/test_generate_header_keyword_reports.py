#!/usr/bin/env python3
"""Tests for generate_header_keyword_reports.py."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

import generate_header_keyword_reports as reports


def requirement(code="M", meaning="Keyword mandatory.", footnote=None):
    detail = {"code": code, "legend_key": code.rstrip("0123456789"), "meaning": meaning}
    if footnote is not None:
        detail["footnote"] = footnote
    return {
        "keyword": "OBIDi" if footnote else "PROD|CATG",
        "requirement": code,
        "requirement_details": [detail],
    }


def sample_result(product_name="SPECTRUM", with_example=True):
    primary_entry = requirement()
    extension_entry = requirement(
        "MA65", "Keyword mandatory when applicable, refer to the table footnotes.", 65
    )
    return {
        "product_name": product_name,
        "product_description": f"{product_name} format",
        "primary": [primary_entry],
        "extension": [extension_entry],
        "mandatory_primary": [primary_entry],
        "mandatory_extension": [extension_entry],
        "footnotes": [{"number": 65, "text": "Use A | B."}],
        "legend": {},
        "example_header_url": "https://example.test/header",
        "example_headers": (
            [
                {"number": 0, "name": "PRIMARY", "header": {"PROD|CATG": "SCIENCE"}},
                {"number": 1, "name": "DATA", "header": {"OBID1": 123}},
            ]
            if with_example
            else None
        ),
    }


class MarkdownTests(unittest.TestCase):
    def test_render_markdown_formats_structured_result(self):
        markdown = reports.render_markdown(sample_result())

        self.assertIn("# SPECTRUM header keyword report", markdown)
        self.assertIn("**PROD\\|CATG**", markdown)
        self.assertIn("OBIDi (for example: OBID1, OBID2, OBID3, etc.)", markdown)
        self.assertIn("Use A \\| B.", markdown)
        self.assertIn("### HDU 0 — PRIMARY", markdown)
        self.assertIn("* PROD|CATG", markdown)
        self.assertIn("* OBID1", markdown)

    def test_render_markdown_handles_missing_sections(self):
        result = sample_result(with_example=False)
        result.update(
            primary=[],
            extension=[],
            mandatory_primary=[],
            mandatory_extension=[],
            footnotes=[],
        )

        markdown = reports.render_markdown(result)

        self.assertIn("No mandatory keywords are defined", markdown)
        self.assertIn("No applicable keyword requirements are defined", markdown)
        self.assertIn("No footnotes are referenced", markdown)
        self.assertIn("No archive example is available", markdown)


class GenerationTests(unittest.TestCase):
    def test_generates_selected_types_and_custom_output_directory(self):
        calls = []

        def fake_get_values(product_type, *, print_summary, use_color):
            calls.append((product_type, print_summary, use_color))
            print(f"plain report for {product_type}")
            return sample_result(product_type)

        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory) / "custom"
            successes, failures = reports.generate_reports(
                ["SPECTRUM", "IMAGE"], output_dir, value_getter=fake_get_values
            )

            self.assertEqual(successes, ["SPECTRUM", "IMAGE"])
            self.assertEqual(failures, {})
            self.assertEqual(
                calls,
                [("SPECTRUM", True, False), ("IMAGE", True, False)],
            )
            plain = (output_dir / "text" / "SPECTRUM.txt").read_text()
            self.assertEqual(plain, "plain report for SPECTRUM\n")
            self.assertNotIn("\033", plain)
            self.assertTrue((output_dir / "markdown" / "IMAGE.md").is_file())
            index = (output_dir / "markdown" / "index.md").read_text()
            self.assertIn("[SPECTRUM](SPECTRUM.md)", index)
            self.assertIn("../text/IMAGE.txt", index)

    def test_continues_after_failure_and_returns_failure(self):
        attempted = []

        def fake_get_values(product_type, *, print_summary, use_color):
            attempted.append(product_type)
            if product_type == "BROKEN":
                print("partial output")
                raise RuntimeError("archive unavailable | retry later")
            print("complete output")
            return sample_result(product_type)

        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            successes, failures = reports.generate_reports(
                ["BROKEN", "SPECTRUM"], output_dir, value_getter=fake_get_values
            )

            self.assertEqual(attempted, ["BROKEN", "SPECTRUM"])
            self.assertEqual(successes, ["SPECTRUM"])
            self.assertEqual(
                failures, {"BROKEN": "archive unavailable | retry later"}
            )
            self.assertFalse((output_dir / "text" / "BROKEN.txt").exists())
            self.assertFalse((output_dir / "markdown" / "BROKEN.md").exists())
            index = (output_dir / "markdown" / "index.md").read_text()
            self.assertIn("BROKEN", index)
            self.assertIn("archive unavailable \\| retry later", index)

    def test_main_uses_all_types_when_none_are_given(self):
        with mock.patch.object(
            reports, "available_product_types", return_value=["ONE", "TWO"]
        ), mock.patch.object(
            reports, "generate_reports", return_value=(["ONE", "TWO"], {})
        ) as generate:
            result = reports.main([])

        self.assertEqual(result, 0)
        self.assertEqual(generate.call_args.args[0], ["ONE", "TWO"])

    def test_main_preserves_selected_types(self):
        with mock.patch.object(
            reports, "available_product_types", return_value=["ONE", "TWO"]
        ), mock.patch.object(
            reports, "generate_reports", return_value=(["TWO"], {})
        ) as generate:
            result = reports.main(["TWO"])

        self.assertEqual(result, 0)
        self.assertEqual(generate.call_args.args[0], ["TWO"])

    def test_main_returns_nonzero_when_a_report_fails(self):
        with mock.patch.object(
            reports, "available_product_types", return_value=["ONE", "TWO"]
        ), mock.patch.object(
            reports,
            "generate_reports",
            return_value=(["ONE"], {"TWO": "archive unavailable"}),
        ):
            result = reports.main([])

        self.assertEqual(result, 1)

    def test_invalid_product_type_is_a_cli_error(self):
        parser = reports.build_parser(["ONE", "TWO"])
        with self.assertRaises(SystemExit) as raised:
            parser.parse_args(["THREE"])
        self.assertEqual(raised.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
