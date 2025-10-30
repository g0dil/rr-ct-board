from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutCalendarsCalendarIdAppointmentsAppointmentIdBody")


@_attrs_define
class PutCalendarsCalendarIdAppointmentsAppointmentIdBody:
    """
    Attributes:
        appointment_id (int):
    """

    appointment_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appointment_id = self.appointment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appointmentId": appointment_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appointment_id = d.pop("appointmentId")

        put_calendars_calendar_id_appointments_appointment_id_body = cls(
            appointment_id=appointment_id,
        )

        put_calendars_calendar_id_appointments_appointment_id_body.additional_properties = d
        return put_calendars_calendar_id_appointments_appointment_id_body

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
