from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tag_base_color import TagBaseColor

T = TypeVar("T", bound="TagBase")


@_attrs_define
class TagBase:
    """
    Attributes:
        color (TagBaseColor): A color in ChurchTools
        description (str):
        id (int):
        name (str):
    """

    color: TagBaseColor
    description: str
    id: int
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.value

        description = self.description

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "description": description,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = TagBaseColor(d.pop("color"))

        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        tag_base = cls(
            color=color,
            description=description,
            id=id,
            name=name,
        )

        tag_base.additional_properties = d
        return tag_base

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
