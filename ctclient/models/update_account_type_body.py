from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_account_type_body_balance_type_type_1 import (
    UpdateAccountTypeBodyBalanceTypeType1,
)
from ..models.update_account_type_body_balance_type_type_2_type_1 import (
    UpdateAccountTypeBodyBalanceTypeType2Type1,
)
from ..models.update_account_type_body_balance_type_type_3_type_1 import (
    UpdateAccountTypeBodyBalanceTypeType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAccountTypeBody")


@_attrs_define
class UpdateAccountTypeBody:
    """
    Example:
        {'balanceType': 'assets', 'name': 'Aktiva', 'sortKey': 0}

    Attributes:
        balance_type (None | UpdateAccountTypeBodyBalanceTypeType1 | UpdateAccountTypeBodyBalanceTypeType2Type1 |
            UpdateAccountTypeBodyBalanceTypeType3Type1):
        name (str):
        sort_key (int | Unset):  Default: 0.
    """

    balance_type: (
        None
        | UpdateAccountTypeBodyBalanceTypeType1
        | UpdateAccountTypeBodyBalanceTypeType2Type1
        | UpdateAccountTypeBodyBalanceTypeType3Type1
    )
    name: str
    sort_key: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance_type: None | str
        if isinstance(self.balance_type, UpdateAccountTypeBodyBalanceTypeType1):
            balance_type = self.balance_type.value
        elif isinstance(self.balance_type, UpdateAccountTypeBodyBalanceTypeType2Type1):
            balance_type = self.balance_type.value
        elif isinstance(self.balance_type, UpdateAccountTypeBodyBalanceTypeType3Type1):
            balance_type = self.balance_type.value
        else:
            balance_type = self.balance_type

        name = self.name

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balanceType": balance_type,
                "name": name,
            }
        )
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_balance_type(
            data: object,
        ) -> (
            None
            | UpdateAccountTypeBodyBalanceTypeType1
            | UpdateAccountTypeBodyBalanceTypeType2Type1
            | UpdateAccountTypeBodyBalanceTypeType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                balance_type_type_1 = UpdateAccountTypeBodyBalanceTypeType1(data)

                return balance_type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                balance_type_type_2_type_1 = UpdateAccountTypeBodyBalanceTypeType2Type1(
                    data
                )

                return balance_type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                balance_type_type_3_type_1 = UpdateAccountTypeBodyBalanceTypeType3Type1(
                    data
                )

                return balance_type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                None
                | UpdateAccountTypeBodyBalanceTypeType1
                | UpdateAccountTypeBodyBalanceTypeType2Type1
                | UpdateAccountTypeBodyBalanceTypeType3Type1,
                data,
            )

        balance_type = _parse_balance_type(d.pop("balanceType"))

        name = d.pop("name")

        sort_key = d.pop("sortKey", UNSET)

        update_account_type_body = cls(
            balance_type=balance_type,
            name=name,
            sort_key=sort_key,
        )

        update_account_type_body.additional_properties = d
        return update_account_type_body

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
