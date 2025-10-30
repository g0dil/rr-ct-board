from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarMeta")


@_attrs_define
class CalendarMeta:
    """
    Attributes:
        modified_date (datetime.datetime | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        modified_pid (int | Unset):
    """

    modified_date: datetime.datetime | Unset = UNSET
    modified_pid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modified_date: str | Unset = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat()

        modified_pid = self.modified_pid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if modified_pid is not UNSET:
            field_dict["modifiedPid"] = modified_pid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: datetime.datetime | Unset
        if isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        modified_pid = d.pop("modifiedPid", UNSET)

        calendar_meta = cls(
            modified_date=modified_date,
            modified_pid=modified_pid,
        )

        calendar_meta.additional_properties = d
        return calendar_meta

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
