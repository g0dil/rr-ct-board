from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_calendars_calendar_id_appointments_response_200_data_item_base_image_type_0_image_option_crop import (
        GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOptionCrop,
    )
    from ..models.get_calendars_calendar_id_appointments_response_200_data_item_base_image_type_0_image_option_focus import (
        GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOptionFocus,
    )


T = TypeVar(
    "T",
    bound="GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOption",
)


@_attrs_define
class GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOption:
    """
    Attributes:
        crop (GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOptionCrop | Unset):
        focus (GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOptionFocus | Unset):
    """

    crop: (
        GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOptionCrop
        | Unset
    ) = UNSET
    focus: (
        GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOptionFocus
        | Unset
    ) = UNSET
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
        from ..models.get_calendars_calendar_id_appointments_response_200_data_item_base_image_type_0_image_option_crop import (
            GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOptionCrop,
        )
        from ..models.get_calendars_calendar_id_appointments_response_200_data_item_base_image_type_0_image_option_focus import (
            GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOptionFocus,
        )

        d = dict(src_dict)
        _crop = d.pop("crop", UNSET)
        crop: (
            GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOptionCrop
            | Unset
        )
        if isinstance(_crop, Unset):
            crop = UNSET
        else:
            crop = GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOptionCrop.from_dict(
                _crop
            )

        _focus = d.pop("focus", UNSET)
        focus: (
            GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOptionFocus
            | Unset
        )
        if isinstance(_focus, Unset):
            focus = UNSET
        else:
            focus = GetCalendarsCalendarIdAppointmentsResponse200DataItemBaseImageType0ImageOptionFocus.from_dict(
                _focus
            )

        get_calendars_calendar_id_appointments_response_200_data_item_base_image_type_0_image_option = cls(
            crop=crop,
            focus=focus,
        )

        get_calendars_calendar_id_appointments_response_200_data_item_base_image_type_0_image_option.additional_properties = d
        return get_calendars_calendar_id_appointments_response_200_data_item_base_image_type_0_image_option

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
