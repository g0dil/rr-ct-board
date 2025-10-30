from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Country")


@_attrs_define
class Country:
    """The details of a country

    Attributes:
        emoji (str | Unset):
        id (int | Unset): ChurchTools ID of country
        iso2 (str | Unset): two letter iso country code
        name (str | Unset): English name of country
        name_translated (str | Unset): Translated name of the country
    """

    emoji: str | Unset = UNSET
    id: int | Unset = UNSET
    iso2: str | Unset = UNSET
    name: str | Unset = UNSET
    name_translated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emoji = self.emoji

        id = self.id

        iso2 = self.iso2

        name = self.name

        name_translated = self.name_translated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if id is not UNSET:
            field_dict["id"] = id
        if iso2 is not UNSET:
            field_dict["iso2"] = iso2
        if name is not UNSET:
            field_dict["name"] = name
        if name_translated is not UNSET:
            field_dict["nameTranslated"] = name_translated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        emoji = d.pop("emoji", UNSET)

        id = d.pop("id", UNSET)

        iso2 = d.pop("iso2", UNSET)

        name = d.pop("name", UNSET)

        name_translated = d.pop("nameTranslated", UNSET)

        country = cls(
            emoji=emoji,
            id=id,
            iso2=iso2,
            name=name,
            name_translated=name_translated,
        )

        country.additional_properties = d
        return country

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
