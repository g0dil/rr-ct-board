from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAccountGroupBody")


@_attrs_define
class UpdateAccountGroupBody:
    """
    Example:
        {'accountClassId': 3, 'isCashAssetAccount': False, 'name': 'Neue Konto gruppe', 'sortKey': 0}

    Attributes:
        account_class_id (int):
        is_cash_asset_account (bool):
        name (str):
        sort_key (int | Unset):  Default: 0.
    """

    account_class_id: int
    is_cash_asset_account: bool
    name: str
    sort_key: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_class_id = self.account_class_id

        is_cash_asset_account = self.is_cash_asset_account

        name = self.name

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountClassId": account_class_id,
                "isCashAssetAccount": is_cash_asset_account,
                "name": name,
            }
        )
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_class_id = d.pop("accountClassId")

        is_cash_asset_account = d.pop("isCashAssetAccount")

        name = d.pop("name")

        sort_key = d.pop("sortKey", UNSET)

        update_account_group_body = cls(
            account_class_id=account_class_id,
            is_cash_asset_account=is_cash_asset_account,
            name=name,
            sort_key=sort_key,
        )

        update_account_group_body.additional_properties = d
        return update_account_group_body

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
