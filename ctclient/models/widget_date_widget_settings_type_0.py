from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_date_widget_settings_type_0_density import (
    WidgetDateWidgetSettingsType0Density,
)

T = TypeVar("T", bound="WidgetDateWidgetSettingsType0")


@_attrs_define
class WidgetDateWidgetSettingsType0:
    """Settings specific to common widgets

    Attributes:
        density (WidgetDateWidgetSettingsType0Density): Density options for common widgets
    """

    density: WidgetDateWidgetSettingsType0Density
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        density = self.density.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "density": density,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        density = WidgetDateWidgetSettingsType0Density(d.pop("density"))

        widget_date_widget_settings_type_0 = cls(
            density=density,
        )

        widget_date_widget_settings_type_0.additional_properties = d
        return widget_date_widget_settings_type_0

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
