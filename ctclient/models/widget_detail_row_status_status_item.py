from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.widget_detail_row_status_status_item_color import (
        WidgetDetailRowStatusStatusItemColor,
    )


T = TypeVar("T", bound="WidgetDetailRowStatusStatusItem")


@_attrs_define
class WidgetDetailRowStatusStatusItem:
    """
    Attributes:
        color (WidgetDetailRowStatusStatusItemColor): Value for Tailwind color
        icon (str):
        infos (list[str]):
        status (str):
    """

    color: WidgetDetailRowStatusStatusItemColor
    icon: str
    infos: list[str]
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.to_dict()

        icon = self.icon

        infos = self.infos

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "icon": icon,
                "infos": infos,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_detail_row_status_status_item_color import (
            WidgetDetailRowStatusStatusItemColor,
        )

        d = dict(src_dict)
        color = WidgetDetailRowStatusStatusItemColor.from_dict(d.pop("color"))

        icon = d.pop("icon")

        infos = cast(list[str], d.pop("infos"))

        status = d.pop("status")

        widget_detail_row_status_status_item = cls(
            color=color,
            icon=icon,
            infos=infos,
            status=status,
        )

        widget_detail_row_status_status_item.additional_properties = d
        return widget_detail_row_status_status_item

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
