import json
from google import genai 
from models import InvoiceData
from prompts import build_invoice_prompt

def extract_invoice(document_text: str) -> InvoiceData:
    client = genai.Client()

    prompt = build_invoice_prompt(document_text)

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
        },
    )

    content = response.text

    if not content:
        raise ValueError("The model returned an empty response.")

    extracted_data = json.loads(content)

    return InvoiceData.model_validate(extracted_data)
