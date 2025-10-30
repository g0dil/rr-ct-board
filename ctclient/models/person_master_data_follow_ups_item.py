from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonMasterDataFollowUpsItem")


@_attrs_define
class PersonMasterDataFollowUpsItem:
    """
    Attributes:
        id (int):  Example: 1.
        name (str):  Example: Integration Kontaktkarte.
        name_translated (str):  Example: Integration Kontaktkarte.
        comment_viewer_id (int | Unset):
    """

    id: int
    name: str
    name_translated: str
    comment_viewer_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        name_translated = self.name_translated

        comment_viewer_id = self.comment_viewer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "nameTranslated": name_translated,
            }
        )
        if comment_viewer_id is not UNSET:
            field_dict["commentViewerId"] = comment_viewer_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        name_translated = d.pop("nameTranslated")

        comment_viewer_id = d.pop("commentViewerId", UNSET)

        person_master_data_follow_ups_item = cls(
            id=id,
            name=name,
            name_translated=name_translated,
            comment_viewer_id=comment_viewer_id,
        )

        person_master_data_follow_ups_item.additional_properties = d
        return person_master_data_follow_ups_item

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
