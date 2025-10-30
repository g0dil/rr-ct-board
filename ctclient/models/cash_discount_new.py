from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CashDiscountNew")


@_attrs_define
class CashDiscountNew:
    """
    Example:
        {'accountId': 3, 'note': 'Skonto 3%', 'rate': 0.03}

    Attributes:
        account_id (int):
        note (str):
        rate (float):
    """

    account_id: int
    note: str
    rate: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        note = self.note

        rate = self.rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "note": note,
                "rate": rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId")

        note = d.pop("note")

        rate = d.pop("rate")

        cash_discount_new = cls(
            account_id=account_id,
            note=note,
            rate=rate,
        )

        cash_discount_new.additional_properties = d
        return cash_discount_new

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
