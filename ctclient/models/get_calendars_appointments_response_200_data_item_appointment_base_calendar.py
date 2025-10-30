from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_calendars_appointments_response_200_data_item_appointment_base_calendar_meta import (
        GetCalendarsAppointmentsResponse200DataItemAppointmentBaseCalendarMeta,
    )


T = TypeVar(
    "T", bound="GetCalendarsAppointmentsResponse200DataItemAppointmentBaseCalendar"
)


@_attrs_define
class GetCalendarsAppointmentsResponse200DataItemAppointmentBaseCalendar:
    """
    Attributes:
        id (int):
        meta (GetCalendarsAppointmentsResponse200DataItemAppointmentBaseCalendarMeta):
        name_translated (str):
        random_url (str):
        is_private (bool | Unset):
        is_public (bool | Unset):
    """

    id: int
    meta: GetCalendarsAppointmentsResponse200DataItemAppointmentBaseCalendarMeta
    name_translated: str
    random_url: str
    is_private: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        meta = self.meta.to_dict()

        name_translated = self.name_translated

        random_url = self.random_url

        is_private = self.is_private

        is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "meta": meta,
                "nameTranslated": name_translated,
                "randomUrl": random_url,
            }
        )
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_calendars_appointments_response_200_data_item_appointment_base_calendar_meta import (
            GetCalendarsAppointmentsResponse200DataItemAppointmentBaseCalendarMeta,
        )

        d = dict(src_dict)
        id = d.pop("id")

        meta = GetCalendarsAppointmentsResponse200DataItemAppointmentBaseCalendarMeta.from_dict(
            d.pop("meta")
        )

        name_translated = d.pop("nameTranslated")

        random_url = d.pop("randomUrl")

        is_private = d.pop("isPrivate", UNSET)

        is_public = d.pop("isPublic", UNSET)

        get_calendars_appointments_response_200_data_item_appointment_base_calendar = (
            cls(
                id=id,
                meta=meta,
                name_translated=name_translated,
                random_url=random_url,
                is_private=is_private,
                is_public=is_public,
            )
        )

        get_calendars_appointments_response_200_data_item_appointment_base_calendar.additional_properties = d
        return (
            get_calendars_appointments_response_200_data_item_appointment_base_calendar
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
