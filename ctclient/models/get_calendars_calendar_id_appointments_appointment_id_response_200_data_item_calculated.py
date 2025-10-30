from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar(
    "T",
    bound="GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemCalculated",
)


@_attrs_define
class GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemCalculated:
    """
    Attributes:
        end_date (datetime.datetime): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        start_date (datetime.datetime): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
    """

    end_date: datetime.datetime
    start_date: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date.isoformat()

        start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endDate": end_date,
                "startDate": start_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_date = isoparse(d.pop("endDate"))

        start_date = isoparse(d.pop("startDate"))

        get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_calculated = cls(
            end_date=end_date,
            start_date=start_date,
        )

        get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_calculated.additional_properties = d
        return get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_calculated

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
