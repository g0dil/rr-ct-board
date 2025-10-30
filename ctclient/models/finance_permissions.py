from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancePermissions")


@_attrs_define
class FinancePermissions:
    """
    Attributes:
        can_view_budgets (bool | Unset):
        can_view_donators (bool | Unset):
        can_view_reports (bool | Unset):
        can_view_transactions (bool | Unset):
        edit_master_data (bool | Unset):
    """

    can_view_budgets: bool | Unset = UNSET
    can_view_donators: bool | Unset = UNSET
    can_view_reports: bool | Unset = UNSET
    can_view_transactions: bool | Unset = UNSET
    edit_master_data: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_view_budgets = self.can_view_budgets

        can_view_donators = self.can_view_donators

        can_view_reports = self.can_view_reports

        can_view_transactions = self.can_view_transactions

        edit_master_data = self.edit_master_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_view_budgets is not UNSET:
            field_dict["canViewBudgets"] = can_view_budgets
        if can_view_donators is not UNSET:
            field_dict["canViewDonators"] = can_view_donators
        if can_view_reports is not UNSET:
            field_dict["canViewReports"] = can_view_reports
        if can_view_transactions is not UNSET:
            field_dict["canViewTransactions"] = can_view_transactions
        if edit_master_data is not UNSET:
            field_dict["editMasterData"] = edit_master_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_view_budgets = d.pop("canViewBudgets", UNSET)

        can_view_donators = d.pop("canViewDonators", UNSET)

        can_view_reports = d.pop("canViewReports", UNSET)

        can_view_transactions = d.pop("canViewTransactions", UNSET)

        edit_master_data = d.pop("editMasterData", UNSET)

        finance_permissions = cls(
            can_view_budgets=can_view_budgets,
            can_view_donators=can_view_donators,
            can_view_reports=can_view_reports,
            can_view_transactions=can_view_transactions,
            edit_master_data=edit_master_data,
        )

        finance_permissions.additional_properties = d
        return finance_permissions

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
