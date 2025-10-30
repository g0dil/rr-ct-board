from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_color import ActionColor
from ..models.action_key import ActionKey
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_action_meta_data import ActionActionMetaData
    from ..models.action_group_type_0 import ActionGroupType0


T = TypeVar("T", bound="Action")


@_attrs_define
class Action:
    """
    Attributes:
        action_meta_data (ActionActionMetaData):
        domain_type (str):
        group (ActionGroupType0 | None):
        key (ActionKey):
        color (ActionColor | Unset): A color in ChurchTools
        description (str | Unset):
        icon (str | Unset):
        name (str | Unset):
    """

    action_meta_data: ActionActionMetaData
    domain_type: str
    group: ActionGroupType0 | None
    key: ActionKey
    color: ActionColor | Unset = UNSET
    description: str | Unset = UNSET
    icon: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_group_type_0 import ActionGroupType0

        action_meta_data = self.action_meta_data.to_dict()

        domain_type = self.domain_type

        group: dict[str, Any] | None
        if isinstance(self.group, ActionGroupType0):
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
        from ..models.action_action_meta_data import ActionActionMetaData
        from ..models.action_group_type_0 import ActionGroupType0

        d = dict(src_dict)
        action_meta_data = ActionActionMetaData.from_dict(d.pop("actionMetaData"))

        domain_type = d.pop("domainType")

        def _parse_group(data: object) -> ActionGroupType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_0 = ActionGroupType0.from_dict(data)

                return group_type_0
            except:  # noqa: E722
                pass
            return cast(ActionGroupType0 | None, data)

        group = _parse_group(d.pop("group"))

        key = ActionKey(d.pop("key"))

        _color = d.pop("color", UNSET)
        color: ActionColor | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = ActionColor(_color)

        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        name = d.pop("name", UNSET)

        action = cls(
            action_meta_data=action_meta_data,
            domain_type=domain_type,
            group=group,
            key=key,
            color=color,
            description=description,
            icon=icon,
            name=name,
        )

        action.additional_properties = d
        return action

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
