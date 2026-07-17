#!/usr/bin/env python3
"""Run get_header_keywords.py once for every accepted product type.

This is an end-to-end smoke test: it invokes the command-line script in a
separate process for each product type, including its ESO archive header
request when an example URL is configured.
"""

from __future__ import annotations

import argparse
import importlib.util
import subprocess
import sys
import time
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT_DIR / "get_header_keywords.py"


def load_header_keywords_module():
    """Load the script so its dynamically generated allowed inputs can be used."""
    spec = importlib.util.spec_from_file_location("get_header_keywords", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {SCRIPT_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def failure_detail(completed: subprocess.CompletedProcess[str]) -> str:
    """Return a compact diagnostic from a failed command."""
    output = completed.stderr.strip() or completed.stdout.strip()
    if not output:
        return "    (command produced no output)"
    return "\n".join(f"    {line}" for line in output.splitlines()[-12:])


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Smoke-test get_header_keywords.py for every allowed input."
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=60.0,
        help="Maximum seconds allowed for each product type (default: 60).",
    )
    args = parser.parse_args()

    module = load_header_keywords_module()
    product_types = module._available_product_types(
        module.table_primary, module.table_extension
    )

    failures: list[str] = []
    print(f"Testing {len(product_types)} allowed product types\n", flush=True)

    for product_type in product_types:
        started = time.monotonic()
        command = [sys.executable, str(SCRIPT_PATH), product_type, "--no-color"]
        try:
            completed = subprocess.run(
                command,
                cwd=ROOT_DIR,
                text=True,
                capture_output=True,
                timeout=args.timeout,
                check=False,
            )
        except subprocess.TimeoutExpired:
            elapsed = time.monotonic() - started
            failures.append(product_type)
            print(
                f"FAIL  {product_type:<20} timed out after {elapsed:.1f}s",
                flush=True,
            )
            continue

        elapsed = time.monotonic() - started
        if completed.returncode == 0:
            print(f"PASS  {product_type:<20} {elapsed:.1f}s", flush=True)
        else:
            failures.append(product_type)
            print(
                f"FAIL  {product_type:<20} exit code {completed.returncode} "
                f"({elapsed:.1f}s)",
                flush=True,
            )
            print(failure_detail(completed), flush=True)

    print()
    if failures:
        print(f"FAILED: {len(failures)}/{len(product_types)}")
        print("Broken inputs: " + ", ".join(failures))
        return 1

    print(f"ALL PASSED: {len(product_types)}/{len(product_types)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
