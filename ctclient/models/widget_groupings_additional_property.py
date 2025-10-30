from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WidgetGroupingsAdditionalProperty")


@_attrs_define
class WidgetGroupingsAdditionalProperty:
    """Individual grouping option configuration

    Attributes:
        key (str): Unique key for the grouping option
        label (str): Display label for the grouping option
        sort_key (int | Unset): Sort order for the grouping option
    """

    key: str
    label: str
    sort_key: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
            }
        )
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        sort_key = d.pop("sortKey", UNSET)

        widget_groupings_additional_property = cls(
            key=key,
            label=label,
            sort_key=sort_key,
        )

        widget_groupings_additional_property.additional_properties = d
        return widget_groupings_additional_property

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
