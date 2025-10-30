from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_info_item_sub_items_item_color import (
    WidgetInfoItemSubItemsItemColor,
)

T = TypeVar("T", bound="WidgetInfoItemSubItemsItem")


@_attrs_define
class WidgetInfoItemSubItemsItem:
    """Sub-item for widget information items

    Attributes:
        color (WidgetInfoItemSubItemsItemColor): A color in ChurchTools
        icon_before (None | str):
        text (str):
    """

    color: WidgetInfoItemSubItemsItemColor
    icon_before: None | str
    text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.value

        icon_before: None | str
        icon_before = self.icon_before

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "iconBefore": icon_before,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = WidgetInfoItemSubItemsItemColor(d.pop("color"))

        def _parse_icon_before(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        icon_before = _parse_icon_before(d.pop("iconBefore"))

        text = d.pop("text")

        widget_info_item_sub_items_item = cls(
            color=color,
            icon_before=icon_before,
            text=text,
        )

        widget_info_item_sub_items_item.additional_properties = d
        return widget_info_item_sub_items_item

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
