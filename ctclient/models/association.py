from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Association")


@_attrs_define
class Association:
    """
    Attributes:
        abbreviation (str):
        country (str):
        id (float):
        key (str):
        name (str):
    """

    abbreviation: str
    country: str
    id: float
    key: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abbreviation = self.abbreviation

        country = self.country

        id = self.id

        key = self.key

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "abbreviation": abbreviation,
                "country": country,
                "id": id,
                "key": key,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        abbreviation = d.pop("abbreviation")

        country = d.pop("country")

        id = d.pop("id")

        key = d.pop("key")

        name = d.pop("name")

        association = cls(
            abbreviation=abbreviation,
            country=country,
            id=id,
            key=key,
            name=name,
        )

        association.additional_properties = d
        return association

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
