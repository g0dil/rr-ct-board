from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_object_song_color_key import DomainObjectSongColorKey
from ..models.domain_object_song_color_shade import DomainObjectSongColorShade

T = TypeVar("T", bound="DomainObjectSongColor")


@_attrs_define
class DomainObjectSongColor:
    """Value for Tailwind color

    Attributes:
        key (DomainObjectSongColorKey): A color in ChurchTools
        shade (DomainObjectSongColorShade):  Example: 500.
    """

    key: DomainObjectSongColorKey
    shade: DomainObjectSongColorShade
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key.value

        shade = self.shade.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "shade": shade,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = DomainObjectSongColorKey(d.pop("key"))

        shade = DomainObjectSongColorShade(d.pop("shade"))

        domain_object_song_color = cls(
            key=key,
            shade=shade,
        )

        domain_object_song_color.additional_properties = d
        return domain_object_song_color

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
