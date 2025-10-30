from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_user_rules_response_200_data_item_operator import (
    GetUserRulesResponse200DataItemOperator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUserRulesResponse200DataItem")


@_attrs_define
class GetUserRulesResponse200DataItem:
    """
    Attributes:
        account_ids (list[int] | Unset):
        accounting_period_id (int | Unset):
        all_accounts (bool | Unset):
        id (int | Unset):
        is_income (bool | Unset):
        operator (GetUserRulesResponse200DataItemOperator | Unset):
        search_string (str | Unset):
        search_type (str | Unset):
        sort_key (int | Unset):
        suggestion_type (str | Unset):
        suggestion_value (str | Unset):
    """

    account_ids: list[int] | Unset = UNSET
    accounting_period_id: int | Unset = UNSET
    all_accounts: bool | Unset = UNSET
    id: int | Unset = UNSET
    is_income: bool | Unset = UNSET
    operator: GetUserRulesResponse200DataItemOperator | Unset = UNSET
    search_string: str | Unset = UNSET
    search_type: str | Unset = UNSET
    sort_key: int | Unset = UNSET
    suggestion_type: str | Unset = UNSET
    suggestion_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_ids: list[int] | Unset = UNSET
        if not isinstance(self.account_ids, Unset):
            account_ids = self.account_ids

        accounting_period_id = self.accounting_period_id

        all_accounts = self.all_accounts

        id = self.id

        is_income = self.is_income

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        search_string = self.search_string

        search_type = self.search_type

        sort_key = self.sort_key

        suggestion_type = self.suggestion_type

        suggestion_value = self.suggestion_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids
        if accounting_period_id is not UNSET:
            field_dict["accountingPeriodId"] = accounting_period_id
        if all_accounts is not UNSET:
            field_dict["allAccounts"] = all_accounts
        if id is not UNSET:
            field_dict["id"] = id
        if is_income is not UNSET:
            field_dict["isIncome"] = is_income
        if operator is not UNSET:
            field_dict["operator"] = operator
        if search_string is not UNSET:
            field_dict["searchString"] = search_string
        if search_type is not UNSET:
            field_dict["searchType"] = search_type
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key
        if suggestion_type is not UNSET:
            field_dict["suggestionType"] = suggestion_type
        if suggestion_value is not UNSET:
            field_dict["suggestionValue"] = suggestion_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_ids = cast(list[int], d.pop("accountIds", UNSET))

        accounting_period_id = d.pop("accountingPeriodId", UNSET)

        all_accounts = d.pop("allAccounts", UNSET)

        id = d.pop("id", UNSET)

        is_income = d.pop("isIncome", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: GetUserRulesResponse200DataItemOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = GetUserRulesResponse200DataItemOperator(_operator)

        search_string = d.pop("searchString", UNSET)

        search_type = d.pop("searchType", UNSET)

        sort_key = d.pop("sortKey", UNSET)

        suggestion_type = d.pop("suggestionType", UNSET)

        suggestion_value = d.pop("suggestionValue", UNSET)

        get_user_rules_response_200_data_item = cls(
            account_ids=account_ids,
            accounting_period_id=accounting_period_id,
            all_accounts=all_accounts,
            id=id,
            is_income=is_income,
            operator=operator,
            search_string=search_string,
            search_type=search_type,
            sort_key=sort_key,
            suggestion_type=suggestion_type,
            suggestion_value=suggestion_value,
        )

        get_user_rules_response_200_data_item.additional_properties = d
        return get_user_rules_response_200_data_item

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
