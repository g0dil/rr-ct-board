from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteTransactionPurposeResponse409DataReferencesItem")


@_attrs_define
class DeleteTransactionPurposeResponse409DataReferencesItem:
    """
    Example:
        {'blocksDeletion': False, 'columnName': 'account_id', 'count': 1, 'tableName': 'cf_transactions', 'type':
            'ENTRY'}

    Attributes:
        blocks_deletion (bool | Unset): Indicator if those references are blocking the deletion.
        column_name (str | Unset): Column name of the reference / foreign key.
        count (int | Unset): Number of references in that table.
        table_name (str | Unset): Table name, with reference / foreign key constraint.
        type_ (str | Unset): Type of reference. 'ENTRY' (entry links to this object) or 'REFERENCE' (this object has a
            foreign key to this table)
    """

    blocks_deletion: bool | Unset = UNSET
    column_name: str | Unset = UNSET
    count: int | Unset = UNSET
    table_name: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blocks_deletion = self.blocks_deletion

        column_name = self.column_name

        count = self.count

        table_name = self.table_name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blocks_deletion is not UNSET:
            field_dict["blocksDeletion"] = blocks_deletion
        if column_name is not UNSET:
            field_dict["columnName"] = column_name
        if count is not UNSET:
            field_dict["count"] = count
        if table_name is not UNSET:
            field_dict["tableName"] = table_name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blocks_deletion = d.pop("blocksDeletion", UNSET)

        column_name = d.pop("columnName", UNSET)

        count = d.pop("count", UNSET)

        table_name = d.pop("tableName", UNSET)

        type_ = d.pop("type", UNSET)

        delete_transaction_purpose_response_409_data_references_item = cls(
            blocks_deletion=blocks_deletion,
            column_name=column_name,
            count=count,
            table_name=table_name,
            type_=type_,
        )

        delete_transaction_purpose_response_409_data_references_item.additional_properties = d
        return delete_transaction_purpose_response_409_data_references_item

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
