from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetPersonMasterdataResponse200DataGrowPathsItem")


@_attrs_define
class GetPersonMasterdataResponse200DataGrowPathsItem:
    """
    Attributes:
        color (str):  Example: gray.
        id (int):  Example: 1.
        name (str):  Example: Willkommen.
        name_translated (str):  Example: Willkommen.
        sort_key (int):  Example: 1.
    """

    color: str
    id: int
    name: str
    name_translated: str
    sort_key: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color

        id = self.id

        name = self.name

        name_translated = self.name_translated

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "id": id,
                "name": name,
                "nameTranslated": name_translated,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color")

        id = d.pop("id")

        name = d.pop("name")

        name_translated = d.pop("nameTranslated")

        sort_key = d.pop("sortKey")

        get_person_masterdata_response_200_data_grow_paths_item = cls(
            color=color,
            id=id,
            name=name,
            name_translated=name_translated,
            sort_key=sort_key,
        )

        get_person_masterdata_response_200_data_grow_paths_item.additional_properties = d
        return get_person_masterdata_response_200_data_grow_paths_item

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
