from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_info_list_info_items_item_color import (
    WidgetInfoListInfoItemsItemColor,
)

if TYPE_CHECKING:
    from ..models.widget_info_list_info_items_item_sub_items_item import (
        WidgetInfoListInfoItemsItemSubItemsItem,
    )


T = TypeVar("T", bound="WidgetInfoListInfoItemsItem")


@_attrs_define
class WidgetInfoListInfoItemsItem:
    """Information item for widget lists

    Attributes:
        color (WidgetInfoListInfoItemsItemColor): A color in ChurchTools
        icon_before (None | str):
        label (None | str):
        sub_items (list[WidgetInfoListInfoItemsItemSubItemsItem]):
        text (str):
    """

    color: WidgetInfoListInfoItemsItemColor
    icon_before: None | str
    label: None | str
    sub_items: list[WidgetInfoListInfoItemsItemSubItemsItem]
    text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.value

        icon_before: None | str
        icon_before = self.icon_before

        label: None | str
        label = self.label

        sub_items = []
        for sub_items_item_data in self.sub_items:
            sub_items_item = sub_items_item_data.to_dict()
            sub_items.append(sub_items_item)

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "iconBefore": icon_before,
                "label": label,
                "subItems": sub_items,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_info_list_info_items_item_sub_items_item import (
            WidgetInfoListInfoItemsItemSubItemsItem,
        )

        d = dict(src_dict)
        color = WidgetInfoListInfoItemsItemColor(d.pop("color"))

        def _parse_icon_before(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        icon_before = _parse_icon_before(d.pop("iconBefore"))

        def _parse_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label = _parse_label(d.pop("label"))

        sub_items = []
        _sub_items = d.pop("subItems")
        for sub_items_item_data in _sub_items:
            sub_items_item = WidgetInfoListInfoItemsItemSubItemsItem.from_dict(
                sub_items_item_data
            )

            sub_items.append(sub_items_item)

        text = d.pop("text")

        widget_info_list_info_items_item = cls(
            color=color,
            icon_before=icon_before,
            label=label,
            sub_items=sub_items,
            text=text,
        )

        widget_info_list_info_items_item.additional_properties = d
        return widget_info_list_info_items_item

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
