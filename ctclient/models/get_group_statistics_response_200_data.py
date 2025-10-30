from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_group_statistics_response_200_data_members import (
        GetGroupStatisticsResponse200DataMembers,
    )
    from ..models.get_group_statistics_response_200_data_unfiltered import (
        GetGroupStatisticsResponse200DataUnfiltered,
    )


T = TypeVar("T", bound="GetGroupStatisticsResponse200Data")


@_attrs_define
class GetGroupStatisticsResponse200Data:
    """Calculated facts about one group.

    Attributes:
        members (GetGroupStatisticsResponse200DataMembers): The keys are of format xx:yy where xx is a group type role
            id and yy is a group member status
        unfiltered (GetGroupStatisticsResponse200DataUnfiltered):
    """

    members: GetGroupStatisticsResponse200DataMembers
    unfiltered: GetGroupStatisticsResponse200DataUnfiltered
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
        from ..models.get_group_statistics_response_200_data_members import (
            GetGroupStatisticsResponse200DataMembers,
        )
        from ..models.get_group_statistics_response_200_data_unfiltered import (
            GetGroupStatisticsResponse200DataUnfiltered,
        )

        d = dict(src_dict)
        members = GetGroupStatisticsResponse200DataMembers.from_dict(d.pop("members"))

        unfiltered = GetGroupStatisticsResponse200DataUnfiltered.from_dict(
            d.pop("unfiltered")
        )

        get_group_statistics_response_200_data = cls(
            members=members,
            unfiltered=unfiltered,
        )

        get_group_statistics_response_200_data.additional_properties = d
        return get_group_statistics_response_200_data

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
