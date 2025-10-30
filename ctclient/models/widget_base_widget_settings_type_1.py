from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget_base_widget_settings_type_1_color import (
        WidgetBaseWidgetSettingsType1Color,
    )


T = TypeVar("T", bound="WidgetBaseWidgetSettingsType1")


@_attrs_define
class WidgetBaseWidgetSettingsType1:
    """
    Attributes:
        background_color (WidgetBaseWidgetSettingsType1Color | Unset): Value for Tailwind color
    """

    background_color: WidgetBaseWidgetSettingsType1Color | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        background_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_color, Unset):
            background_color = self.background_color.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_base_widget_settings_type_1_color import (
            WidgetBaseWidgetSettingsType1Color,
        )

        d = dict(src_dict)
        _background_color = d.pop("backgroundColor", UNSET)
        background_color: WidgetBaseWidgetSettingsType1Color | Unset
        if isinstance(_background_color, Unset):
            background_color = UNSET
        else:
            background_color = WidgetBaseWidgetSettingsType1Color.from_dict(
                _background_color
            )

        widget_base_widget_settings_type_1 = cls(
            background_color=background_color,
        )

        widget_base_widget_settings_type_1.additional_properties = d
        return widget_base_widget_settings_type_1

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
