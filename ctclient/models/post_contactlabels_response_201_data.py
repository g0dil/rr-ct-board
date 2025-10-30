from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostContactlabelsResponse201Data")


@_attrs_define
class PostContactlabelsResponse201Data:
    """Master Data for Contact Labels. Used to label E-Mail Adresses.

    Attributes:
        id (int): ID of Record Example: 1.
        is_default (bool): Indicator if label is the default. Used for new person emails
        name (str): Name of Label Example: Private.
        name_translated (str): Translated Name of Label Example: Privat.
        sort_key (int):  Example: 10.
    """

    id: int
    is_default: bool
    name: str
    name_translated: str
    sort_key: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_default = self.is_default

        name = self.name

        name_translated = self.name_translated

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "isDefault": is_default,
                "name": name,
                "nameTranslated": name_translated,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        is_default = d.pop("isDefault")

        name = d.pop("name")

        name_translated = d.pop("nameTranslated")

        sort_key = d.pop("sortKey")

        post_contactlabels_response_201_data = cls(
            id=id,
            is_default=is_default,
            name=name,
            name_translated=name_translated,
            sort_key=sort_key,
        )

        post_contactlabels_response_201_data.additional_properties = d
        return post_contactlabels_response_201_data

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
