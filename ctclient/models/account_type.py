from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_type_balance_type_type_1 import AccountTypeBalanceTypeType1
from ..models.account_type_balance_type_type_2_type_1 import (
    AccountTypeBalanceTypeType2Type1,
)
from ..models.account_type_balance_type_type_3_type_1 import (
    AccountTypeBalanceTypeType3Type1,
)

if TYPE_CHECKING:
    from ..models.account_type_meta import AccountTypeMeta


T = TypeVar("T", bound="AccountType")


@_attrs_define
class AccountType:
    """
    Attributes:
        balance_type (AccountTypeBalanceTypeType1 | AccountTypeBalanceTypeType2Type1 | AccountTypeBalanceTypeType3Type1
            | None):  Example: assets.
        id (int):  Example: 1.
        is_balance_account (bool):
        meta (AccountTypeMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson': {'id': 1},
            'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        name (str):  Example: Aktiva.
        sort_key (int):  Default: 0.
    """

    balance_type: (
        AccountTypeBalanceTypeType1
        | AccountTypeBalanceTypeType2Type1
        | AccountTypeBalanceTypeType3Type1
        | None
    )
    id: int
    is_balance_account: bool
    meta: AccountTypeMeta
    name: str
    sort_key: int = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance_type: None | str
        if isinstance(self.balance_type, AccountTypeBalanceTypeType1):
            balance_type = self.balance_type.value
        elif isinstance(self.balance_type, AccountTypeBalanceTypeType2Type1):
            balance_type = self.balance_type.value
        elif isinstance(self.balance_type, AccountTypeBalanceTypeType3Type1):
            balance_type = self.balance_type.value
        else:
            balance_type = self.balance_type

        id = self.id

        is_balance_account = self.is_balance_account

        meta = self.meta.to_dict()

        name = self.name

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balanceType": balance_type,
                "id": id,
                "isBalanceAccount": is_balance_account,
                "meta": meta,
                "name": name,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_type_meta import AccountTypeMeta

        d = dict(src_dict)

        def _parse_balance_type(
            data: object,
        ) -> (
            AccountTypeBalanceTypeType1
            | AccountTypeBalanceTypeType2Type1
            | AccountTypeBalanceTypeType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                balance_type_type_1 = AccountTypeBalanceTypeType1(data)

                return balance_type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                balance_type_type_2_type_1 = AccountTypeBalanceTypeType2Type1(data)

                return balance_type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                balance_type_type_3_type_1 = AccountTypeBalanceTypeType3Type1(data)

                return balance_type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                AccountTypeBalanceTypeType1
                | AccountTypeBalanceTypeType2Type1
                | AccountTypeBalanceTypeType3Type1
                | None,
                data,
            )

        balance_type = _parse_balance_type(d.pop("balanceType"))

        id = d.pop("id")

        is_balance_account = d.pop("isBalanceAccount")

        meta = AccountTypeMeta.from_dict(d.pop("meta"))

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        account_type = cls(
            balance_type=balance_type,
            id=id,
            is_balance_account=is_balance_account,
            meta=meta,
            name=name,
            sort_key=sort_key,
        )

        account_type.additional_properties = d
        return account_type

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
