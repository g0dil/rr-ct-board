from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_post_summary_options_filter import (
    SubscriptionPostSummaryOptionsFilter,
)

T = TypeVar("T", bound="SubscriptionPostSummaryOptions")


@_attrs_define
class SubscriptionPostSummaryOptions:
    """
    Attributes:
        filter_ (SubscriptionPostSummaryOptionsFilter):
        weekdays (list[int]):
    """

    filter_: SubscriptionPostSummaryOptionsFilter
    weekdays: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_.value

        weekdays = self.weekdays

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter": filter_,
                "weekdays": weekdays,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_ = SubscriptionPostSummaryOptionsFilter(d.pop("filter"))

        weekdays = cast(list[int], d.pop("weekdays"))

        subscription_post_summary_options = cls(
            filter_=filter_,
            weekdays=weekdays,
        )

        subscription_post_summary_options.additional_properties = d
        return subscription_post_summary_options

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
