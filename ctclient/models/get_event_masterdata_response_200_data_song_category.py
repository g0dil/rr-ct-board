from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetEventMasterdataResponse200DataSongCategory")


@_attrs_define
class GetEventMasterdataResponse200DataSongCategory:
    """
    Attributes:
        campus_id (int | Unset):
        id (int | Unset):
        name (str | Unset):
        name_translated (str | Unset):
        sort_key (int | Unset):
    """

    campus_id: int | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    name_translated: str | Unset = UNSET
    sort_key: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campus_id = self.campus_id

        id = self.id

        name = self.name

        name_translated = self.name_translated

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campus_id is not UNSET:
            field_dict["campusId"] = campus_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if name_translated is not UNSET:
            field_dict["nameTranslated"] = name_translated
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        campus_id = d.pop("campusId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        name_translated = d.pop("nameTranslated", UNSET)

        sort_key = d.pop("sortKey", UNSET)

        get_event_masterdata_response_200_data_song_category = cls(
            campus_id=campus_id,
            id=id,
            name=name,
            name_translated=name_translated,
            sort_key=sort_key,
        )

        get_event_masterdata_response_200_data_song_category.additional_properties = d
        return get_event_masterdata_response_200_data_song_category

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
