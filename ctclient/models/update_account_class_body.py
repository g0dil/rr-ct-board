from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAccountClassBody")


@_attrs_define
class UpdateAccountClassBody:
    """
    Attributes:
        account_type_id (int):  Example: 3.
        name (str):  Example: Verwaltungsvermögen.
        include_profit_loss (bool | Unset):  Default: False.
        sort_key (int | Unset):  Default: 0.
    """

    account_type_id: int
    name: str
    include_profit_loss: bool | Unset = False
    sort_key: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_type_id = self.account_type_id

        name = self.name

        include_profit_loss = self.include_profit_loss

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountTypeId": account_type_id,
                "name": name,
            }
        )
        if include_profit_loss is not UNSET:
            field_dict["includeProfitLoss"] = include_profit_loss
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_type_id = d.pop("accountTypeId")

        name = d.pop("name")

        include_profit_loss = d.pop("includeProfitLoss", UNSET)

        sort_key = d.pop("sortKey", UNSET)

        update_account_class_body = cls(
            account_type_id=account_type_id,
            name=name,
            include_profit_loss=include_profit_loss,
            sort_key=sort_key,
        )

        update_account_class_body.additional_properties = d
        return update_account_class_body

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
