from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_cash_discount_response_409_data_references_item import (
        DeleteCashDiscountResponse409DataReferencesItem,
    )


T = TypeVar("T", bound="DeleteCashDiscountResponse409Data")


@_attrs_define
class DeleteCashDiscountResponse409Data:
    """
    Attributes:
        deleteable (bool | Unset):
        references (list[DeleteCashDiscountResponse409DataReferencesItem] | Unset):
    """

    deleteable: bool | Unset = UNSET
    references: list[DeleteCashDiscountResponse409DataReferencesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleteable = self.deleteable

        references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleteable is not UNSET:
            field_dict["deleteable"] = deleteable
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_cash_discount_response_409_data_references_item import (
            DeleteCashDiscountResponse409DataReferencesItem,
        )

        d = dict(src_dict)
        deleteable = d.pop("deleteable", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = DeleteCashDiscountResponse409DataReferencesItem.from_dict(
                references_item_data
            )

            references.append(references_item)

        delete_cash_discount_response_409_data = cls(
            deleteable=deleteable,
            references=references,
        )

        delete_cash_discount_response_409_data.additional_properties = d
        return delete_cash_discount_response_409_data

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
