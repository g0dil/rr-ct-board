from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoutineStepCreateWaitActionData")


@_attrs_define
class RoutineStepCreateWaitActionData:
    """
    Attributes:
        num_days (int | Unset):
        until_date (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
    """

    num_days: int | Unset = UNSET
    until_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_days = self.num_days

        until_date: str | Unset = UNSET
        if not isinstance(self.until_date, Unset):
            until_date = self.until_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_days is not UNSET:
            field_dict["numDays"] = num_days
        if until_date is not UNSET:
            field_dict["untilDate"] = until_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num_days = d.pop("numDays", UNSET)

        _until_date = d.pop("untilDate", UNSET)
        until_date: datetime.date | Unset
        if isinstance(_until_date, Unset):
            until_date = UNSET
        else:
            until_date = isoparse(_until_date).date()

        routine_step_create_wait_action_data = cls(
            num_days=num_days,
            until_date=until_date,
        )

        routine_step_create_wait_action_data.additional_properties = d
        return routine_step_create_wait_action_data

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
