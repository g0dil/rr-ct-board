from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppointmentCalculatedBaseImageType0ImageOptionFocus")


@_attrs_define
class AppointmentCalculatedBaseImageType0ImageOptionFocus:
    """
    Attributes:
        x (str | Unset):  Example: 0.50000.
        y (str | Unset):  Example: 0.50000.
    """

    x: str | Unset = UNSET
    y: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x = self.x

        y = self.y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        appointment_calculated_base_image_type_0_image_option_focus = cls(
            x=x,
            y=y,
        )

        appointment_calculated_base_image_type_0_image_option_focus.additional_properties = d
        return appointment_calculated_base_image_type_0_image_option_focus

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
