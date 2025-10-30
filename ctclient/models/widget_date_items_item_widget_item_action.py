from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_date_items_item_widget_item_action_flavor import (
    WidgetDateItemsItemWidgetItemActionFlavor,
)
from ..models.widget_date_items_item_widget_item_action_key import (
    WidgetDateItemsItemWidgetItemActionKey,
)
from ..models.widget_date_items_item_widget_item_action_type import (
    WidgetDateItemsItemWidgetItemActionType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget_date_items_item_widget_item_action_props import (
        WidgetDateItemsItemWidgetItemActionProps,
    )


T = TypeVar("T", bound="WidgetDateItemsItemWidgetItemAction")


@_attrs_define
class WidgetDateItemsItemWidgetItemAction:
    """
    Attributes:
        key (WidgetDateItemsItemWidgetItemActionKey):
        label (str):
        type_ (WidgetDateItemsItemWidgetItemActionType): Type of widget action Example: primary.
        flavor (WidgetDateItemsItemWidgetItemActionFlavor | Unset): Flavor of widget action Example: basic.
        icon (str | Unset):
        props (WidgetDateItemsItemWidgetItemActionProps | Unset):
    """

    key: WidgetDateItemsItemWidgetItemActionKey
    label: str
    type_: WidgetDateItemsItemWidgetItemActionType
    flavor: WidgetDateItemsItemWidgetItemActionFlavor | Unset = UNSET
    icon: str | Unset = UNSET
    props: WidgetDateItemsItemWidgetItemActionProps | Unset = UNSET
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
        from ..models.widget_date_items_item_widget_item_action_props import (
            WidgetDateItemsItemWidgetItemActionProps,
        )

        d = dict(src_dict)
        key = WidgetDateItemsItemWidgetItemActionKey(d.pop("key"))

        label = d.pop("label")

        type_ = WidgetDateItemsItemWidgetItemActionType(d.pop("type"))

        _flavor = d.pop("flavor", UNSET)
        flavor: WidgetDateItemsItemWidgetItemActionFlavor | Unset
        if isinstance(_flavor, Unset):
            flavor = UNSET
        else:
            flavor = WidgetDateItemsItemWidgetItemActionFlavor(_flavor)

        icon = d.pop("icon", UNSET)

        _props = d.pop("props", UNSET)
        props: WidgetDateItemsItemWidgetItemActionProps | Unset
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = WidgetDateItemsItemWidgetItemActionProps.from_dict(_props)

        widget_date_items_item_widget_item_action = cls(
            key=key,
            label=label,
            type_=type_,
            flavor=flavor,
            icon=icon,
            props=props,
        )

        widget_date_items_item_widget_item_action.additional_properties = d
        return widget_date_items_item_widget_item_action

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
