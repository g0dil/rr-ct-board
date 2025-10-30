from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transaction_summary_credit_debit_summary_accounts_item import (
        TransactionSummaryCreditDebitSummaryAccountsItem,
    )
    from ..models.transaction_summary_credit_debit_summary_credit import (
        TransactionSummaryCreditDebitSummaryCredit,
    )
    from ..models.transaction_summary_credit_debit_summary_debit import (
        TransactionSummaryCreditDebitSummaryDebit,
    )
    from ..models.transaction_summary_credit_debit_summary_sum import (
        TransactionSummaryCreditDebitSummarySum,
    )


T = TypeVar("T", bound="TransactionSummaryCreditDebitSummary")


@_attrs_define
class TransactionSummaryCreditDebitSummary:
    """
    Attributes:
        accounts (list[TransactionSummaryCreditDebitSummaryAccountsItem]):
        credit (TransactionSummaryCreditDebitSummaryCredit):
        debit (TransactionSummaryCreditDebitSummaryDebit):
        sum_ (TransactionSummaryCreditDebitSummarySum):
    """

    accounts: list[TransactionSummaryCreditDebitSummaryAccountsItem]
    credit: TransactionSummaryCreditDebitSummaryCredit
    debit: TransactionSummaryCreditDebitSummaryDebit
    sum_: TransactionSummaryCreditDebitSummarySum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()
            accounts.append(accounts_item)

        credit = self.credit.to_dict()

        debit = self.debit.to_dict()

        sum_ = self.sum_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts": accounts,
                "credit": credit,
                "debit": debit,
                "sum": sum_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_summary_credit_debit_summary_accounts_item import (
            TransactionSummaryCreditDebitSummaryAccountsItem,
        )
        from ..models.transaction_summary_credit_debit_summary_credit import (
            TransactionSummaryCreditDebitSummaryCredit,
        )
        from ..models.transaction_summary_credit_debit_summary_debit import (
            TransactionSummaryCreditDebitSummaryDebit,
        )
        from ..models.transaction_summary_credit_debit_summary_sum import (
            TransactionSummaryCreditDebitSummarySum,
        )

        d = dict(src_dict)
        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = TransactionSummaryCreditDebitSummaryAccountsItem.from_dict(
                accounts_item_data
            )

            accounts.append(accounts_item)

        credit = TransactionSummaryCreditDebitSummaryCredit.from_dict(d.pop("credit"))

        debit = TransactionSummaryCreditDebitSummaryDebit.from_dict(d.pop("debit"))

        sum_ = TransactionSummaryCreditDebitSummarySum.from_dict(d.pop("sum"))

        transaction_summary_credit_debit_summary = cls(
            accounts=accounts,
            credit=credit,
            debit=debit,
            sum_=sum_,
        )

        transaction_summary_credit_debit_summary.additional_properties = d
        return transaction_summary_credit_debit_summary

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
