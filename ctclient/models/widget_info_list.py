from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_info_list_direction import WidgetInfoListDirection
from ..models.widget_info_list_size import WidgetInfoListSize

if TYPE_CHECKING:
    from ..models.widget_info_list_info_items_item import WidgetInfoListInfoItemsItem


T = TypeVar("T", bound="WidgetInfoList")


@_attrs_define
class WidgetInfoList:
    """List of information items for widgets

    Attributes:
        direction (WidgetInfoListDirection): Direction for widget info lists
        info_items (list[WidgetInfoListInfoItemsItem]):
        size (WidgetInfoListSize): Size options for widget info lists
        with_label (bool):
    """

    direction: WidgetInfoListDirection
    info_items: list[WidgetInfoListInfoItemsItem]
    size: WidgetInfoListSize
    with_label: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direction = self.direction.value

        info_items = []
        for info_items_item_data in self.info_items:
            info_items_item = info_items_item_data.to_dict()
            info_items.append(info_items_item)

        size = self.size.value

        with_label = self.with_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "direction": direction,
                "infoItems": info_items,
                "size": size,
                "withLabel": with_label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_info_list_info_items_item import (
            WidgetInfoListInfoItemsItem,
        )

        d = dict(src_dict)
        direction = WidgetInfoListDirection(d.pop("direction"))

        info_items = []
        _info_items = d.pop("infoItems")
        for info_items_item_data in _info_items:
            info_items_item = WidgetInfoListInfoItemsItem.from_dict(
                info_items_item_data
            )

            info_items.append(info_items_item)

        size = WidgetInfoListSize(d.pop("size"))

        with_label = d.pop("withLabel")

        widget_info_list = cls(
            direction=direction,
            info_items=info_items,
            size=size,
            with_label=with_label,
        )

        widget_info_list.additional_properties = d
        return widget_info_list

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
