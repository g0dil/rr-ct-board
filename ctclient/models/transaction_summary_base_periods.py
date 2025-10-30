from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transaction_summary_base_periods_end_date import (
        TransactionSummaryBasePeriodsEndDate,
    )
    from ..models.transaction_summary_base_periods_start_date import (
        TransactionSummaryBasePeriodsStartDate,
    )


T = TypeVar("T", bound="TransactionSummaryBasePeriods")


@_attrs_define
class TransactionSummaryBasePeriods:
    """
    Attributes:
        end_date (TransactionSummaryBasePeriodsEndDate):
        start_date (TransactionSummaryBasePeriodsStartDate):
    """

    end_date: TransactionSummaryBasePeriodsEndDate
    start_date: TransactionSummaryBasePeriodsStartDate
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date.to_dict()

        start_date = self.start_date.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endDate": end_date,
                "startDate": start_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_summary_base_periods_end_date import (
            TransactionSummaryBasePeriodsEndDate,
        )
        from ..models.transaction_summary_base_periods_start_date import (
            TransactionSummaryBasePeriodsStartDate,
        )

        d = dict(src_dict)
        end_date = TransactionSummaryBasePeriodsEndDate.from_dict(d.pop("endDate"))

        start_date = TransactionSummaryBasePeriodsStartDate.from_dict(
            d.pop("startDate")
        )

        transaction_summary_base_periods = cls(
            end_date=end_date,
            start_date=start_date,
        )

        transaction_summary_base_periods.additional_properties = d
        return transaction_summary_base_periods

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
