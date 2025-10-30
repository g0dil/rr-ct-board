from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_tags_tag_id_body_color import PutTagsTagIdBodyColor

T = TypeVar("T", bound="PutTagsTagIdBody")


@_attrs_define
class PutTagsTagIdBody:
    """
    Attributes:
        color (PutTagsTagIdBodyColor): A color in ChurchTools
        description (None | str):  Example: Für alles, was mit Mission zu tun hat.
        name (str):  Example: Mission.
    """

    color: PutTagsTagIdBodyColor
    description: None | str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.value

        description: None | str
        description = self.description

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "description": description,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = PutTagsTagIdBodyColor(d.pop("color"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        name = d.pop("name")

        put_tags_tag_id_body = cls(
            color=color,
            description=description,
            name=name,
        )

        put_tags_tag_id_body.additional_properties = d
        return put_tags_tag_id_body

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
