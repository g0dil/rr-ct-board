from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_date_widget_action_flavor import WidgetDateWidgetActionFlavor
from ..models.widget_date_widget_action_key import WidgetDateWidgetActionKey
from ..models.widget_date_widget_action_type import WidgetDateWidgetActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget_date_widget_action_props import WidgetDateWidgetActionProps


T = TypeVar("T", bound="WidgetDateWidgetAction")


@_attrs_define
class WidgetDateWidgetAction:
    """
    Attributes:
        key (WidgetDateWidgetActionKey):
        label (str):
        type_ (WidgetDateWidgetActionType): Type of widget action Example: primary.
        flavor (WidgetDateWidgetActionFlavor | Unset): Flavor of widget action Example: basic.
        icon (str | Unset):
        props (WidgetDateWidgetActionProps | Unset):
    """

    key: WidgetDateWidgetActionKey
    label: str
    type_: WidgetDateWidgetActionType
    flavor: WidgetDateWidgetActionFlavor | Unset = UNSET
    icon: str | Unset = UNSET
    props: WidgetDateWidgetActionProps | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key.value

        label = self.label

        type_ = self.type_.value

        flavor: str | Unset = UNSET
        if not isinstance(self.flavor, Unset):
            flavor = self.flavor.value

        icon = self.icon

        props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props, Unset):
            props = self.props.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "type": type_,
            }
        )
        if flavor is not UNSET:
            field_dict["flavor"] = flavor
        if icon is not UNSET:
            field_dict["icon"] = icon
        if props is not UNSET:
            field_dict["props"] = props

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_date_widget_action_props import WidgetDateWidgetActionProps

        d = dict(src_dict)
        key = WidgetDateWidgetActionKey(d.pop("key"))

        label = d.pop("label")

        type_ = WidgetDateWidgetActionType(d.pop("type"))

        _flavor = d.pop("flavor", UNSET)
        flavor: WidgetDateWidgetActionFlavor | Unset
        if isinstance(_flavor, Unset):
            flavor = UNSET
        else:
            flavor = WidgetDateWidgetActionFlavor(_flavor)

        icon = d.pop("icon", UNSET)

        _props = d.pop("props", UNSET)
        props: WidgetDateWidgetActionProps | Unset
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = WidgetDateWidgetActionProps.from_dict(_props)

        widget_date_widget_action = cls(
            key=key,
            label=label,
            type_=type_,
            flavor=flavor,
            icon=icon,
            props=props,
        )

        widget_date_widget_action.additional_properties = d
        return widget_date_widget_action

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
