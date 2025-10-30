from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_account_group_response_200_data_meta import (
        UpdateAccountGroupResponse200DataMeta,
    )


T = TypeVar("T", bound="UpdateAccountGroupResponse200Data")


@_attrs_define
class UpdateAccountGroupResponse200Data:
    """
    Attributes:
        account_class_id (int):  Example: 2.
        id (int):  Example: 1.
        is_cash_asset_account (bool):
        meta (UpdateAccountGroupResponse200DataMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson':
            {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        name (str):  Example: Sachanlagen.
        sort_key (int):  Default: 0.
    """

    account_class_id: int
    id: int
    is_cash_asset_account: bool
    meta: UpdateAccountGroupResponse200DataMeta
    name: str
    sort_key: int = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_class_id = self.account_class_id

        id = self.id

        is_cash_asset_account = self.is_cash_asset_account

        meta = self.meta.to_dict()

        name = self.name

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountClassId": account_class_id,
                "id": id,
                "isCashAssetAccount": is_cash_asset_account,
                "meta": meta,
                "name": name,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_account_group_response_200_data_meta import (
            UpdateAccountGroupResponse200DataMeta,
        )

        d = dict(src_dict)
        account_class_id = d.pop("accountClassId")

        id = d.pop("id")

        is_cash_asset_account = d.pop("isCashAssetAccount")

        meta = UpdateAccountGroupResponse200DataMeta.from_dict(d.pop("meta"))

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        update_account_group_response_200_data = cls(
            account_class_id=account_class_id,
            id=id,
            is_cash_asset_account=is_cash_asset_account,
            meta=meta,
            name=name,
            sort_key=sort_key,
        )

        update_account_group_response_200_data.additional_properties = d
        return update_account_group_response_200_data

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
