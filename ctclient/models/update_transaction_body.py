from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTransactionBody")


@_attrs_define
class UpdateTransactionBody:
    """
    Example:
        {'accountId': 10, 'amount': 7812, 'contraAccountId': 11, 'costCenterId': 12, 'documentDate': '2019-01-14',
            'documentNumber': '4/4', 'donatorId': 13, 'isImmutable': False, 'note': 'This is a transaction'}

    Attributes:
        account_id (int):
        amount (int): Value is in cent.
        contra_account_id (int):
        cost_center_id (int):
        document_date (datetime.date):
        document_number (str):
        note (str):
        cash_discount_amount (int | Unset): Value is in cent.
        cash_discount_id (int | Unset):
        donator_id (int | Unset):
        is_immutable (bool | Unset): If `true` this transaction is immutable and cannot be edited or deleted. Default:
            False.
        tax_rate_id (int | Unset): If updated, the corresponding tax split booking automatically gets updated.
    """

    account_id: int
    amount: int
    contra_account_id: int
    cost_center_id: int
    document_date: datetime.date
    document_number: str
    note: str
    cash_discount_amount: int | Unset = UNSET
    cash_discount_id: int | Unset = UNSET
    donator_id: int | Unset = UNSET
    is_immutable: bool | Unset = False
    tax_rate_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        amount = self.amount

        contra_account_id = self.contra_account_id

        cost_center_id = self.cost_center_id

        document_date = self.document_date.isoformat()

        document_number = self.document_number

        note = self.note

        cash_discount_amount = self.cash_discount_amount

        cash_discount_id = self.cash_discount_id

        donator_id = self.donator_id

        is_immutable = self.is_immutable

        tax_rate_id = self.tax_rate_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "amount": amount,
                "contraAccountId": contra_account_id,
                "costCenterId": cost_center_id,
                "documentDate": document_date,
                "documentNumber": document_number,
                "note": note,
            }
        )
        if cash_discount_amount is not UNSET:
            field_dict["cashDiscountAmount"] = cash_discount_amount
        if cash_discount_id is not UNSET:
            field_dict["cashDiscountId"] = cash_discount_id
        if donator_id is not UNSET:
            field_dict["donatorId"] = donator_id
        if is_immutable is not UNSET:
            field_dict["isImmutable"] = is_immutable
        if tax_rate_id is not UNSET:
            field_dict["taxRateId"] = tax_rate_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId")

        amount = d.pop("amount")

        contra_account_id = d.pop("contraAccountId")

        cost_center_id = d.pop("costCenterId")

        document_date = isoparse(d.pop("documentDate")).date()

        document_number = d.pop("documentNumber")

        note = d.pop("note")

        cash_discount_amount = d.pop("cashDiscountAmount", UNSET)

        cash_discount_id = d.pop("cashDiscountId", UNSET)

        donator_id = d.pop("donatorId", UNSET)

        is_immutable = d.pop("isImmutable", UNSET)

        tax_rate_id = d.pop("taxRateId", UNSET)

        update_transaction_body = cls(
            account_id=account_id,
            amount=amount,
            contra_account_id=contra_account_id,
            cost_center_id=cost_center_id,
            document_date=document_date,
            document_number=document_number,
            note=note,
            cash_discount_amount=cash_discount_amount,
            cash_discount_id=cash_discount_id,
            donator_id=donator_id,
            is_immutable=is_immutable,
            tax_rate_id=tax_rate_id,
        )

        update_transaction_body.additional_properties = d
        return update_transaction_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
