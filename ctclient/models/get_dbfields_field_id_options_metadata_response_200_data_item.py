from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDbfieldsFieldIdOptionsMetadataResponse200DataItem")


@_attrs_define
class GetDbfieldsFieldIdOptionsMetadataResponse200DataItem:
    """
    Attributes:
        is_auto_increment (bool | Unset):
        length (int | None | Unset):
        name (str | Unset):
        type_ (str | Unset):
    """

    is_auto_increment: bool | Unset = UNSET
    length: int | None | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_auto_increment = self.is_auto_increment

        length: int | None | Unset
        if isinstance(self.length, Unset):
            length = UNSET
        else:
            length = self.length

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_auto_increment is not UNSET:
            field_dict["isAutoIncrement"] = is_auto_increment
        if length is not UNSET:
            field_dict["length"] = length
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_auto_increment = d.pop("isAutoIncrement", UNSET)

        def _parse_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        length = _parse_length(d.pop("length", UNSET))

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        get_dbfields_field_id_options_metadata_response_200_data_item = cls(
            is_auto_increment=is_auto_increment,
            length=length,
            name=name,
            type_=type_,
        )

        get_dbfields_field_id_options_metadata_response_200_data_item.additional_properties = d
        return get_dbfields_field_id_options_metadata_response_200_data_item

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
