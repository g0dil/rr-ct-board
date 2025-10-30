from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WidgetDetailRowPropertiesPropertiesItem")


@_attrs_define
class WidgetDetailRowPropertiesPropertiesItem:
    """
    Attributes:
        label (str):
        property_ (list[str]):
    """

    label: str
    property_: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        property_ = self.property_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "property": property_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        property_ = cast(list[str], d.pop("property"))

        widget_detail_row_properties_properties_item = cls(
            label=label,
            property_=property_,
        )

        widget_detail_row_properties_properties_item.additional_properties = d
        return widget_detail_row_properties_properties_item

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
