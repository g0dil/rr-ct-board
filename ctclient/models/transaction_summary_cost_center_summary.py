from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transaction_summary_cost_center_summary_income import (
        TransactionSummaryCostCenterSummaryIncome,
    )
    from ..models.transaction_summary_cost_center_summary_outcome import (
        TransactionSummaryCostCenterSummaryOutcome,
    )
    from ..models.transaction_summary_cost_center_summary_sum import (
        TransactionSummaryCostCenterSummarySum,
    )


T = TypeVar("T", bound="TransactionSummaryCostCenterSummary")


@_attrs_define
class TransactionSummaryCostCenterSummary:
    """
    Attributes:
        income (TransactionSummaryCostCenterSummaryIncome):
        outcome (TransactionSummaryCostCenterSummaryOutcome):
        sum_ (TransactionSummaryCostCenterSummarySum):
    """

    income: TransactionSummaryCostCenterSummaryIncome
    outcome: TransactionSummaryCostCenterSummaryOutcome
    sum_: TransactionSummaryCostCenterSummarySum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        income = self.income.to_dict()

        outcome = self.outcome.to_dict()

        sum_ = self.sum_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "income": income,
                "outcome": outcome,
                "sum": sum_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_summary_cost_center_summary_income import (
            TransactionSummaryCostCenterSummaryIncome,
        )
        from ..models.transaction_summary_cost_center_summary_outcome import (
            TransactionSummaryCostCenterSummaryOutcome,
        )
        from ..models.transaction_summary_cost_center_summary_sum import (
            TransactionSummaryCostCenterSummarySum,
        )

        d = dict(src_dict)
        income = TransactionSummaryCostCenterSummaryIncome.from_dict(d.pop("income"))

        outcome = TransactionSummaryCostCenterSummaryOutcome.from_dict(d.pop("outcome"))

        sum_ = TransactionSummaryCostCenterSummarySum.from_dict(d.pop("sum"))

        transaction_summary_cost_center_summary = cls(
            income=income,
            outcome=outcome,
            sum_=sum_,
        )

        transaction_summary_cost_center_summary.additional_properties = d
        return transaction_summary_cost_center_summary

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
