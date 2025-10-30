from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_sync_mapping_body_status import CreateSyncMappingBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSyncMappingBody")


@_attrs_define
class CreateSyncMappingBody:
    """
    Attributes:
        domain_id (None | str): Identifier of ChurchTools Entity Example: 1.
        domain_type (str): ChurchTools Domain Type Example: person.
        last_synced_date (datetime.datetime | None): DateTime of Last Synchronisation in Zulu Format Example:
            2020-04-21T22:00:00Z.
        source_entity_id (None | str): Identifier of Entity in Source System Example: 4.
        source_id (int): Identifier of Synchronisation Source Example: 2.
        status (CreateSyncMappingBodyStatus): Status of Entity Mapping Example: synced.
        scope (None | str | Unset): scope key identifying the context of the entity mapping
    """

    domain_id: None | str
    domain_type: str
    last_synced_date: datetime.datetime | None
    source_entity_id: None | str
    source_id: int
    status: CreateSyncMappingBodyStatus
    scope: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_id: None | str
        domain_id = self.domain_id

        domain_type = self.domain_type

        last_synced_date: None | str
        if isinstance(self.last_synced_date, datetime.datetime):
            last_synced_date = self.last_synced_date.isoformat()
        else:
            last_synced_date = self.last_synced_date

        source_entity_id: None | str
        source_entity_id = self.source_entity_id

        source_id = self.source_id

        status = self.status.value

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainId": domain_id,
                "domainType": domain_type,
                "lastSyncedDate": last_synced_date,
                "sourceEntityId": source_entity_id,
                "sourceId": source_id,
                "status": status,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_domain_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain_id = _parse_domain_id(d.pop("domainId"))

        domain_type = d.pop("domainType")

        def _parse_last_synced_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_date_type_0 = isoparse(data)

                return last_synced_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None, data)

        last_synced_date = _parse_last_synced_date(d.pop("lastSyncedDate"))

        def _parse_source_entity_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_entity_id = _parse_source_entity_id(d.pop("sourceEntityId"))

        source_id = d.pop("sourceId")

        status = CreateSyncMappingBodyStatus(d.pop("status"))

        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        create_sync_mapping_body = cls(
            domain_id=domain_id,
            domain_type=domain_type,
            last_synced_date=last_synced_date,
            source_entity_id=source_entity_id,
            source_id=source_id,
            status=status,
            scope=scope,
        )

        create_sync_mapping_body.additional_properties = d
        return create_sync_mapping_body

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
