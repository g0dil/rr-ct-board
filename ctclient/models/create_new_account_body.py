from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateNewAccountBody")


@_attrs_define
class CreateNewAccountBody:
    """
    Example:
        {'accountGroupId': 4, 'accountingPeriodId': 5, 'budget': 1000000, 'example': 'Donations', 'identifier':
            'DE12345678901234567890', 'isDonationAccount': False, 'isOpeningBalanceAccount': False, 'name': 'the new
            donations account', 'number': '8200'}

    Attributes:
        account_group_id (int):
        accounting_period_id (int):
        name (str):
        number (str):
        budget (int | Unset):
        identifier (str | Unset):
        is_donation_account (bool | Unset):
        is_opening_balance_account (bool | Unset):
    """

    account_group_id: int
    accounting_period_id: int
    name: str
    number: str
    budget: int | Unset = UNSET
    identifier: str | Unset = UNSET
    is_donation_account: bool | Unset = UNSET
    is_opening_balance_account: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_group_id = self.account_group_id

        accounting_period_id = self.accounting_period_id

        name = self.name

        number = self.number

        budget = self.budget

        identifier = self.identifier

        is_donation_account = self.is_donation_account

        is_opening_balance_account = self.is_opening_balance_account

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountGroupId": account_group_id,
                "accountingPeriodId": accounting_period_id,
                "name": name,
                "number": number,
            }
        )
        if budget is not UNSET:
            field_dict["budget"] = budget
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if is_donation_account is not UNSET:
            field_dict["isDonationAccount"] = is_donation_account
        if is_opening_balance_account is not UNSET:
            field_dict["isOpeningBalanceAccount"] = is_opening_balance_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_group_id = d.pop("accountGroupId")

        accounting_period_id = d.pop("accountingPeriodId")

        name = d.pop("name")

        number = d.pop("number")

        budget = d.pop("budget", UNSET)

        identifier = d.pop("identifier", UNSET)

        is_donation_account = d.pop("isDonationAccount", UNSET)

        is_opening_balance_account = d.pop("isOpeningBalanceAccount", UNSET)

        create_new_account_body = cls(
            account_group_id=account_group_id,
            accounting_period_id=accounting_period_id,
            name=name,
            number=number,
            budget=budget,
            identifier=identifier,
            is_donation_account=is_donation_account,
            is_opening_balance_account=is_opening_balance_account,
        )

        create_new_account_body.additional_properties = d
        return create_new_account_body

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
