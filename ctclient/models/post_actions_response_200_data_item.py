from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_actions_response_200_data_item_color import (
    PostActionsResponse200DataItemColor,
)
from ..models.post_actions_response_200_data_item_key import (
    PostActionsResponse200DataItemKey,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_actions_response_200_data_item_action_meta_data import (
        PostActionsResponse200DataItemActionMetaData,
    )
    from ..models.post_actions_response_200_data_item_group_type_0 import (
        PostActionsResponse200DataItemGroupType0,
    )


T = TypeVar("T", bound="PostActionsResponse200DataItem")


@_attrs_define
class PostActionsResponse200DataItem:
    """
    Attributes:
        action_meta_data (PostActionsResponse200DataItemActionMetaData):
        domain_type (str):
        group (None | PostActionsResponse200DataItemGroupType0):
        key (PostActionsResponse200DataItemKey):
        color (PostActionsResponse200DataItemColor | Unset): A color in ChurchTools
        description (str | Unset):
        icon (str | Unset):
        name (str | Unset):
    """

    action_meta_data: PostActionsResponse200DataItemActionMetaData
    domain_type: str
    group: None | PostActionsResponse200DataItemGroupType0
    key: PostActionsResponse200DataItemKey
    color: PostActionsResponse200DataItemColor | Unset = UNSET
    description: str | Unset = UNSET
    icon: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_actions_response_200_data_item_group_type_0 import (
            PostActionsResponse200DataItemGroupType0,
        )

        action_meta_data = self.action_meta_data.to_dict()

        domain_type = self.domain_type

        group: dict[str, Any] | None
        if isinstance(self.group, PostActionsResponse200DataItemGroupType0):
            group = self.group.to_dict()
        else:
            group = self.group

        key = self.key.value

        color: str | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        description = self.description

        icon = self.icon

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionMetaData": action_meta_data,
                "domainType": domain_type,
                "group": group,
                "key": key,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_actions_response_200_data_item_action_meta_data import (
            PostActionsResponse200DataItemActionMetaData,
        )
        from ..models.post_actions_response_200_data_item_group_type_0 import (
            PostActionsResponse200DataItemGroupType0,
        )

        d = dict(src_dict)
        action_meta_data = PostActionsResponse200DataItemActionMetaData.from_dict(
            d.pop("actionMetaData")
        )

        domain_type = d.pop("domainType")

        def _parse_group(
            data: object,
        ) -> None | PostActionsResponse200DataItemGroupType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_0 = PostActionsResponse200DataItemGroupType0.from_dict(data)

                return group_type_0
            except:  # noqa: E722
                pass
            return cast(None | PostActionsResponse200DataItemGroupType0, data)

        group = _parse_group(d.pop("group"))

        key = PostActionsResponse200DataItemKey(d.pop("key"))

        _color = d.pop("color", UNSET)
        color: PostActionsResponse200DataItemColor | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = PostActionsResponse200DataItemColor(_color)

        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        name = d.pop("name", UNSET)

        post_actions_response_200_data_item = cls(
            action_meta_data=action_meta_data,
            domain_type=domain_type,
            group=group,
            key=key,
            color=color,
            description=description,
            icon=icon,
            name=name,
        )

        post_actions_response_200_data_item.additional_properties = d
        return post_actions_response_200_data_item

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
