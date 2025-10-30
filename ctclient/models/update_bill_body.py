from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBillBody")


@_attrs_define
class UpdateBillBody:
    """
    Attributes:
        submitted_date (datetime.date):
        submitted_pid (int):
        filename (str | Unset):
        split_transaction_id (int | Unset):
        transaction_id (int | Unset):
        transaction_suggestion_id (int | Unset):
    """

    submitted_date: datetime.date
    submitted_pid: int
    filename: str | Unset = UNSET
    split_transaction_id: int | Unset = UNSET
    transaction_id: int | Unset = UNSET
    transaction_suggestion_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        submitted_date = isoparse(d.pop("submittedDate")).date()

        submitted_pid = d.pop("submittedPid")

        filename = d.pop("filename", UNSET)

        split_transaction_id = d.pop("splitTransactionId", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        transaction_suggestion_id = d.pop("transactionSuggestionId", UNSET)

        update_bill_body = cls(
            submitted_date=submitted_date,
            submitted_pid=submitted_pid,
            filename=filename,
            split_transaction_id=split_transaction_id,
            transaction_id=transaction_id,
            transaction_suggestion_id=transaction_suggestion_id,
        )

        update_bill_body.additional_properties = d
        return update_bill_body

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
