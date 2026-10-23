# Structured LLM Prompt Pipeline and JSON Extractor

## Overview

This project implements an executable Python pipeline that extracts structured invoice information from unstructured text using Google's Gemini API.

The extracted information is validated against a Pydantic schema and saved as a JSON file. The project demonstrates prompt engineering, few-shot examples, LLM integration, structured output, and schema validation.

## Features

- Integrates with the Google Gemini API.
- Uses parameterized prompt templates.
- Uses few-shot examples to guide invoice extraction.
- Extracts invoice details from plain-text documents.
- Validates extracted data using Pydantic.
- Handles missing invoice fields using `null`.
- Saves validated results to a JSON file.
- Supports custom input and output file paths.
- Reports input, extraction, validation, and output errors.

## Technology Stack

- Python 3.12+
- Google Gen AI SDK (`google-genai`)
- Pydantic
- Gemini Flash model

## Project Structure

```text
Structured_LLM_Prompt_Pipeline_and_JSON_Extractor/
├── main.py
├── extractor.py
├── models.py
├── prompts.py
├── sample_invoice.txt
├── output.json
└── README.md
```

| File | Purpose |
|---|---|
| `main.py` | Reads the input file, runs extraction, and saves JSON. |
| `extractor.py` | Calls Gemini and validates the response. |
| `models.py` | Defines the Pydantic invoice schema. |
| `prompts.py` | Defines the parameterized invoice prompt and few-shot examples. |
| `sample_invoice.txt` | Sample unstructured invoice text. |
| `output.json` | Generated JSON output after a successful run. |

## Extracted Fields

The pipeline extracts the following fields:

| Field | Description |
|---|---|
| `invoice_number` | Invoice identifier |
| `invoice_date` | Invoice issue date |
| `vendor_name` | Name of the vendor |
| `total_amount` | Final invoice amount |
| `currency` | Three-letter currency code, such as INR |

If a field is missing from the source document, the model is instructed to return `null`.

## Prerequisites

- Python 3.12 or later
- A Google Gemini API key
- An active internet connection

## Setup

### 1. Create and activate a virtual environment

From the internship repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If the repository already has a virtual environment, activate the existing one instead of creating another.

### 2. Install dependencies

```bash
python -m pip install google-genai pydantic
```

### 3. Configure the Gemini API key

Set the API key as an environment variable:

```bash
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your actual key. Do not commit API keys to GitHub.

Verify the configuration without displaying the key:

```bash
python -c 'import os; print(bool(os.getenv("GEMINI_API_KEY")))'
```

The expected output is `True`.

## Usage

Run the executable pipeline from this directory:

```bash
python main.py sample_invoice.txt
```

To specify a custom output file:

```bash
python main.py sample_invoice.txt --output extracted_invoice.json
```

The script reads the input text, sends it to Gemini, validates the extracted data using Pydantic, and writes the validated result to the specified JSON file.

## Example Input

```text
INVOICE

Invoice Ref: INV-2026-1042

Issued by: Sunrise Office Supplies Pvt. Ltd.
Address: 14 Lake View Road, Hyderabad, Telangana

Bill To: Datheon Technologies
Invoice Date: 22 October 2026

Description: Office stationery and printer supplies
Subtotal: INR 4,800.00
GST: INR 864.00

Please remit the total amount of INR 5,664.00.

Payment Terms: Due within 15 days.
```

## Example Output

A successful run creates `output.json` with a structure similar to:

```json
{
  "invoice_number": "INV-2026-1042",
  "invoice_date": "2026-10-22",
  "vendor_name": "Sunrise Office Supplies Pvt. Ltd.",
  "total_amount": "5664.00",
  "currency": "INR"
}
```

The exact serialized decimal representation may vary.

## Validation and Error Handling

The pipeline uses Pydantic to validate the extracted data against the invoice schema.

It checks field types, validates date values, and supports missing fields represented as `null`. The script also handles empty or unreadable input files, invalid model output, and output-file errors.

Schema validation confirms that the data matches the defined types and structure; it does not independently guarantee that every extracted value is factually correct.

## Execution Flow

1. Read unstructured invoice text from a file.
2. Build the extraction prompt using the prompt template.
3. Send the prompt to Gemini.
4. Parse the model's JSON response.
5. Validate the extracted fields using Pydantic.
6. Save the validated data as JSON.
7. Display the result and report success or failure.

## Scope

This implementation focuses on extracting invoice information from plain-text documents. PDF and image upload, OCR, and a graphical user interface are outside the current scope.

## Task Objective

Deliver an executable Python script that parses unstructured text documents into structured, validated JSON schemas using an LLM and Pydantic.
