from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transaction_summary_credit_debit_summary_accounts_item_balance import (
        TransactionSummaryCreditDebitSummaryAccountsItemBalance,
    )
    from ..models.transaction_summary_credit_debit_summary_accounts_item_credit import (
        TransactionSummaryCreditDebitSummaryAccountsItemCredit,
    )
    from ..models.transaction_summary_credit_debit_summary_accounts_item_debit import (
        TransactionSummaryCreditDebitSummaryAccountsItemDebit,
    )


T = TypeVar("T", bound="TransactionSummaryCreditDebitSummaryAccountsItem")


@_attrs_define
class TransactionSummaryCreditDebitSummaryAccountsItem:
    """
    Attributes:
        balance (TransactionSummaryCreditDebitSummaryAccountsItemBalance):
        credit (TransactionSummaryCreditDebitSummaryAccountsItemCredit):
        debit (TransactionSummaryCreditDebitSummaryAccountsItemDebit):
        id (int):
        name (str):
        number (str):
    """

    balance: TransactionSummaryCreditDebitSummaryAccountsItemBalance
    credit: TransactionSummaryCreditDebitSummaryAccountsItemCredit
    debit: TransactionSummaryCreditDebitSummaryAccountsItemDebit
    id: int
    name: str
    number: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance = self.balance.to_dict()

        credit = self.credit.to_dict()

        debit = self.debit.to_dict()

        id = self.id

        name = self.name

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balance": balance,
                "credit": credit,
                "debit": debit,
                "id": id,
                "name": name,
                "number": number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_summary_credit_debit_summary_accounts_item_balance import (
            TransactionSummaryCreditDebitSummaryAccountsItemBalance,
        )
        from ..models.transaction_summary_credit_debit_summary_accounts_item_credit import (
            TransactionSummaryCreditDebitSummaryAccountsItemCredit,
        )
        from ..models.transaction_summary_credit_debit_summary_accounts_item_debit import (
            TransactionSummaryCreditDebitSummaryAccountsItemDebit,
        )

        d = dict(src_dict)
        balance = TransactionSummaryCreditDebitSummaryAccountsItemBalance.from_dict(
            d.pop("balance")
        )

        credit = TransactionSummaryCreditDebitSummaryAccountsItemCredit.from_dict(
            d.pop("credit")
        )

        debit = TransactionSummaryCreditDebitSummaryAccountsItemDebit.from_dict(
            d.pop("debit")
        )

        id = d.pop("id")

        name = d.pop("name")

        number = d.pop("number")

        transaction_summary_credit_debit_summary_accounts_item = cls(
            balance=balance,
            credit=credit,
            debit=debit,
            id=id,
            name=name,
            number=number,
        )

        transaction_summary_credit_debit_summary_accounts_item.additional_properties = d
        return transaction_summary_credit_debit_summary_accounts_item

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
