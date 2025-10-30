from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAllFinanceTemplatesResponse200ItemCounts")


@_attrs_define
class GetAllFinanceTemplatesResponse200ItemCounts:
    """
    Attributes:
        account_classes (int | Unset):
        account_groups (int | Unset):
        account_types (int | Unset):
        accounts (int | Unset):
        cost_centers (int | Unset):
        tax_rates (int | Unset):
        tax_types (int | Unset):
    """

    account_classes: int | Unset = UNSET
    account_groups: int | Unset = UNSET
    account_types: int | Unset = UNSET
    accounts: int | Unset = UNSET
    cost_centers: int | Unset = UNSET
    tax_rates: int | Unset = UNSET
    tax_types: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_classes = self.account_classes

        account_groups = self.account_groups

        account_types = self.account_types

        accounts = self.accounts

        cost_centers = self.cost_centers

        tax_rates = self.tax_rates

        tax_types = self.tax_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_classes is not UNSET:
            field_dict["accountClasses"] = account_classes
        if account_groups is not UNSET:
            field_dict["accountGroups"] = account_groups
        if account_types is not UNSET:
            field_dict["accountTypes"] = account_types
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if cost_centers is not UNSET:
            field_dict["costCenters"] = cost_centers
        if tax_rates is not UNSET:
            field_dict["taxRates"] = tax_rates
        if tax_types is not UNSET:
            field_dict["taxTypes"] = tax_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_classes = d.pop("accountClasses", UNSET)

        account_groups = d.pop("accountGroups", UNSET)

        account_types = d.pop("accountTypes", UNSET)

        accounts = d.pop("accounts", UNSET)

        cost_centers = d.pop("costCenters", UNSET)

        tax_rates = d.pop("taxRates", UNSET)

        tax_types = d.pop("taxTypes", UNSET)

        get_all_finance_templates_response_200_item_counts = cls(
            account_classes=account_classes,
            account_groups=account_groups,
            account_types=account_types,
            accounts=accounts,
            cost_centers=cost_centers,
            tax_rates=tax_rates,
            tax_types=tax_types,
        )

        get_all_finance_templates_response_200_item_counts.additional_properties = d
        return get_all_finance_templates_response_200_item_counts

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
