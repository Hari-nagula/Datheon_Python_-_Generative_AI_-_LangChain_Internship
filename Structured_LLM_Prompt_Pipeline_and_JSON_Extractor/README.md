# Structured LLM Prompt Pipeline and JSON Extractor

## Overview
A Python application that uses Google's Gemini API to extract structured data from invoice text. It uses parameterized prompt templates, few-shot examples, JSON output, and Pydantic validation.

## Requirements
- Python 3
- Google Gemini API key
- `google-genai`
- `pydantic`

## Setup
Activate the project's virtual environment and install dependencies:

```bash
python -m pip install google-genai pydantic
```

Set your API key in the terminal:

```bash
export GEMINI_API_KEY="your_api_key"
```

Keep your API key private. Do not commit it to source control.

## Files
- `models.py` — Defines the Pydantic invoice schema.
- `prompts.py` — Contains the parameterized invoice prompt and few-shot examples.
- `extractor.py` — Calls Gemini, parses the JSON response, and validates it using Pydantic.

## Run
From this directory, execute:

```bash
python -c 'from extractor import extract_invoice; result = extract_invoice("Invoice Number: INV-101\nDate: 2026-10-01\nVendor: ABC Technologies\nTotal: INR 1500.00"); print(result.model_dump_json(indent=2))'
```

## Validation
The application validates the extracted invoice fields using Pydantic. Missing fields may be represented as `null`, and invalid values such as an incorrectly formatted date are rejected.

## API costs
Gemini API usage is subject to the selected model's availability, quotas, and applicable free-tier limits.

