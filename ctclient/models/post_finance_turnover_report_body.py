from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_finance_turnover_report_body_period import (
    PostFinanceTurnoverReportBodyPeriod,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFinanceTurnoverReportBody")


@_attrs_define
class PostFinanceTurnoverReportBody:
    """
    Attributes:
        accounting_period_id (float): ID of Accounting Period Example: 1.
        period (PostFinanceTurnoverReportBodyPeriod): Select monthly oder quarterly report Example: monthly.
        show_empty_accounts (bool | Unset): Show Accounts With No Transactions Default: False.
    """

    accounting_period_id: float
    period: PostFinanceTurnoverReportBodyPeriod
    show_empty_accounts: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_period_id = self.accounting_period_id

        period = self.period.value

        show_empty_accounts = self.show_empty_accounts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountingPeriodId": accounting_period_id,
                "period": period,
            }
        )
        if show_empty_accounts is not UNSET:
            field_dict["showEmptyAccounts"] = show_empty_accounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounting_period_id = d.pop("accountingPeriodId")

        period = PostFinanceTurnoverReportBodyPeriod(d.pop("period"))

        show_empty_accounts = d.pop("showEmptyAccounts", UNSET)

        post_finance_turnover_report_body = cls(
            accounting_period_id=accounting_period_id,
            period=period,
            show_empty_accounts=show_empty_accounts,
        )

        post_finance_turnover_report_body.additional_properties = d
        return post_finance_turnover_report_body

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
