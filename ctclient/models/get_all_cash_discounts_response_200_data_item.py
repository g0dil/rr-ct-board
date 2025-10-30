from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_all_cash_discounts_response_200_data_item_meta import (
        GetAllCashDiscountsResponse200DataItemMeta,
    )


T = TypeVar("T", bound="GetAllCashDiscountsResponse200DataItem")


@_attrs_define
class GetAllCashDiscountsResponse200DataItem:
    """
    Example:
        {'accountId': 2, 'id': 1, 'note': 'Skonto 2%', 'rate': 0.02}

    Attributes:
        account_id (int | Unset):
        id (int | Unset):
        meta (GetAllCashDiscountsResponse200DataItemMeta | Unset):  Example: {'createdDate': '2020-01-01T00:00:00Z',
            'createdPerson': {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        note (str | Unset):
        rate (float | Unset):
    """

    account_id: int | Unset = UNSET
    id: int | Unset = UNSET
    meta: GetAllCashDiscountsResponse200DataItemMeta | Unset = UNSET
    note: str | Unset = UNSET
    rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        id = self.id

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        note = self.note

        rate = self.rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if id is not UNSET:
            field_dict["id"] = id
        if meta is not UNSET:
            field_dict["meta"] = meta
        if note is not UNSET:
            field_dict["note"] = note
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_all_cash_discounts_response_200_data_item_meta import (
            GetAllCashDiscountsResponse200DataItemMeta,
        )

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        id = d.pop("id", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: GetAllCashDiscountsResponse200DataItemMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GetAllCashDiscountsResponse200DataItemMeta.from_dict(_meta)

        note = d.pop("note", UNSET)

        rate = d.pop("rate", UNSET)

        get_all_cash_discounts_response_200_data_item = cls(
            account_id=account_id,
            id=id,
            meta=meta,
            note=note,
            rate=rate,
        )

        get_all_cash_discounts_response_200_data_item.additional_properties = d
        return get_all_cash_discounts_response_200_data_item

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
