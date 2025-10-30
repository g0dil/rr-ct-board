from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_actions_response_200_data_item_action_meta_data_color import (
    PostActionsResponse200DataItemActionMetaDataColor,
)

T = TypeVar("T", bound="PostActionsResponse200DataItemActionMetaData")


@_attrs_define
class PostActionsResponse200DataItemActionMetaData:
    """
    Attributes:
        color (PostActionsResponse200DataItemActionMetaDataColor): A color in ChurchTools
        description (str):
        icon (str):
        name (str):
    """

    color: PostActionsResponse200DataItemActionMetaDataColor
    description: str
    icon: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.value

        description = self.description

        icon = self.icon

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "description": description,
                "icon": icon,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = PostActionsResponse200DataItemActionMetaDataColor(d.pop("color"))

        description = d.pop("description")

        icon = d.pop("icon")

        name = d.pop("name")

        post_actions_response_200_data_item_action_meta_data = cls(
            color=color,
            description=description,
            icon=icon,
            name=name,
        )

        post_actions_response_200_data_item_action_meta_data.additional_properties = d
        return post_actions_response_200_data_item_action_meta_data

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
