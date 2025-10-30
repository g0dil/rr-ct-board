from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_meeting_response_201_data_attendances_additional_property import (
    CreateMeetingResponse201DataAttendancesAdditionalProperty,
)

T = TypeVar("T", bound="CreateMeetingResponse201DataAttendances")


@_attrs_define
class CreateMeetingResponse201DataAttendances:
    """Map of person IDs to attendance status"""

    additional_properties: dict[
        str, CreateMeetingResponse201DataAttendancesAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_meeting_response_201_data_attendances = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                CreateMeetingResponse201DataAttendancesAdditionalProperty(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        create_meeting_response_201_data_attendances.additional_properties = (
            additional_properties
        )
        return create_meeting_response_201_data_attendances

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> CreateMeetingResponse201DataAttendancesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: CreateMeetingResponse201DataAttendancesAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
