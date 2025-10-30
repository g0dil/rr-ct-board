from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAccountingPeriodBody")


@_attrs_define
class UpdateAccountingPeriodBody:
    """
    Example:
        {'clientId': 2, 'endDate': '2019-12-31', 'isClosed': False, 'setImmutable': False, 'startDate': '2019-01-01'}

    Attributes:
        client_id (int):
        end_date (datetime.date):
        is_closed (bool):
        start_date (datetime.date):
        set_immutable (bool | Unset): If `true` all mutable transactions will be set to immutable. Hence no transaction
            will be editable or deletebale afterward. Default: False.
    """

    client_id: int
    end_date: datetime.date
    is_closed: bool
    start_date: datetime.date
    set_immutable: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        end_date = self.end_date.isoformat()

        is_closed = self.is_closed

        start_date = self.start_date.isoformat()

        set_immutable = self.set_immutable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientId": client_id,
                "endDate": end_date,
                "isClosed": is_closed,
                "startDate": start_date,
            }
        )
        if set_immutable is not UNSET:
            field_dict["setImmutable"] = set_immutable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("clientId")

        end_date = isoparse(d.pop("endDate")).date()

        is_closed = d.pop("isClosed")

        start_date = isoparse(d.pop("startDate")).date()

        set_immutable = d.pop("setImmutable", UNSET)

        update_accounting_period_body = cls(
            client_id=client_id,
            end_date=end_date,
            is_closed=is_closed,
            start_date=start_date,
            set_immutable=set_immutable,
        )

        update_accounting_period_body.additional_properties = d
        return update_accounting_period_body

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
