from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TaxRateNew")


@_attrs_define
class TaxRateNew:
    """
    Example:
        {'accountId': 5, 'note': 'Ust. 7%', 'rate': 0.07, 'taxTypeId': 4}

    Attributes:
        account_id (int):
        note (str):
        rate (float):
        tax_type_id (int):
    """

    account_id: int
    note: str
    rate: float
    tax_type_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        note = self.note

        rate = self.rate

        tax_type_id = self.tax_type_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "note": note,
                "rate": rate,
                "taxTypeId": tax_type_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId")

        note = d.pop("note")

        rate = d.pop("rate")

        tax_type_id = d.pop("taxTypeId")

        tax_rate_new = cls(
            account_id=account_id,
            note=note,
            rate=rate,
            tax_type_id=tax_type_id,
        )

        tax_rate_new.additional_properties = d
        return tax_rate_new

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
