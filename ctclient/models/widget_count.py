from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_count_color import WidgetCountColor
from ..models.widget_count_type import WidgetCountType

T = TypeVar("T", bound="WidgetCount")


@_attrs_define
class WidgetCount:
    """Count display for widgets

    Attributes:
        color (WidgetCountColor): A color in ChurchTools
        text (str):
        type_ (WidgetCountType):
    """

    color: WidgetCountColor
    text: str
    type_: WidgetCountType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.value

        text = self.text

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "text": text,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = WidgetCountColor(d.pop("color"))

        text = d.pop("text")

        type_ = WidgetCountType(d.pop("type"))

        widget_count = cls(
            color=color,
            text=text,
            type_=type_,
        )

        widget_count.additional_properties = d
        return widget_count

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
