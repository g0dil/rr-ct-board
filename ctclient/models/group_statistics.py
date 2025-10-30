from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.group_statistics_members import GroupStatisticsMembers
    from ..models.group_statistics_unfiltered import GroupStatisticsUnfiltered


T = TypeVar("T", bound="GroupStatistics")


@_attrs_define
class GroupStatistics:
    """Calculated facts about one group.

    Attributes:
        members (GroupStatisticsMembers): The keys are of format xx:yy where xx is a group type role id and yy is a
            group member status
        unfiltered (GroupStatisticsUnfiltered):
    """

    members: GroupStatisticsMembers
    unfiltered: GroupStatisticsUnfiltered
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        members = self.members.to_dict()

        unfiltered = self.unfiltered.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "members": members,
                "unfiltered": unfiltered,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_statistics_members import GroupStatisticsMembers
        from ..models.group_statistics_unfiltered import GroupStatisticsUnfiltered

        d = dict(src_dict)
        members = GroupStatisticsMembers.from_dict(d.pop("members"))

        unfiltered = GroupStatisticsUnfiltered.from_dict(d.pop("unfiltered"))

        group_statistics = cls(
            members=members,
            unfiltered=unfiltered,
        )

        group_statistics.additional_properties = d
        return group_statistics

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
