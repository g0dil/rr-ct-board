from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TransactionSummaryCostCenterSummarySum")


@_attrs_define
class TransactionSummaryCostCenterSummarySum:
    """
    Attributes:
        last_year (int):
        this_year (int):
    """

    last_year: int
    this_year: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_year = self.last_year

        this_year = self.this_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastYear": last_year,
                "thisYear": this_year,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_year = d.pop("lastYear")

        this_year = d.pop("thisYear")

        transaction_summary_cost_center_summary_sum = cls(
            last_year=last_year,
            this_year=this_year,
        )

        transaction_summary_cost_center_summary_sum.additional_properties = d
        return transaction_summary_cost_center_summary_sum

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
