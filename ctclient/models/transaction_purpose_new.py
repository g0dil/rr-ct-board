from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionPurposeNew")


@_attrs_define
class TransactionPurposeNew:
    """
    Example:
        {'accountIds': [4, 5, 6], 'costCenterId': 5, 'isIncome': True, 'name': 'Für was steht der Zweck nochmal?',
            'purposeAccountId': 6, 'sortKey': 7}

    Attributes:
        cost_center_id (int | None):
        is_income (bool):
        name (str):
        purpose_account_id (int):
        sort_key (int):
        account_ids (list[int] | Unset):
    """

    cost_center_id: int | None
    is_income: bool
    name: str
    purpose_account_id: int
    sort_key: int
    account_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_center_id: int | None
        cost_center_id = self.cost_center_id

        is_income = self.is_income

        name = self.name

        purpose_account_id = self.purpose_account_id

        sort_key = self.sort_key

        account_ids: list[int] | Unset = UNSET
        if not isinstance(self.account_ids, Unset):
            account_ids = self.account_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "costCenterId": cost_center_id,
                "isIncome": is_income,
                "name": name,
                "purposeAccountId": purpose_account_id,
                "sortKey": sort_key,
            }
        )
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cost_center_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cost_center_id = _parse_cost_center_id(d.pop("costCenterId"))

        is_income = d.pop("isIncome")

        name = d.pop("name")

        purpose_account_id = d.pop("purposeAccountId")

        sort_key = d.pop("sortKey")

        account_ids = cast(list[int], d.pop("accountIds", UNSET))

        transaction_purpose_new = cls(
            cost_center_id=cost_center_id,
            is_income=is_income,
            name=name,
            purpose_account_id=purpose_account_id,
            sort_key=sort_key,
            account_ids=account_ids,
        )

        transaction_purpose_new.additional_properties = d
        return transaction_purpose_new

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
