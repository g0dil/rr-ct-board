from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchTransactionBodyFiltersType1")


@_attrs_define
class BatchTransactionBodyFiltersType1:
    """Include explicit IDs

    Attributes:
        accounting_period_id (int): Filter by Accounting Period Example: 1.
        include_ids (list[int]): List of Transaction IDs. Only those Transactions are updated. Example: [21, 42].
        include (list[int] | Unset): List of Transaction IDs. Only those Transactions are updated. Example: [21, 42].
    """

    accounting_period_id: int
    include_ids: list[int]
    include: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_period_id = self.accounting_period_id

        include_ids = self.include_ids

        include: list[int] | Unset = UNSET
        if not isinstance(self.include, Unset):
            include = self.include

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountingPeriodId": accounting_period_id,
                "includeIds": include_ids,
            }
        )
        if include is not UNSET:
            field_dict["include"] = include

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounting_period_id = d.pop("accountingPeriodId")

        include_ids = cast(list[int], d.pop("includeIds"))

        include = cast(list[int], d.pop("include", UNSET))

        batch_transaction_body_filters_type_1 = cls(
            accounting_period_id=accounting_period_id,
            include_ids=include_ids,
            include=include,
        )

        batch_transaction_body_filters_type_1.additional_properties = d
        return batch_transaction_body_filters_type_1

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
