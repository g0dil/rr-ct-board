from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGroupHomepagesResponse200DataItemDomainAttributes")


@_attrs_define
class GetGroupHomepagesResponse200DataItemDomainAttributes:
    """
    Attributes:
        child_group_ids (list[int]):
        parent_group_id (int):
    """

    child_group_ids: list[int]
    parent_group_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        child_group_ids = self.child_group_ids

        parent_group_id = self.parent_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "childGroupIds": child_group_ids,
                "parentGroupId": parent_group_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        child_group_ids = cast(list[int], d.pop("childGroupIds"))

        parent_group_id = d.pop("parentGroupId")

        get_group_homepages_response_200_data_item_domain_attributes = cls(
            child_group_ids=child_group_ids,
            parent_group_id=parent_group_id,
        )

        get_group_homepages_response_200_data_item_domain_attributes.additional_properties = d
        return get_group_homepages_response_200_data_item_domain_attributes

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
