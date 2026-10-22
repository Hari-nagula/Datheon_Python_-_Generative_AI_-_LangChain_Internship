from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field


class InvoiceData(BaseModel):
    invoice_number: str | None = Field(description="Invoice identifier, or null if missing")
    invoice_date: date | None = Field(description="Date the invoice was issued, or null if missing")
    vendor_name: str | None = Field(description="Name of the company issuing the invoice, or null if missing")
    total_amount: Decimal | None = Field(description="Final invoice amount, or null if missing")
    currency: str | None = Field(description="Currency code, such as INR or USD, or null if missing")

