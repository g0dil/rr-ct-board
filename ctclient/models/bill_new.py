from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillNew")


@_attrs_define
class BillNew:
    """
    Attributes:
        accounting_period_id (int):
        file_id (int):
        submitted_date (datetime.date):
        submitted_pid (int):
        filename (str | Unset):
        split_transaction_id (int | Unset):
        transaction_id (int | Unset):
        transaction_suggestion_id (int | Unset):
    """

    accounting_period_id: int
    file_id: int
    submitted_date: datetime.date
    submitted_pid: int
    filename: str | Unset = UNSET
    split_transaction_id: int | Unset = UNSET
    transaction_id: int | Unset = UNSET
    transaction_suggestion_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_period_id = self.accounting_period_id

        file_id = self.file_id

        submitted_date = self.submitted_date.isoformat()

        submitted_pid = self.submitted_pid

        filename = self.filename

        split_transaction_id = self.split_transaction_id

        transaction_id = self.transaction_id

        transaction_suggestion_id = self.transaction_suggestion_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountingPeriodId": accounting_period_id,
                "fileId": file_id,
                "submittedDate": submitted_date,
                "submittedPid": submitted_pid,
            }
        )
        if filename is not UNSET:
            field_dict["filename"] = filename
        if split_transaction_id is not UNSET:
            field_dict["splitTransactionId"] = split_transaction_id
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if transaction_suggestion_id is not UNSET:
            field_dict["transactionSuggestionId"] = transaction_suggestion_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounting_period_id = d.pop("accountingPeriodId")

        file_id = d.pop("fileId")

        submitted_date = isoparse(d.pop("submittedDate")).date()

        submitted_pid = d.pop("submittedPid")

        filename = d.pop("filename", UNSET)

        split_transaction_id = d.pop("splitTransactionId", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        transaction_suggestion_id = d.pop("transactionSuggestionId", UNSET)

        bill_new = cls(
            accounting_period_id=accounting_period_id,
            file_id=file_id,
            submitted_date=submitted_date,
            submitted_pid=submitted_pid,
            filename=filename,
            split_transaction_id=split_transaction_id,
            transaction_id=transaction_id,
            transaction_suggestion_id=transaction_suggestion_id,
        )

        bill_new.additional_properties = d
        return bill_new

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
