from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountingPeriodCreateBalances")


@_attrs_define
class AccountingPeriodCreateBalances:
    """
    Attributes:
        from_ (list[int] | Unset):
        opening_balance_account (int | Unset):
    """

    from_: list[int] | Unset = UNSET
    opening_balance_account: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_: list[int] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_

        opening_balance_account = self.opening_balance_account

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if opening_balance_account is not UNSET:
            field_dict["openingBalanceAccount"] = opening_balance_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = cast(list[int], d.pop("from", UNSET))

        opening_balance_account = d.pop("openingBalanceAccount", UNSET)

        accounting_period_create_balances = cls(
            from_=from_,
            opening_balance_account=opening_balance_account,
        )

        accounting_period_create_balances.additional_properties = d
        return accounting_period_create_balances

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
