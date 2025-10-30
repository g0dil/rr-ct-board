from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkingType0DataType0VideosItemActorsItem")


@_attrs_define
class LinkingType0DataType0VideosItemActorsItem:
    """
    Attributes:
        profile (str | Unset): The URL or an identifier for the actor's profile. Example:
            https://example.com/actor/profile.
        role (str | Unset): The role played by the actor. Example: Main Character.
    """

    profile: str | Unset = UNSET
    role: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile = self.profile

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile is not UNSET:
            field_dict["profile"] = profile
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        profile = d.pop("profile", UNSET)

        role = d.pop("role", UNSET)

        linking_type_0_data_type_0_videos_item_actors_item = cls(
            profile=profile,
            role=role,
        )

        linking_type_0_data_type_0_videos_item_actors_item.additional_properties = d
        return linking_type_0_data_type_0_videos_item_actors_item

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
