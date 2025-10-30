from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGroupsGroupIdPoststatisticsResponse200DataItem")


@_attrs_define
class GetGroupsGroupIdPoststatisticsResponse200DataItem:
    """
    Attributes:
        group_intern (float):
        group_visible (float):
    """

    group_intern: float
    group_visible: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_intern = self.group_intern

        group_visible = self.group_visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_intern": group_intern,
                "group_visible": group_visible,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_intern = d.pop("group_intern")

        group_visible = d.pop("group_visible")

        get_groups_group_id_poststatistics_response_200_data_item = cls(
            group_intern=group_intern,
            group_visible=group_visible,
        )

        get_groups_group_id_poststatistics_response_200_data_item.additional_properties = d
        return get_groups_group_id_poststatistics_response_200_data_item

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
