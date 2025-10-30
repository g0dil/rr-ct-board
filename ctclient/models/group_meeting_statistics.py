from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupMeetingStatistics")


@_attrs_define
class GroupMeetingStatistics:
    """
    Attributes:
        absent (int | Unset):
        not_in_group (int | Unset):
        present (int | Unset):
        unsure (int | Unset):
    """

    absent: int | Unset = UNSET
    not_in_group: int | Unset = UNSET
    present: int | Unset = UNSET
    unsure: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        absent = self.absent

        not_in_group = self.not_in_group

        present = self.present

        unsure = self.unsure

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if absent is not UNSET:
            field_dict["absent"] = absent
        if not_in_group is not UNSET:
            field_dict["not-in-group"] = not_in_group
        if present is not UNSET:
            field_dict["present"] = present
        if unsure is not UNSET:
            field_dict["unsure"] = unsure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        absent = d.pop("absent", UNSET)

        not_in_group = d.pop("not-in-group", UNSET)

        present = d.pop("present", UNSET)

        unsure = d.pop("unsure", UNSET)

        group_meeting_statistics = cls(
            absent=absent,
            not_in_group=not_in_group,
            present=present,
            unsure=unsure,
        )

        group_meeting_statistics.additional_properties = d
        return group_meeting_statistics

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
