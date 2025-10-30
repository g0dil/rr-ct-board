from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RefreshDynamicgroupsResponse200DataItem")


@_attrs_define
class RefreshDynamicgroupsResponse200DataItem:
    """
    Attributes:
        created (int | Unset):
        deleted (int | Unset):
        group_id (int | Unset):
        updated (int | Unset):
    """

    created: int | Unset = UNSET
    deleted: int | Unset = UNSET
    group_id: int | Unset = UNSET
    updated: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        deleted = self.deleted

        group_id = self.group_id

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created", UNSET)

        deleted = d.pop("deleted", UNSET)

        group_id = d.pop("groupId", UNSET)

        updated = d.pop("updated", UNSET)

        refresh_dynamicgroups_response_200_data_item = cls(
            created=created,
            deleted=deleted,
            group_id=group_id,
            updated=updated,
        )

        refresh_dynamicgroups_response_200_data_item.additional_properties = d
        return refresh_dynamicgroups_response_200_data_item

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
