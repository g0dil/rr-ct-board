from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_dbfields_field_id_response_200_data_field_type_intern_code import (
    GetDbfieldsFieldIdResponse200DataFieldTypeInternCode,
)

T = TypeVar("T", bound="GetDbfieldsFieldIdResponse200DataFieldType")


@_attrs_define
class GetDbfieldsFieldIdResponse200DataFieldType:
    """
    Attributes:
        id (int):
        intern_code (GetDbfieldsFieldIdResponse200DataFieldTypeInternCode): The intern code of the field type the field
            belongs to. This is used to define the type of the field.
        name (str):
        sort_key (int):
    """

    id: int
    intern_code: GetDbfieldsFieldIdResponse200DataFieldTypeInternCode
    name: str
    sort_key: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        intern_code = self.intern_code.value

        name = self.name

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "internCode": intern_code,
                "name": name,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        intern_code = GetDbfieldsFieldIdResponse200DataFieldTypeInternCode(
            d.pop("internCode")
        )

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        get_dbfields_field_id_response_200_data_field_type = cls(
            id=id,
            intern_code=intern_code,
            name=name,
            sort_key=sort_key,
        )

        get_dbfields_field_id_response_200_data_field_type.additional_properties = d
        return get_dbfields_field_id_response_200_data_field_type

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
