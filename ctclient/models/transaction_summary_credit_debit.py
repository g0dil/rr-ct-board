from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transaction_summary_credit_debit_type import (
    TransactionSummaryCreditDebitType,
)

if TYPE_CHECKING:
    from ..models.transaction_summary_credit_debit_periods import (
        TransactionSummaryCreditDebitPeriods,
    )
    from ..models.transaction_summary_credit_debit_summary import (
        TransactionSummaryCreditDebitSummary,
    )


T = TypeVar("T", bound="TransactionSummaryCreditDebit")


@_attrs_define
class TransactionSummaryCreditDebit:
    """
    Attributes:
        periods (TransactionSummaryCreditDebitPeriods):
        summary (TransactionSummaryCreditDebitSummary):
        type_ (TransactionSummaryCreditDebitType):
    """

    periods: TransactionSummaryCreditDebitPeriods
    summary: TransactionSummaryCreditDebitSummary
    type_: TransactionSummaryCreditDebitType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        periods = self.periods.to_dict()

        summary = self.summary.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "periods": periods,
                "summary": summary,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_summary_credit_debit_periods import (
            TransactionSummaryCreditDebitPeriods,
        )
        from ..models.transaction_summary_credit_debit_summary import (
            TransactionSummaryCreditDebitSummary,
        )

        d = dict(src_dict)
        periods = TransactionSummaryCreditDebitPeriods.from_dict(d.pop("periods"))

        summary = TransactionSummaryCreditDebitSummary.from_dict(d.pop("summary"))

        type_ = TransactionSummaryCreditDebitType(d.pop("type"))

        transaction_summary_credit_debit = cls(
            periods=periods,
            summary=summary,
            type_=type_,
        )

        transaction_summary_credit_debit.additional_properties = d
        return transaction_summary_credit_debit

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
