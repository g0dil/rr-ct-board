from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_calendars_calendar_id_appointments_appointment_id_response_200_data_base import (
        PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBase,
    )
    from ..models.put_calendars_calendar_id_appointments_appointment_id_response_200_data_calculated import (
        PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataCalculated,
    )


T = TypeVar("T", bound="PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200Data")


@_attrs_define
class PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200Data:
    """
    Attributes:
        base (PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBase):
        calculated (PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataCalculated):
    """

    base: PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBase
    calculated: PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataCalculated
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base = self.base.to_dict()

        calculated = self.calculated.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base": base,
                "calculated": calculated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_calendars_calendar_id_appointments_appointment_id_response_200_data_base import (
            PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBase,
        )
        from ..models.put_calendars_calendar_id_appointments_appointment_id_response_200_data_calculated import (
            PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataCalculated,
        )

        d = dict(src_dict)
        base = PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBase.from_dict(
            d.pop("base")
        )

        calculated = PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataCalculated.from_dict(
            d.pop("calculated")
        )

        put_calendars_calendar_id_appointments_appointment_id_response_200_data = cls(
            base=base,
            calculated=calculated,
        )

        put_calendars_calendar_id_appointments_appointment_id_response_200_data.additional_properties = d
        return put_calendars_calendar_id_appointments_appointment_id_response_200_data

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
