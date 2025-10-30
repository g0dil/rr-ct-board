from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_new_account_response_200_data_item_meta import (
        CreateNewAccountResponse200DataItemMeta,
    )
    from ..models.create_new_account_response_200_data_item_permissions import (
        CreateNewAccountResponse200DataItemPermissions,
    )


T = TypeVar("T", bound="CreateNewAccountResponse200DataItem")


@_attrs_define
class CreateNewAccountResponse200DataItem:
    """
    Attributes:
        account_group_id (int):  Example: 2.
        accounting_period_id (int):  Example: 3.
        annotation (None | str):
        balance (int): Current balance of account in cent. Example: 20043.
        budget (int | None): Budget of account in cent. Example: 100000.
        budget_balance (int): Current budget balance of account in cent. Example: 19500.
        budget_balance_last_period (int): Budget balance of matching account from last period in euro cent. Example:
            8300.
        budget_last_period (int | None): Budget of matching account from last period in euro cent. Example: 20000.
        id (int):  Example: 1.
        identifier (str):
        is_donation_account (bool):  Example: True.
        is_opening_balance_account (bool):
        meta (CreateNewAccountResponse200DataItemMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z',
            'createdPerson': {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        name (str):  Example: Donations.
        number (str):  Example: 8200.
        permissions (CreateNewAccountResponse200DataItemPermissions):
        tax_rate_id (int | None):
    """

    account_group_id: int
    accounting_period_id: int
    annotation: None | str
    balance: int
    budget: int | None
    budget_balance: int
    budget_balance_last_period: int
    budget_last_period: int | None
    id: int
    identifier: str
    is_donation_account: bool
    is_opening_balance_account: bool
    meta: CreateNewAccountResponse200DataItemMeta
    name: str
    number: str
    permissions: CreateNewAccountResponse200DataItemPermissions
    tax_rate_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_group_id = self.account_group_id

        accounting_period_id = self.accounting_period_id

        annotation: None | str
        annotation = self.annotation

        balance = self.balance

        budget: int | None
        budget = self.budget

        budget_balance = self.budget_balance

        budget_balance_last_period = self.budget_balance_last_period

        budget_last_period: int | None
        budget_last_period = self.budget_last_period

        id = self.id

        identifier = self.identifier

        is_donation_account = self.is_donation_account

        is_opening_balance_account = self.is_opening_balance_account

        meta = self.meta.to_dict()

        name = self.name

        number = self.number

        permissions = self.permissions.to_dict()

        tax_rate_id: int | None
        tax_rate_id = self.tax_rate_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountGroupId": account_group_id,
                "accountingPeriodId": accounting_period_id,
                "annotation": annotation,
                "balance": balance,
                "budget": budget,
                "budgetBalance": budget_balance,
                "budgetBalanceLastPeriod": budget_balance_last_period,
                "budgetLastPeriod": budget_last_period,
                "id": id,
                "identifier": identifier,
                "isDonationAccount": is_donation_account,
                "isOpeningBalanceAccount": is_opening_balance_account,
                "meta": meta,
                "name": name,
                "number": number,
                "permissions": permissions,
                "taxRateId": tax_rate_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_new_account_response_200_data_item_meta import (
            CreateNewAccountResponse200DataItemMeta,
        )
        from ..models.create_new_account_response_200_data_item_permissions import (
            CreateNewAccountResponse200DataItemPermissions,
        )

        d = dict(src_dict)
        account_group_id = d.pop("accountGroupId")

        accounting_period_id = d.pop("accountingPeriodId")

        def _parse_annotation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        annotation = _parse_annotation(d.pop("annotation"))

        balance = d.pop("balance")

        def _parse_budget(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        budget = _parse_budget(d.pop("budget"))

        budget_balance = d.pop("budgetBalance")

        budget_balance_last_period = d.pop("budgetBalanceLastPeriod")

        def _parse_budget_last_period(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        budget_last_period = _parse_budget_last_period(d.pop("budgetLastPeriod"))

        id = d.pop("id")

        identifier = d.pop("identifier")

        is_donation_account = d.pop("isDonationAccount")

        is_opening_balance_account = d.pop("isOpeningBalanceAccount")

        meta = CreateNewAccountResponse200DataItemMeta.from_dict(d.pop("meta"))

        name = d.pop("name")

        number = d.pop("number")

        permissions = CreateNewAccountResponse200DataItemPermissions.from_dict(
            d.pop("permissions")
        )

        def _parse_tax_rate_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        tax_rate_id = _parse_tax_rate_id(d.pop("taxRateId"))

        create_new_account_response_200_data_item = cls(
            account_group_id=account_group_id,
            accounting_period_id=accounting_period_id,
            annotation=annotation,
            balance=balance,
            budget=budget,
            budget_balance=budget_balance,
            budget_balance_last_period=budget_balance_last_period,
            budget_last_period=budget_last_period,
            id=id,
            identifier=identifier,
            is_donation_account=is_donation_account,
            is_opening_balance_account=is_opening_balance_account,
            meta=meta,
            name=name,
            number=number,
            permissions=permissions,
            tax_rate_id=tax_rate_id,
        )

        create_new_account_response_200_data_item.additional_properties = d
        return create_new_account_response_200_data_item

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
