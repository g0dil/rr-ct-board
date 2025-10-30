from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PersonMasterDataCommentViewersItem")


@_attrs_define
class PersonMasterDataCommentViewersItem:
    """
    Attributes:
        id (int): ID of comment viewer group
        name (str): Name of comment viewer group
        name_translated (str): Translated name of comment viewer group
    """

    id: int
    name: str
    name_translated: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        name_translated = self.name_translated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "nameTranslated": name_translated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        name_translated = d.pop("nameTranslated")

        person_master_data_comment_viewers_item = cls(
            id=id,
            name=name,
            name_translated=name_translated,
        )

        person_master_data_comment_viewers_item.additional_properties = d
        return person_master_data_comment_viewers_item

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
