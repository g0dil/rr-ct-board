from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_transaction_purpose_by_id_response_200_data_meta import (
        GetTransactionPurposeByIdResponse200DataMeta,
    )


T = TypeVar("T", bound="GetTransactionPurposeByIdResponse200Data")


@_attrs_define
class GetTransactionPurposeByIdResponse200Data:
    """
    Example:
        {'accountIds': [1, 2, 3], 'costCenterId': 2, 'id': 1, 'isIncome': True, 'name': 'Der Zweck heiligt die Mittel',
            'purposeAccountId': 3, 'sortKey': 4}

    Attributes:
        account_ids (list[int] | Unset):
        cost_center_id (int | None | Unset):
        id (int | Unset):
        is_income (bool | Unset):
        meta (GetTransactionPurposeByIdResponse200DataMeta | Unset):  Example: {'createdDate': '2020-01-01T00:00:00Z',
            'createdPerson': {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        name (str | Unset):
        purpose_account_id (int | Unset): This will always be a single account. But it depends on the `isIncome` flag if
            this is the debit or the credit account.
        sort_key (int | Unset):
    """

    account_ids: list[int] | Unset = UNSET
    cost_center_id: int | None | Unset = UNSET
    id: int | Unset = UNSET
    is_income: bool | Unset = UNSET
    meta: GetTransactionPurposeByIdResponse200DataMeta | Unset = UNSET
    name: str | Unset = UNSET
    purpose_account_id: int | Unset = UNSET
    sort_key: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_ids: list[int] | Unset = UNSET
        if not isinstance(self.account_ids, Unset):
            account_ids = self.account_ids

        cost_center_id: int | None | Unset
        if isinstance(self.cost_center_id, Unset):
            cost_center_id = UNSET
        else:
            cost_center_id = self.cost_center_id

        id = self.id

        is_income = self.is_income

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        name = self.name

        purpose_account_id = self.purpose_account_id

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids
        if cost_center_id is not UNSET:
            field_dict["costCenterId"] = cost_center_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_income is not UNSET:
            field_dict["isIncome"] = is_income
        if meta is not UNSET:
            field_dict["meta"] = meta
        if name is not UNSET:
            field_dict["name"] = name
        if purpose_account_id is not UNSET:
            field_dict["purposeAccountId"] = purpose_account_id
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_transaction_purpose_by_id_response_200_data_meta import (
            GetTransactionPurposeByIdResponse200DataMeta,
        )

        d = dict(src_dict)
        account_ids = cast(list[int], d.pop("accountIds", UNSET))

        def _parse_cost_center_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cost_center_id = _parse_cost_center_id(d.pop("costCenterId", UNSET))

        id = d.pop("id", UNSET)

        is_income = d.pop("isIncome", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: GetTransactionPurposeByIdResponse200DataMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GetTransactionPurposeByIdResponse200DataMeta.from_dict(_meta)

        name = d.pop("name", UNSET)

        purpose_account_id = d.pop("purposeAccountId", UNSET)

        sort_key = d.pop("sortKey", UNSET)

        get_transaction_purpose_by_id_response_200_data = cls(
            account_ids=account_ids,
            cost_center_id=cost_center_id,
            id=id,
            is_income=is_income,
            meta=meta,
            name=name,
            purpose_account_id=purpose_account_id,
            sort_key=sort_key,
        )

        get_transaction_purpose_by_id_response_200_data.additional_properties = d
        return get_transaction_purpose_by_id_response_200_data

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
