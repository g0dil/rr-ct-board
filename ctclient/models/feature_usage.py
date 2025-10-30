from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feature_usage_type import FeatureUsageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FeatureUsage")


@_attrs_define
class FeatureUsage:
    """
    Attributes:
        name (str): Feature, tour or event name.
        type_ (FeatureUsageType):
        delta (float | Unset): Value to decrement the metric by
    """

    name: str
    type_: FeatureUsageType
    delta: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        delta = self.delta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if delta is not UNSET:
            field_dict["delta"] = delta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = FeatureUsageType(d.pop("type"))

        delta = d.pop("delta", UNSET)

        feature_usage = cls(
            name=name,
            type_=type_,
            delta=delta,
        )

        feature_usage.additional_properties = d
        return feature_usage

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
