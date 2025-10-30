from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AccountingPeriodBase")


@_attrs_define
class AccountingPeriodBase:
    """
    Attributes:
        client_id (int):
        end_date (datetime.date):
        increment_document_number (bool):
        is_closed (bool):
        start_date (datetime.date):
    """

    client_id: int
    end_date: datetime.date
    increment_document_number: bool
    is_closed: bool
    start_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        end_date = self.end_date.isoformat()

        increment_document_number = self.increment_document_number

        is_closed = self.is_closed

        start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientId": client_id,
                "endDate": end_date,
                "incrementDocumentNumber": increment_document_number,
                "isClosed": is_closed,
                "startDate": start_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("clientId")

        end_date = isoparse(d.pop("endDate")).date()

        increment_document_number = d.pop("incrementDocumentNumber")

        is_closed = d.pop("isClosed")

        start_date = isoparse(d.pop("startDate")).date()

        accounting_period_base = cls(
            client_id=client_id,
            end_date=end_date,
            increment_document_number=increment_document_number,
            is_closed=is_closed,
            start_date=start_date,
        )

        accounting_period_base.additional_properties = d
        return accounting_period_base

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
