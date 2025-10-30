from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchTransactionBodyFiltersType2")


@_attrs_define
class BatchTransactionBodyFiltersType2:
    """Exclude specific IDs

    Attributes:
        accounting_period_id (int): Filter by Accounting Period Example: 1.
        exclude_ids (list[int]): List of Transaction IDs. All Transactions except this list of IDs are updated in the
            given Accouting Period.
        exclude (list[int] | Unset): List of Transaction IDs. All Transactions except this list of IDs are updated in
            the given Accouting Period.
    """

    accounting_period_id: int
    exclude_ids: list[int]
    exclude: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_period_id = self.accounting_period_id

        exclude_ids = self.exclude_ids

        exclude: list[int] | Unset = UNSET
        if not isinstance(self.exclude, Unset):
            exclude = self.exclude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountingPeriodId": accounting_period_id,
                "excludeIds": exclude_ids,
            }
        )
        if exclude is not UNSET:
            field_dict["exclude"] = exclude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounting_period_id = d.pop("accountingPeriodId")

        exclude_ids = cast(list[int], d.pop("excludeIds"))

        exclude = cast(list[int], d.pop("exclude", UNSET))

        batch_transaction_body_filters_type_2 = cls(
            accounting_period_id=accounting_period_id,
            exclude_ids=exclude_ids,
            exclude=exclude,
        )

        batch_transaction_body_filters_type_2.additional_properties = d
        return batch_transaction_body_filters_type_2

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
