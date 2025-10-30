from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_calendars_calendar_id_appointments_appointment_id_response_200_data_base_image_type_0_image_option_crop import (
        PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOptionCrop,
    )
    from ..models.put_calendars_calendar_id_appointments_appointment_id_response_200_data_base_image_type_0_image_option_focus import (
        PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOptionFocus,
    )


T = TypeVar(
    "T",
    bound="PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOption",
)


@_attrs_define
class PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOption:
    """
    Attributes:
        crop (PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOptionCrop | Unset):
        focus (PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOptionFocus | Unset):
    """

    crop: (
        PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOptionCrop
        | Unset
    ) = UNSET
    focus: (
        PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOptionFocus
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
        from ..models.put_calendars_calendar_id_appointments_appointment_id_response_200_data_base_image_type_0_image_option_crop import (
            PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOptionCrop,
        )
        from ..models.put_calendars_calendar_id_appointments_appointment_id_response_200_data_base_image_type_0_image_option_focus import (
            PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOptionFocus,
        )

        d = dict(src_dict)
        _crop = d.pop("crop", UNSET)
        crop: (
            PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOptionCrop
            | Unset
        )
        if isinstance(_crop, Unset):
            crop = UNSET
        else:
            crop = PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOptionCrop.from_dict(
                _crop
            )

        _focus = d.pop("focus", UNSET)
        focus: (
            PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOptionFocus
            | Unset
        )
        if isinstance(_focus, Unset):
            focus = UNSET
        else:
            focus = PutCalendarsCalendarIdAppointmentsAppointmentIdResponse200DataBaseImageType0ImageOptionFocus.from_dict(
                _focus
            )

        put_calendars_calendar_id_appointments_appointment_id_response_200_data_base_image_type_0_image_option = cls(
            crop=crop,
            focus=focus,
        )

        put_calendars_calendar_id_appointments_appointment_id_response_200_data_base_image_type_0_image_option.additional_properties = d
        return put_calendars_calendar_id_appointments_appointment_id_response_200_data_base_image_type_0_image_option

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
