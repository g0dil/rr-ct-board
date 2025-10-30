from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appointment_base_image_type_0_image_option_crop import (
        AppointmentBaseImageType0ImageOptionCrop,
    )
    from ..models.appointment_base_image_type_0_image_option_focus import (
        AppointmentBaseImageType0ImageOptionFocus,
    )


T = TypeVar("T", bound="AppointmentBaseImageType0ImageOption")


@_attrs_define
class AppointmentBaseImageType0ImageOption:
    """
    Attributes:
        crop (AppointmentBaseImageType0ImageOptionCrop | Unset):
        focus (AppointmentBaseImageType0ImageOptionFocus | Unset):
    """

    crop: AppointmentBaseImageType0ImageOptionCrop | Unset = UNSET
    focus: AppointmentBaseImageType0ImageOptionFocus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.crop, Unset):
            crop = self.crop.to_dict()

        focus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.focus, Unset):
            focus = self.focus.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crop is not UNSET:
            field_dict["crop"] = crop
        if focus is not UNSET:
            field_dict["focus"] = focus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appointment_base_image_type_0_image_option_crop import (
            AppointmentBaseImageType0ImageOptionCrop,
        )
        from ..models.appointment_base_image_type_0_image_option_focus import (
            AppointmentBaseImageType0ImageOptionFocus,
        )

        d = dict(src_dict)
        _crop = d.pop("crop", UNSET)
        crop: AppointmentBaseImageType0ImageOptionCrop | Unset
        if isinstance(_crop, Unset):
            crop = UNSET
        else:
            crop = AppointmentBaseImageType0ImageOptionCrop.from_dict(_crop)

        _focus = d.pop("focus", UNSET)
        focus: AppointmentBaseImageType0ImageOptionFocus | Unset
        if isinstance(_focus, Unset):
            focus = UNSET
        else:
            focus = AppointmentBaseImageType0ImageOptionFocus.from_dict(_focus)

        appointment_base_image_type_0_image_option = cls(
            crop=crop,
            focus=focus,
        )

        appointment_base_image_type_0_image_option.additional_properties = d
        return appointment_base_image_type_0_image_option

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
