
import argparse
import sys
from pathlib import Path

from pydantic import ValidationError

from extractor import extract_invoice


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract invoice details from a text file "
                    "and save validated JSON."
    )

    parser.add_argument(
        "input_file",
        help="Path to the invoice text file"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="output.json",
        help="Output JSON file (default: output.json)"
    )

    args = parser.parse_args()

    input_path = Path(args.input_file)
    output_path = Path(args.output)

    # 1. Read the unstructured invoice text.
    try:
        document_text = input_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Error reading input file: {exc}", file=sys.stderr)
        return 1

    if not document_text.strip():
        print("Error: The input file is empty.", file=sys.stderr)
        return 1

    try:
        # 2. Send the text to Gemini and validate the response.
        invoice = extract_invoice(document_text)
    except ValidationError as exc:
        print("Error: Gemini returned data that failed validation.")
        print(exc)
        return 1
    except ValueError as exc:
        print(f"Error processing invoice: {exc}")
        return 1
    except Exception as exc:
        print(f"Extraction failed: {exc}", file=sys.stderr)
        return 1

    # 3. Save the validated model as JSON.
    try:
        output_path.write_text(
            invoice.model_dump_json(indent=2),
            encoding="utf-8"
        )
    except OSError as exc:
        print(f"Error writing output file: {exc}", file=sys.stderr)
        return 1

    print(f"Invoice extraction successful.")
    print(f"Validated JSON saved to: {output_path}")

    # 4. Display the result in the terminal.
    print("\nExtracted invoice details:")
    print(invoice.model_dump_json(indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

