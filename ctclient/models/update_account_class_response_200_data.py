from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_account_class_response_200_data_meta import (
        UpdateAccountClassResponse200DataMeta,
    )


T = TypeVar("T", bound="UpdateAccountClassResponse200Data")


@_attrs_define
class UpdateAccountClassResponse200Data:
    """
    Attributes:
        account_type_id (int):  Example: 2.
        id (int):  Example: 1.
        include_profit_loss (bool): If true, an additional row is added to that class in the report, which lists the
            profit-loss sum.
        meta (UpdateAccountClassResponse200DataMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson':
            {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        name (str):  Example: Anlagevermögen.
        sort_key (int):  Default: 0.
    """

    account_type_id: int
    id: int
    include_profit_loss: bool
    meta: UpdateAccountClassResponse200DataMeta
    name: str
    sort_key: int = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_type_id = self.account_type_id

        id = self.id

        include_profit_loss = self.include_profit_loss

        meta = self.meta.to_dict()

        name = self.name

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountTypeId": account_type_id,
                "id": id,
                "includeProfitLoss": include_profit_loss,
                "meta": meta,
                "name": name,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_account_class_response_200_data_meta import (
            UpdateAccountClassResponse200DataMeta,
        )

        d = dict(src_dict)
        account_type_id = d.pop("accountTypeId")

        id = d.pop("id")

        include_profit_loss = d.pop("includeProfitLoss")

        meta = UpdateAccountClassResponse200DataMeta.from_dict(d.pop("meta"))

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        update_account_class_response_200_data = cls(
            account_type_id=account_type_id,
            id=id,
            include_profit_loss=include_profit_loss,
            meta=meta,
            name=name,
            sort_key=sort_key,
        )

        update_account_class_response_200_data.additional_properties = d
        return update_account_class_response_200_data

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
