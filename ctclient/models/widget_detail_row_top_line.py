from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_detail_row_top_line_type import WidgetDetailRowTopLineType

if TYPE_CHECKING:
    from ..models.widget_detail_row_top_line_color import WidgetDetailRowTopLineColor


T = TypeVar("T", bound="WidgetDetailRowTopLine")


@_attrs_define
class WidgetDetailRowTopLine:
    """Top line row type for widget detail items

    Attributes:
        color (WidgetDetailRowTopLineColor): Value for Tailwind color
        infos (list[str]):
        type_ (WidgetDetailRowTopLineType):
    """

    color: WidgetDetailRowTopLineColor
    infos: list[str]
    type_: WidgetDetailRowTopLineType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.to_dict()

        infos = self.infos

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "infos": infos,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_detail_row_top_line_color import (
            WidgetDetailRowTopLineColor,
        )

        d = dict(src_dict)
        color = WidgetDetailRowTopLineColor.from_dict(d.pop("color"))

        infos = cast(list[str], d.pop("infos"))

        type_ = WidgetDetailRowTopLineType(d.pop("type"))

        widget_detail_row_top_line = cls(
            color=color,
            infos=infos,
            type_=type_,
        )

        widget_detail_row_top_line.additional_properties = d
        return widget_detail_row_top_line

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
