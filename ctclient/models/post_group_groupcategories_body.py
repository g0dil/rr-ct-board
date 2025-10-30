from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_group_groupcategories_body_color import (
    PostGroupGroupcategoriesBodyColor,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostGroupGroupcategoriesBody")


@_attrs_define
class PostGroupGroupcategoriesBody:
    """
    Attributes:
        color (PostGroupGroupcategoriesBodyColor): A color in ChurchTools
        name (str):  Example: Gottesdienst.
        sort_key (int):  Example: 5.
        description (None | str | Unset):  Example: Wir feiern Gottesdienst!.
    """

    color: PostGroupGroupcategoriesBodyColor
    name: str
    sort_key: int
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.value

        name = self.name

        sort_key = self.sort_key

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "name": name,
                "sortKey": sort_key,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = PostGroupGroupcategoriesBodyColor(d.pop("color"))

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        post_group_groupcategories_body = cls(
            color=color,
            name=name,
            sort_key=sort_key,
            description=description,
        )

        post_group_groupcategories_body.additional_properties = d
        return post_group_groupcategories_body

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
