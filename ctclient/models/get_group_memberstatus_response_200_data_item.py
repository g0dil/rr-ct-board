from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_group_memberstatus_response_200_data_item_id import (
    GetGroupMemberstatusResponse200DataItemId,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGroupMemberstatusResponse200DataItem")


@_attrs_define
class GetGroupMemberstatusResponse200DataItem:
    """
    Attributes:
        id (GetGroupMemberstatusResponse200DataItemId | Unset):
        name (str | Unset):
    """

    id: GetGroupMemberstatusResponse200DataItemId | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: GetGroupMemberstatusResponse200DataItemId | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = GetGroupMemberstatusResponse200DataItemId(_id)

        name = d.pop("name", UNSET)

        get_group_memberstatus_response_200_data_item = cls(
            id=id,
            name=name,
        )

        get_group_memberstatus_response_200_data_item.additional_properties = d
        return get_group_memberstatus_response_200_data_item

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
