from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_sync_conflict_response_200_sync_conflicts_type import (
    UpdateSyncConflictResponse200SyncConflictsType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_sync_conflict_response_200_sync_conflicts_data_item import (
        UpdateSyncConflictResponse200SyncConflictsDataItem,
    )
    from ..models.update_sync_conflict_response_200_sync_conflicts_meta import (
        UpdateSyncConflictResponse200SyncConflictsMeta,
    )


T = TypeVar("T", bound="UpdateSyncConflictResponse200SyncConflicts")


@_attrs_define
class UpdateSyncConflictResponse200SyncConflicts:
    """A sync conflict object holds information about the type of conflict, the corresponding source and the entity
    mapping.

        Attributes:
            data (list[UpdateSyncConflictResponse200SyncConflictsDataItem] | Unset): Array of relevant meta information
            entity_mapping_id (int | Unset): Entity Mapping Id Example: 1.
            id (int | Unset): Conflict Id Example: 1.
            job_id (str | Unset): Job Id, where conflict appeared Example: 7E31C399-91B1-4148-BFDD-6C05B557A25C.
            meta (UpdateSyncConflictResponse200SyncConflictsMeta | Unset):
            type_ (UpdateSyncConflictResponse200SyncConflictsType | Unset): Conflict Type Example: create.
    """

    data: list[UpdateSyncConflictResponse200SyncConflictsDataItem] | Unset = UNSET
    entity_mapping_id: int | Unset = UNSET
    id: int | Unset = UNSET
    job_id: str | Unset = UNSET
    meta: UpdateSyncConflictResponse200SyncConflictsMeta | Unset = UNSET
    type_: UpdateSyncConflictResponse200SyncConflictsType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        entity_mapping_id = self.entity_mapping_id

        id = self.id

        job_id = self.job_id

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if entity_mapping_id is not UNSET:
            field_dict["entityMappingId"] = entity_mapping_id
        if id is not UNSET:
            field_dict["id"] = id
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if meta is not UNSET:
            field_dict["meta"] = meta
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_sync_conflict_response_200_sync_conflicts_data_item import (
            UpdateSyncConflictResponse200SyncConflictsDataItem,
        )
        from ..models.update_sync_conflict_response_200_sync_conflicts_meta import (
            UpdateSyncConflictResponse200SyncConflictsMeta,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = UpdateSyncConflictResponse200SyncConflictsDataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        entity_mapping_id = d.pop("entityMappingId", UNSET)

        id = d.pop("id", UNSET)

        job_id = d.pop("jobId", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: UpdateSyncConflictResponse200SyncConflictsMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = UpdateSyncConflictResponse200SyncConflictsMeta.from_dict(_meta)

        _type_ = d.pop("type", UNSET)
        type_: UpdateSyncConflictResponse200SyncConflictsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UpdateSyncConflictResponse200SyncConflictsType(_type_)

        update_sync_conflict_response_200_sync_conflicts = cls(
            data=data,
            entity_mapping_id=entity_mapping_id,
            id=id,
            job_id=job_id,
            meta=meta,
            type_=type_,
        )

        update_sync_conflict_response_200_sync_conflicts.additional_properties = d
        return update_sync_conflict_response_200_sync_conflicts

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
