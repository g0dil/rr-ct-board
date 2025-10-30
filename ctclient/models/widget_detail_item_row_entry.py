from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_detail_item_row_entry_type import WidgetDetailItemRowEntryType

if TYPE_CHECKING:
    from ..models.widget_detail_item_row_entry_color import (
        WidgetDetailItemRowEntryColor,
    )


T = TypeVar("T", bound="WidgetDetailItemRowEntry")


@_attrs_define
class WidgetDetailItemRowEntry:
    """Entry row type for widget detail items

    Attributes:
        color (WidgetDetailItemRowEntryColor): Value for Tailwind color
        icon (str):
        text (str):
        type_ (WidgetDetailItemRowEntryType):
    """

    color: WidgetDetailItemRowEntryColor
    icon: str
    text: str
    type_: WidgetDetailItemRowEntryType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.to_dict()

        icon = self.icon

        text = self.text

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "icon": icon,
                "text": text,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_detail_item_row_entry_color import (
            WidgetDetailItemRowEntryColor,
        )

        d = dict(src_dict)
        color = WidgetDetailItemRowEntryColor.from_dict(d.pop("color"))

        icon = d.pop("icon")

        text = d.pop("text")

        type_ = WidgetDetailItemRowEntryType(d.pop("type"))

        widget_detail_item_row_entry = cls(
            color=color,
            icon=icon,
            text=text,
            type_=type_,
        )

        widget_detail_item_row_entry.additional_properties = d
        return widget_detail_item_row_entry

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
