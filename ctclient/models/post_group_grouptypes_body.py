from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_group_grouptypes_body_color import PostGroupGrouptypesBodyColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostGroupGrouptypesBody")


@_attrs_define
class PostGroupGrouptypesBody:
    """
    Attributes:
        available_for_new_person (bool):
        color (PostGroupGrouptypesBodyColor): A color in ChurchTools
        is_leader_necessary (bool):
        name (str):  Example: Kleingruppe.
        name_plural (str):  Example: Kleingruppen.
        permission_depth (int):
        posts_enabled (bool):  Example: True.
        shorty (str):  Example: KG.
        sort_key (int):  Example: 2.
        description (str | Unset):
    """

    available_for_new_person: bool
    color: PostGroupGrouptypesBodyColor
    is_leader_necessary: bool
    name: str
    name_plural: str
    permission_depth: int
    posts_enabled: bool
    shorty: str
    sort_key: int
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_for_new_person = self.available_for_new_person

        color = self.color.value

        is_leader_necessary = self.is_leader_necessary

        name = self.name

        name_plural = self.name_plural

        permission_depth = self.permission_depth

        posts_enabled = self.posts_enabled

        shorty = self.shorty

        sort_key = self.sort_key

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availableForNewPerson": available_for_new_person,
                "color": color,
                "isLeaderNecessary": is_leader_necessary,
                "name": name,
                "namePlural": name_plural,
                "permissionDepth": permission_depth,
                "postsEnabled": posts_enabled,
                "shorty": shorty,
                "sortKey": sort_key,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_for_new_person = d.pop("availableForNewPerson")

        color = PostGroupGrouptypesBodyColor(d.pop("color"))

        is_leader_necessary = d.pop("isLeaderNecessary")

        name = d.pop("name")

        name_plural = d.pop("namePlural")

        permission_depth = d.pop("permissionDepth")

        posts_enabled = d.pop("postsEnabled")

        shorty = d.pop("shorty")

        sort_key = d.pop("sortKey")

        description = d.pop("description", UNSET)

        post_group_grouptypes_body = cls(
            available_for_new_person=available_for_new_person,
            color=color,
            is_leader_necessary=is_leader_necessary,
            name=name,
            name_plural=name_plural,
            permission_depth=permission_depth,
            posts_enabled=posts_enabled,
            shorty=shorty,
            sort_key=sort_key,
            description=description,
        )

        post_group_grouptypes_body.additional_properties = d
        return post_group_grouptypes_body

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
