from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GroupMemberAggregationsAdditionalProperty")


@_attrs_define
class GroupMemberAggregationsAdditionalProperty:
    """
    Attributes:
        average (float):
        max_ (float):
        min_ (float):
        sum_ (float):
    """

    average: float
    max_: float
    min_: float
    sum_: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average = self.average

        max_ = self.max_

        min_ = self.min_

        sum_ = self.sum_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "average": average,
                "max": max_,
                "min": min_,
                "sum": sum_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        average = d.pop("average")

        max_ = d.pop("max")

        min_ = d.pop("min")

        sum_ = d.pop("sum")

        group_member_aggregations_additional_property = cls(
            average=average,
            max_=max_,
            min_=min_,
            sum_=sum_,
        )

        group_member_aggregations_additional_property.additional_properties = d
        return group_member_aggregations_additional_property

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
