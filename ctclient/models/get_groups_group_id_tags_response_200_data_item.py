from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGroupsGroupIdTagsResponse200DataItem")


@_attrs_define
class GetGroupsGroupIdTagsResponse200DataItem:
    """
    Attributes:
        count (int | Unset):
        id (int | Unset):
        modified_at (str | Unset):
        modified_by (int | Unset):
        name (str | Unset):
    """

    count: int | Unset = UNSET
    id: int | Unset = UNSET
    modified_at: str | Unset = UNSET
    modified_by: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        id = self.id

        modified_at = self.modified_at

        modified_by = self.modified_by

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if id is not UNSET:
            field_dict["id"] = id
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        id = d.pop("id", UNSET)

        modified_at = d.pop("modifiedAt", UNSET)

        modified_by = d.pop("modifiedBy", UNSET)

        name = d.pop("name", UNSET)

        get_groups_group_id_tags_response_200_data_item = cls(
            count=count,
            id=id,
            modified_at=modified_at,
            modified_by=modified_by,
            name=name,
        )

        get_groups_group_id_tags_response_200_data_item.additional_properties = d
        return get_groups_group_id_tags_response_200_data_item

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
