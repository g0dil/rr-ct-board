from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base import (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBase,
    )
    from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_calculated import (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemCalculated,
    )


T = TypeVar(
    "T", bound="GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItem"
)


@_attrs_define
class GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItem:
    """
    Attributes:
        base (GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBase):
        calculated (GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemCalculated):
    """

    base: GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBase
    calculated: (
        GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemCalculated
    )
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
        from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_base import (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBase,
        )
        from ..models.get_calendars_calendar_id_appointments_appointment_id_response_200_data_item_calculated import (
            GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemCalculated,
        )

        d = dict(src_dict)
        base = GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemBase.from_dict(
            d.pop("base")
        )

        calculated = GetCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataItemCalculated.from_dict(
            d.pop("calculated")
        )

        get_calendars_calendar_id_appointments_appointment_id_response_200_data_item = (
            cls(
                base=base,
                calculated=calculated,
            )
        )

        get_calendars_calendar_id_appointments_appointment_id_response_200_data_item.additional_properties = d
        return (
            get_calendars_calendar_id_appointments_appointment_id_response_200_data_item
        )

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
