from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tag_with_count_color import TagWithCountColor

T = TypeVar("T", bound="TagWithCount")


@_attrs_define
class TagWithCount:
    """
    Attributes:
        count (int):
        color (TagWithCountColor): A color in ChurchTools
        description (str):
        id (int):
        name (str):
    """

    count: int
    color: TagWithCountColor
    description: str
    id: int
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        color = self.color.value

        description = self.description

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
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
        count = d.pop("count")

        color = TagWithCountColor(d.pop("color"))

        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        tag_with_count = cls(
            count=count,
            color=color,
            description=description,
            id=id,
            name=name,
        )

        tag_with_count.additional_properties = d
        return tag_with_count

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
