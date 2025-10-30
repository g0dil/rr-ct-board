from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_tax_rate_response_200_data_meta import (
        UpdateTaxRateResponse200DataMeta,
    )


T = TypeVar("T", bound="UpdateTaxRateResponse200Data")


@_attrs_define
class UpdateTaxRateResponse200Data:
    """
    Attributes:
        id (int):
        meta (UpdateTaxRateResponse200DataMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson':
            {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        rate (float):
        tax_type_id (int):
        account_id (int | Unset):
        note (str | Unset):
    """

    id: int
    meta: UpdateTaxRateResponse200DataMeta
    rate: float
    tax_type_id: int
    account_id: int | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        meta = self.meta.to_dict()

        rate = self.rate

        tax_type_id = self.tax_type_id

        account_id = self.account_id

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "meta": meta,
                "rate": rate,
                "taxTypeId": tax_type_id,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_tax_rate_response_200_data_meta import (
            UpdateTaxRateResponse200DataMeta,
        )

        d = dict(src_dict)
        id = d.pop("id")

        meta = UpdateTaxRateResponse200DataMeta.from_dict(d.pop("meta"))

        rate = d.pop("rate")

        tax_type_id = d.pop("taxTypeId")

        account_id = d.pop("accountId", UNSET)

        note = d.pop("note", UNSET)

        update_tax_rate_response_200_data = cls(
            id=id,
            meta=meta,
            rate=rate,
            tax_type_id=tax_type_id,
            account_id=account_id,
            note=note,
        )

        update_tax_rate_response_200_data.additional_properties = d
        return update_tax_rate_response_200_data

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
