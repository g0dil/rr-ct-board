from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_meeting_attendances_additional_property import (
    GroupMeetingAttendancesAdditionalProperty,
)

T = TypeVar("T", bound="GroupMeetingAttendances")


@_attrs_define
class GroupMeetingAttendances:
    """Map of person IDs to attendance status"""

    additional_properties: dict[str, GroupMeetingAttendancesAdditionalProperty] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_meeting_attendances = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GroupMeetingAttendancesAdditionalProperty(prop_dict)

            additional_properties[prop_name] = additional_property

        group_meeting_attendances.additional_properties = additional_properties
        return group_meeting_attendances

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GroupMeetingAttendancesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: GroupMeetingAttendancesAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
