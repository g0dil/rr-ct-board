from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sync_entity_mapping_status import SyncEntityMappingStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_entity_mapping_meta import SyncEntityMappingMeta


T = TypeVar("T", bound="SyncEntityMapping")


@_attrs_define
class SyncEntityMapping:
    """Mapping information between a ChurchTools entity and its corresponding entity in a third party system.

    Attributes:
        domain_id (str | Unset): ChurchTools Internal Domain Identifier
        domain_type (str | Unset): ChurchTools Domain Type
        id (int | Unset): ID of Entity Mapping Example: 1.
        last_synced_date (datetime.datetime | None | Unset): Date of Last Sync
        meta (SyncEntityMappingMeta | Unset):
        scope (None | str | Unset): scope key identifying the context of the entity mapping
        source_entity_id (str | Unset): Source Entity's Identifier
        source_id (int | Unset): Id of Source System Registered in ChurchTools Example: 1.
        status (SyncEntityMappingStatus | Unset): Status of Relationship Example: synced.
    """

    domain_id: str | Unset = UNSET
    domain_type: str | Unset = UNSET
    id: int | Unset = UNSET
    last_synced_date: datetime.datetime | None | Unset = UNSET
    meta: SyncEntityMappingMeta | Unset = UNSET
    scope: None | str | Unset = UNSET
    source_entity_id: str | Unset = UNSET
    source_id: int | Unset = UNSET
    status: SyncEntityMappingStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_id = self.domain_id

        domain_type = self.domain_type

        id = self.id

        last_synced_date: None | str | Unset
        if isinstance(self.last_synced_date, Unset):
            last_synced_date = UNSET
        elif isinstance(self.last_synced_date, datetime.datetime):
            last_synced_date = self.last_synced_date.isoformat()
        else:
            last_synced_date = self.last_synced_date

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        source_entity_id = self.source_entity_id

        source_id = self.source_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_id is not UNSET:
            field_dict["domainId"] = domain_id
        if domain_type is not UNSET:
            field_dict["domainType"] = domain_type
        if id is not UNSET:
            field_dict["id"] = id
        if last_synced_date is not UNSET:
            field_dict["lastSyncedDate"] = last_synced_date
        if meta is not UNSET:
            field_dict["meta"] = meta
        if scope is not UNSET:
            field_dict["scope"] = scope
        if source_entity_id is not UNSET:
            field_dict["sourceEntityId"] = source_entity_id
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_entity_mapping_meta import SyncEntityMappingMeta

        d = dict(src_dict)
        domain_id = d.pop("domainId", UNSET)

        domain_type = d.pop("domainType", UNSET)

        id = d.pop("id", UNSET)

        def _parse_last_synced_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_date_type_0 = isoparse(data)

                return last_synced_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_synced_date = _parse_last_synced_date(d.pop("lastSyncedDate", UNSET))

        _meta = d.pop("meta", UNSET)
        meta: SyncEntityMappingMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = SyncEntityMappingMeta.from_dict(_meta)

        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        source_entity_id = d.pop("sourceEntityId", UNSET)

        source_id = d.pop("sourceId", UNSET)

        _status = d.pop("status", UNSET)
        status: SyncEntityMappingStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SyncEntityMappingStatus(_status)

        sync_entity_mapping = cls(
            domain_id=domain_id,
            domain_type=domain_type,
            id=id,
            last_synced_date=last_synced_date,
            meta=meta,
            scope=scope,
            source_entity_id=source_entity_id,
            source_id=source_id,
            status=status,
        )

        sync_entity_mapping.additional_properties = d
        return sync_entity_mapping

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
