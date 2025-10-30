from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_new_account_type_response_200_data_item_balance_type_type_1 import (
    CreateNewAccountTypeResponse200DataItemBalanceTypeType1,
)
from ..models.create_new_account_type_response_200_data_item_balance_type_type_2_type_1 import (
    CreateNewAccountTypeResponse200DataItemBalanceTypeType2Type1,
)
from ..models.create_new_account_type_response_200_data_item_balance_type_type_3_type_1 import (
    CreateNewAccountTypeResponse200DataItemBalanceTypeType3Type1,
)

if TYPE_CHECKING:
    from ..models.create_new_account_type_response_200_data_item_meta import (
        CreateNewAccountTypeResponse200DataItemMeta,
    )


T = TypeVar("T", bound="CreateNewAccountTypeResponse200DataItem")


@_attrs_define
class CreateNewAccountTypeResponse200DataItem:
    """
    Attributes:
        balance_type (CreateNewAccountTypeResponse200DataItemBalanceTypeType1 |
            CreateNewAccountTypeResponse200DataItemBalanceTypeType2Type1 |
            CreateNewAccountTypeResponse200DataItemBalanceTypeType3Type1 | None):  Example: assets.
        id (int):  Example: 1.
        is_balance_account (bool):
        meta (CreateNewAccountTypeResponse200DataItemMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z',
            'createdPerson': {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        name (str):  Example: Aktiva.
        sort_key (int):  Default: 0.
    """

    balance_type: (
        CreateNewAccountTypeResponse200DataItemBalanceTypeType1
        | CreateNewAccountTypeResponse200DataItemBalanceTypeType2Type1
        | CreateNewAccountTypeResponse200DataItemBalanceTypeType3Type1
        | None
    )
    id: int
    is_balance_account: bool
    meta: CreateNewAccountTypeResponse200DataItemMeta
    name: str
    sort_key: int = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance_type: None | str
        if isinstance(
            self.balance_type, CreateNewAccountTypeResponse200DataItemBalanceTypeType1
        ):
            balance_type = self.balance_type.value
        elif isinstance(
            self.balance_type,
            CreateNewAccountTypeResponse200DataItemBalanceTypeType2Type1,
        ):
            balance_type = self.balance_type.value
        elif isinstance(
            self.balance_type,
            CreateNewAccountTypeResponse200DataItemBalanceTypeType3Type1,
        ):
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
        from ..models.create_new_account_type_response_200_data_item_meta import (
            CreateNewAccountTypeResponse200DataItemMeta,
        )

        d = dict(src_dict)

        def _parse_balance_type(
            data: object,
        ) -> (
            CreateNewAccountTypeResponse200DataItemBalanceTypeType1
            | CreateNewAccountTypeResponse200DataItemBalanceTypeType2Type1
            | CreateNewAccountTypeResponse200DataItemBalanceTypeType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                balance_type_type_1 = (
                    CreateNewAccountTypeResponse200DataItemBalanceTypeType1(data)
                )

                return balance_type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                balance_type_type_2_type_1 = (
                    CreateNewAccountTypeResponse200DataItemBalanceTypeType2Type1(data)
                )

                return balance_type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                balance_type_type_3_type_1 = (
                    CreateNewAccountTypeResponse200DataItemBalanceTypeType3Type1(data)
                )

                return balance_type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                CreateNewAccountTypeResponse200DataItemBalanceTypeType1
                | CreateNewAccountTypeResponse200DataItemBalanceTypeType2Type1
                | CreateNewAccountTypeResponse200DataItemBalanceTypeType3Type1
                | None,
                data,
            )

        balance_type = _parse_balance_type(d.pop("balanceType"))

        id = d.pop("id")

        is_balance_account = d.pop("isBalanceAccount")

        meta = CreateNewAccountTypeResponse200DataItemMeta.from_dict(d.pop("meta"))

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        create_new_account_type_response_200_data_item = cls(
            balance_type=balance_type,
            id=id,
            is_balance_account=is_balance_account,
            meta=meta,
            name=name,
            sort_key=sort_key,
        )

        create_new_account_type_response_200_data_item.additional_properties = d
        return create_new_account_type_response_200_data_item

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
