from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.language_code import LanguageCode

T = TypeVar("T", bound="Language")


@_attrs_define
class Language:
    """
    Attributes:
        code (LanguageCode): The language code is a two-letter code that represents the language. For example, "en" for
            English, "de" for German, and "fr" for French.
        id (int):
        is_active (bool):
        name (str):
        sort_key (int):
    """

    code: LanguageCode
    id: int
    is_active: bool
    name: str
    sort_key: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        id = self.id

        is_active = self.is_active

        name = self.name

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "id": id,
                "isActive": is_active,
                "name": name,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = LanguageCode(d.pop("code"))

        id = d.pop("id")

        is_active = d.pop("isActive")

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        language = cls(
            code=code,
            id=id,
            is_active=is_active,
            name=name,
            sort_key=sort_key,
        )

        language.additional_properties = d
        return language

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
