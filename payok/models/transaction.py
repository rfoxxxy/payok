import json
from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, validator
from pydantic.fields import Field

from ..enums import Currency, PayStatus, WebhookStatus


class Transaction(BaseModel):
    """
    Class for Transaction model
    """

    id: Union[int, str] = Field(..., alias="payment_id")
    description: str
    email: str
    amount: float
    amount_profit: float
    currency: Union[Currency, str]
    comission_percent: float
    comission_fixed: float
    method: str
    transaction: int
    date: datetime
    pay_date: datetime = Field(default=None)
    status: PayStatus = Field(PayStatus.waiting, alias="transaction_status")
    custom_fields: Optional[dict]
    webhook_status: WebhookStatus
    webhook_amount: int

    @property
    def is_paid(self) -> bool:
        return bool(self.status)

    @validator("custom_fields", pre=True)
    def validate_fields(raw_field: str) -> dict:  # type: ignore
        string = raw_field.replace("&quot;", '"')
        return json.loads(string)
