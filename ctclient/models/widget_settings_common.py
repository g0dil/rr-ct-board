from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_settings_common_density import WidgetSettingsCommonDensity

T = TypeVar("T", bound="WidgetSettingsCommon")


@_attrs_define
class WidgetSettingsCommon:
    """Settings specific to common widgets

    Attributes:
        density (WidgetSettingsCommonDensity): Density options for common widgets
    """

    density: WidgetSettingsCommonDensity
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
        density = WidgetSettingsCommonDensity(d.pop("density"))

        widget_settings_common = cls(
            density=density,
        )

        widget_settings_common.additional_properties = d
        return widget_settings_common

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
