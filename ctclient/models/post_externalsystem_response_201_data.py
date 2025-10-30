from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostExternalsystemResponse201Data")


@_attrs_define
class PostExternalsystemResponse201Data:
    """
    Attributes:
        id (int):  Example: 7.
        name_translated (str):  Example: Main Hall.
        campus_id (int | None | Unset):  Example: 5.
        name (str | Unset):  Example: Room.
        name_plural (str | Unset):  Example: Rooms.
        sort_key (int | Unset):  Example: 1.
        does_require_cal_entry (bool | Unset): use `needsAppointment` instead
    """

    id: int
    name_translated: str
    campus_id: int | None | Unset = UNSET
    name: str | Unset = UNSET
    name_plural: str | Unset = UNSET
    sort_key: int | Unset = UNSET
    does_require_cal_entry: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name_translated = self.name_translated

        campus_id: int | None | Unset
        if isinstance(self.campus_id, Unset):
            campus_id = UNSET
        else:
            campus_id = self.campus_id

        name = self.name

        name_plural = self.name_plural

        sort_key = self.sort_key

        does_require_cal_entry = self.does_require_cal_entry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nameTranslated": name_translated,
            }
        )
        if campus_id is not UNSET:
            field_dict["campusId"] = campus_id
        if name is not UNSET:
            field_dict["name"] = name
        if name_plural is not UNSET:
            field_dict["namePlural"] = name_plural
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key
        if does_require_cal_entry is not UNSET:
            field_dict["doesRequireCalEntry"] = does_require_cal_entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name_translated = d.pop("nameTranslated")

        def _parse_campus_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        campus_id = _parse_campus_id(d.pop("campusId", UNSET))

        name = d.pop("name", UNSET)

        name_plural = d.pop("namePlural", UNSET)

        sort_key = d.pop("sortKey", UNSET)

        does_require_cal_entry = d.pop("doesRequireCalEntry", UNSET)

        post_externalsystem_response_201_data = cls(
            id=id,
            name_translated=name_translated,
            campus_id=campus_id,
            name=name,
            name_plural=name_plural,
            sort_key=sort_key,
            does_require_cal_entry=does_require_cal_entry,
        )

        post_externalsystem_response_201_data.additional_properties = d
        return post_externalsystem_response_201_data

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
