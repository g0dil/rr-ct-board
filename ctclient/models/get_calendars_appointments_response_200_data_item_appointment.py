from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_calendars_appointments_response_200_data_item_appointment_base import (
        GetCalendarsAppointmentsResponse200DataItemAppointmentBase,
    )
    from ..models.get_calendars_appointments_response_200_data_item_appointment_calculated import (
        GetCalendarsAppointmentsResponse200DataItemAppointmentCalculated,
    )


T = TypeVar("T", bound="GetCalendarsAppointmentsResponse200DataItemAppointment")


@_attrs_define
class GetCalendarsAppointmentsResponse200DataItemAppointment:
    """
    Attributes:
        base (GetCalendarsAppointmentsResponse200DataItemAppointmentBase):
        calculated (GetCalendarsAppointmentsResponse200DataItemAppointmentCalculated):
    """

    base: GetCalendarsAppointmentsResponse200DataItemAppointmentBase
    calculated: GetCalendarsAppointmentsResponse200DataItemAppointmentCalculated
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
        from ..models.get_calendars_appointments_response_200_data_item_appointment_base import (
            GetCalendarsAppointmentsResponse200DataItemAppointmentBase,
        )
        from ..models.get_calendars_appointments_response_200_data_item_appointment_calculated import (
            GetCalendarsAppointmentsResponse200DataItemAppointmentCalculated,
        )

        d = dict(src_dict)
        base = GetCalendarsAppointmentsResponse200DataItemAppointmentBase.from_dict(
            d.pop("base")
        )

        calculated = (
            GetCalendarsAppointmentsResponse200DataItemAppointmentCalculated.from_dict(
                d.pop("calculated")
            )
        )

        get_calendars_appointments_response_200_data_item_appointment = cls(
            base=base,
            calculated=calculated,
        )

        get_calendars_appointments_response_200_data_item_appointment.additional_properties = d
        return get_calendars_appointments_response_200_data_item_appointment

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
