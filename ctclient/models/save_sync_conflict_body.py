from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.save_sync_conflict_body_type import SaveSyncConflictBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.save_sync_conflict_body_data_item import SaveSyncConflictBodyDataItem


T = TypeVar("T", bound="SaveSyncConflictBody")


@_attrs_define
class SaveSyncConflictBody:
    """
    Attributes:
        entity_mapping_id (int): Entity Mapping Id Example: 1.
        job_id (str): Job Identifier (usually GUID) Example: 7E31C399-91B1-4148-BFDD-6C05B557A25C.
        type_ (SaveSyncConflictBodyType): Type of Conflict Example: create.
        data (list[SaveSyncConflictBodyDataItem] | Unset):
    """

    entity_mapping_id: int
    job_id: str
    type_: SaveSyncConflictBodyType
    data: list[SaveSyncConflictBodyDataItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_mapping_id = self.entity_mapping_id

        job_id = self.job_id

        type_ = self.type_.value

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entityMappingId": entity_mapping_id,
                "jobId": job_id,
                "type": type_,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.save_sync_conflict_body_data_item import (
            SaveSyncConflictBodyDataItem,
        )

        d = dict(src_dict)
        entity_mapping_id = d.pop("entityMappingId")

        job_id = d.pop("jobId")

        type_ = SaveSyncConflictBodyType(d.pop("type"))

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = SaveSyncConflictBodyDataItem.from_dict(data_item_data)

            data.append(data_item)

        save_sync_conflict_body = cls(
            entity_mapping_id=entity_mapping_id,
            job_id=job_id,
            type_=type_,
            data=data,
        )

        save_sync_conflict_body.additional_properties = d
        return save_sync_conflict_body

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
