from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppointmentCalculatedBaseImageType0ImageOptionCrop")


@_attrs_define
class AppointmentCalculatedBaseImageType0ImageOptionCrop:
    """
    Attributes:
        bottom (str | Unset):  Example: 0.00000.
        left (str | Unset):  Example: 0.00000.
        right (str | Unset):  Example: 0.00000.
        top (str | Unset):  Example: 0.00000.
    """

    bottom: str | Unset = UNSET
    left: str | Unset = UNSET
    right: str | Unset = UNSET
    top: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bottom = self.bottom

        left = self.left

        right = self.right

        top = self.top

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bottom is not UNSET:
            field_dict["bottom"] = bottom
        if left is not UNSET:
            field_dict["left"] = left
        if right is not UNSET:
            field_dict["right"] = right
        if top is not UNSET:
            field_dict["top"] = top

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bottom = d.pop("bottom", UNSET)

        left = d.pop("left", UNSET)

        right = d.pop("right", UNSET)

        top = d.pop("top", UNSET)

        appointment_calculated_base_image_type_0_image_option_crop = cls(
            bottom=bottom,
            left=left,
            right=right,
            top=top,
        )

        appointment_calculated_base_image_type_0_image_option_crop.additional_properties = d
        return appointment_calculated_base_image_type_0_image_option_crop

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
