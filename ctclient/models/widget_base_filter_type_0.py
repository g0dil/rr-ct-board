from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget_base_filter_type_0_options_item import (
        WidgetBaseFilterType0OptionsItem,
    )


T = TypeVar("T", bound="WidgetBaseFilterType0")


@_attrs_define
class WidgetBaseFilterType0:
    """
    Attributes:
        options (list[WidgetBaseFilterType0OptionsItem] | Unset):
    """

    options: list[WidgetBaseFilterType0OptionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_base_filter_type_0_options_item import (
            WidgetBaseFilterType0OptionsItem,
        )

        d = dict(src_dict)
        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = WidgetBaseFilterType0OptionsItem.from_dict(options_item_data)

            options.append(options_item)

        widget_base_filter_type_0 = cls(
            options=options,
        )

        widget_base_filter_type_0.additional_properties = d
        return widget_base_filter_type_0

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
