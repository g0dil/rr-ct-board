from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_detail_row_properties_type import WidgetDetailRowPropertiesType

if TYPE_CHECKING:
    from ..models.widget_detail_row_properties_properties_item import (
        WidgetDetailRowPropertiesPropertiesItem,
    )


T = TypeVar("T", bound="WidgetDetailRowProperties")


@_attrs_define
class WidgetDetailRowProperties:
    """Properties row type for widget detail items

    Attributes:
        properties (list[WidgetDetailRowPropertiesPropertiesItem]):
        type_ (WidgetDetailRowPropertiesType):
    """

    properties: list[WidgetDetailRowPropertiesPropertiesItem]
    type_: WidgetDetailRowPropertiesType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        properties = []
        for properties_item_data in self.properties:
            properties_item = properties_item_data.to_dict()
            properties.append(properties_item)

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "properties": properties,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_detail_row_properties_properties_item import (
            WidgetDetailRowPropertiesPropertiesItem,
        )

        d = dict(src_dict)
        properties = []
        _properties = d.pop("properties")
        for properties_item_data in _properties:
            properties_item = WidgetDetailRowPropertiesPropertiesItem.from_dict(
                properties_item_data
            )

            properties.append(properties_item)

        type_ = WidgetDetailRowPropertiesType(d.pop("type"))

        widget_detail_row_properties = cls(
            properties=properties,
            type_=type_,
        )

        widget_detail_row_properties.additional_properties = d
        return widget_detail_row_properties

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
