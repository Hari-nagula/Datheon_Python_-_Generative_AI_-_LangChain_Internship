INVOICE_PROMPT_TEMPLATE = """
You are a document data extraction assistant.

Extract the required fields from the invoice text below.

Rules:
1. Return only a JSON object.
2. Do not include Markdown fences or explanations.
3. Do not guess missing information.
4. Use YYYY-MM-DD for invoice_date.
5. Represent total_amount as a decimal number.
6. Use a three-letter currency code when identifiable.
7. If a field is missing, use null.

Required JSON fields:
- invoice_number
- invoice_date
- vendor_name
- total_amount
- currency

Example:

Invoice text:
Invoice Number: INV-101
Date: 2026-10-01
Vendor: ABC Technologies
Total: INR 1500.00

Expected JSON:
{{
  "invoice_number": "INV-101",
  "invoice_date": "2026-10-01",
  "vendor_name": "ABC Technologies",
  "total_amount": 1500.00,
  "currency": "INR"
}}


Example 2:

Invoice text:
Invoice Number: INV-102
Vendor: Sample Company
Total: INR 750.00

Expected JSON:
{{
  "invoice_number": "INV-102",
  "invoice_date": null,
  "vendor_name": "Sample Company",
  "total_amount": 750.00,
  "currency": "INR"
}}


Now extract data from this invoice:

Invoice text:
{document_text}
"""


def build_invoice_prompt(document_text: str) -> str:
    return INVOICE_PROMPT_TEMPLATE.format(
        document_text=document_text
    )

