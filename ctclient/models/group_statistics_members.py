from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.group_statistics_members_additional_property import (
        GroupStatisticsMembersAdditionalProperty,
    )


T = TypeVar("T", bound="GroupStatisticsMembers")


@_attrs_define
class GroupStatisticsMembers:
    """The keys are of format xx:yy where xx is a group type role id and yy is a group member status"""

    additional_properties: dict[str, GroupStatisticsMembersAdditionalProperty] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_statistics_members_additional_property import (
            GroupStatisticsMembersAdditionalProperty,
        )

        d = dict(src_dict)
        group_statistics_members = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GroupStatisticsMembersAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        group_statistics_members.additional_properties = additional_properties
        return group_statistics_members

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GroupStatisticsMembersAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: GroupStatisticsMembersAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
