from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDbfieldtypesResponse200DataItem")


@_attrs_define
class GetDbfieldtypesResponse200DataItem:
    """
    Attributes:
        id (int | Unset):
        intern_code (str | Unset):
        name (str | Unset):
        sort_key (int | Unset):
    """

    id: int | Unset = UNSET
    intern_code: str | Unset = UNSET
    name: str | Unset = UNSET
    sort_key: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        intern_code = self.intern_code

        name = self.name

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if intern_code is not UNSET:
            field_dict["internCode"] = intern_code
        if name is not UNSET:
            field_dict["name"] = name
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        intern_code = d.pop("internCode", UNSET)

        name = d.pop("name", UNSET)

        sort_key = d.pop("sortKey", UNSET)

        get_dbfieldtypes_response_200_data_item = cls(
            id=id,
            intern_code=intern_code,
            name=name,
            sort_key=sort_key,
        )

        get_dbfieldtypes_response_200_data_item.additional_properties = d
        return get_dbfieldtypes_response_200_data_item

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
