from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.appointment_calculated_with_includes_appointment_base import (
        AppointmentCalculatedWithIncludesAppointmentBase,
    )
    from ..models.appointment_calculated_with_includes_appointment_calculated import (
        AppointmentCalculatedWithIncludesAppointmentCalculated,
    )


T = TypeVar("T", bound="AppointmentCalculatedWithIncludesAppointment")


@_attrs_define
class AppointmentCalculatedWithIncludesAppointment:
    """
    Attributes:
        base (AppointmentCalculatedWithIncludesAppointmentBase):
        calculated (AppointmentCalculatedWithIncludesAppointmentCalculated):
    """

    base: AppointmentCalculatedWithIncludesAppointmentBase
    calculated: AppointmentCalculatedWithIncludesAppointmentCalculated
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
        from ..models.appointment_calculated_with_includes_appointment_base import (
            AppointmentCalculatedWithIncludesAppointmentBase,
        )
        from ..models.appointment_calculated_with_includes_appointment_calculated import (
            AppointmentCalculatedWithIncludesAppointmentCalculated,
        )

        d = dict(src_dict)
        base = AppointmentCalculatedWithIncludesAppointmentBase.from_dict(d.pop("base"))

        calculated = AppointmentCalculatedWithIncludesAppointmentCalculated.from_dict(
            d.pop("calculated")
        )

        appointment_calculated_with_includes_appointment = cls(
            base=base,
            calculated=calculated,
        )

        appointment_calculated_with_includes_appointment.additional_properties = d
        return appointment_calculated_with_includes_appointment

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
