from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="WidgetDateItemActionData")


@_attrs_define
class WidgetDateItemActionData:
    """
    Attributes:
        appointment_id (int):
        calendar_id (int):
        start_date (datetime.date): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
    """

    appointment_id: int
    calendar_id: int
    start_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appointment_id = self.appointment_id

        calendar_id = self.calendar_id

        start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appointmentId": appointment_id,
                "calendarId": calendar_id,
                "startDate": start_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appointment_id = d.pop("appointmentId")

        calendar_id = d.pop("calendarId")

        start_date = isoparse(d.pop("startDate")).date()

        widget_date_item_action_data = cls(
            appointment_id=appointment_id,
            calendar_id=calendar_id,
            start_date=start_date,
        )

        widget_date_item_action_data.additional_properties = d
        return widget_date_item_action_data

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
