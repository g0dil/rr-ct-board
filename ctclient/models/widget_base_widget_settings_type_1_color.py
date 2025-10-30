from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_base_widget_settings_type_1_color_key import (
    WidgetBaseWidgetSettingsType1ColorKey,
)
from ..models.widget_base_widget_settings_type_1_color_shade import (
    WidgetBaseWidgetSettingsType1ColorShade,
)

T = TypeVar("T", bound="WidgetBaseWidgetSettingsType1Color")


@_attrs_define
class WidgetBaseWidgetSettingsType1Color:
    """Value for Tailwind color

    Attributes:
        key (WidgetBaseWidgetSettingsType1ColorKey): A color in ChurchTools
        shade (WidgetBaseWidgetSettingsType1ColorShade):  Example: 500.
    """

    key: WidgetBaseWidgetSettingsType1ColorKey
    shade: WidgetBaseWidgetSettingsType1ColorShade
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key.value

        shade = self.shade.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "shade": shade,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = WidgetBaseWidgetSettingsType1ColorKey(d.pop("key"))

        shade = WidgetBaseWidgetSettingsType1ColorShade(d.pop("shade"))

        widget_base_widget_settings_type_1_color = cls(
            key=key,
            shade=shade,
        )

        widget_base_widget_settings_type_1_color.additional_properties = d
        return widget_base_widget_settings_type_1_color

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
