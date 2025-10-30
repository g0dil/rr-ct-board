from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_entity_mapping_body_status import UpdateEntityMappingBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEntityMappingBody")


@_attrs_define
class UpdateEntityMappingBody:
    """
    Attributes:
        last_synced_date (datetime.datetime): DateTime of Last Synchronisation in Zulu Format Example:
            2020-04-21T22:00:00Z.
        source_entity_id (None | str): Identifier of Synchronisation Source Example: 2.
        status (UpdateEntityMappingBodyStatus): Status of Entity Mapping Example: synced.
        domain_id (None | str | Unset): Domain Id of ChurchTools Entity Example: 1.
        domain_type (str | Unset): ChurchTools Domain Type Example: person.
        scope (None | str | Unset): scope key identifying the context of the entity mapping
        source_id (int | Unset): Id of Source Example: 2.
    """

    last_synced_date: datetime.datetime
    source_entity_id: None | str
    status: UpdateEntityMappingBodyStatus
    domain_id: None | str | Unset = UNSET
    domain_type: str | Unset = UNSET
    scope: None | str | Unset = UNSET
    source_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_synced_date = self.last_synced_date.isoformat()

        source_entity_id: None | str
        source_entity_id = self.source_entity_id

        status = self.status.value

        domain_id: None | str | Unset
        if isinstance(self.domain_id, Unset):
            domain_id = UNSET
        else:
            domain_id = self.domain_id

        domain_type = self.domain_type

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        source_id = self.source_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastSyncedDate": last_synced_date,
                "sourceEntityId": source_entity_id,
                "status": status,
            }
        )
        if domain_id is not UNSET:
            field_dict["domainId"] = domain_id
        if domain_type is not UNSET:
            field_dict["domainType"] = domain_type
        if scope is not UNSET:
            field_dict["scope"] = scope
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_synced_date = isoparse(d.pop("lastSyncedDate"))

        def _parse_source_entity_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_entity_id = _parse_source_entity_id(d.pop("sourceEntityId"))

        status = UpdateEntityMappingBodyStatus(d.pop("status"))

        def _parse_domain_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain_id = _parse_domain_id(d.pop("domainId", UNSET))

        domain_type = d.pop("domainType", UNSET)

        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        source_id = d.pop("sourceId", UNSET)

        update_entity_mapping_body = cls(
            last_synced_date=last_synced_date,
            source_entity_id=source_entity_id,
            status=status,
            domain_id=domain_id,
            domain_type=domain_type,
            scope=scope,
            source_id=source_id,
        )

        update_entity_mapping_body.additional_properties = d
        return update_entity_mapping_body

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
