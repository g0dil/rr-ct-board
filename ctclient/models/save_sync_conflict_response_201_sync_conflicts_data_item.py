from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SaveSyncConflictResponse201SyncConflictsDataItem")


@_attrs_define
class SaveSyncConflictResponse201SyncConflictsDataItem:
    """A Conflict Can Have Multiple Key-Value Pairs as Additional Data

    Attributes:
        id (int | Unset):
        key (str | Unset):
        value (str | Unset):
    """

    id: int | Unset = UNSET
    key: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        save_sync_conflict_response_201_sync_conflicts_data_item = cls(
            id=id,
            key=key,
            value=value,
        )

        save_sync_conflict_response_201_sync_conflicts_data_item.additional_properties = d
        return save_sync_conflict_response_201_sync_conflicts_data_item

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
