from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_tags_domain_type_body_color import PostTagsDomainTypeBodyColor

T = TypeVar("T", bound="PostTagsDomainTypeBody")


@_attrs_define
class PostTagsDomainTypeBody:
    """
    Attributes:
        color (PostTagsDomainTypeBodyColor): A color in ChurchTools
        description (None | str):  Example: Für alles, was mit Mission zu tun hat.
        name (str):  Example: Mission.
    """

    color: PostTagsDomainTypeBodyColor
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
        color = PostTagsDomainTypeBodyColor(d.pop("color"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        name = d.pop("name")

        post_tags_domain_type_body = cls(
            color=color,
            description=description,
            name=name,
        )

        post_tags_domain_type_body.additional_properties = d
        return post_tags_domain_type_body

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
