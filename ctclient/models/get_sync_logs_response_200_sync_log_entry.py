from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sync_logs_response_200_sync_log_entry_job import (
        GetSyncLogsResponse200SyncLogEntryJob,
    )
    from ..models.get_sync_logs_response_200_sync_log_entry_message_args import (
        GetSyncLogsResponse200SyncLogEntryMessageArgs,
    )


T = TypeVar("T", bound="GetSyncLogsResponse200SyncLogEntry")


@_attrs_define
class GetSyncLogsResponse200SyncLogEntry:
    """Log entry during a sync execution.

    Attributes:
        date (datetime.datetime):
        domain_id (str):
        domain_type (str):
        id (int):
        is_dry_run (bool):
        job (GetSyncLogsResponse200SyncLogEntryJob):
        level (str):
        message_i18_n (str):
        source_entity_id (str):
        system (str):
        type_ (str):
        message_args (GetSyncLogsResponse200SyncLogEntryMessageArgs | Unset):
    """

    date: datetime.datetime
    domain_id: str
    domain_type: str
    id: int
    is_dry_run: bool
    job: GetSyncLogsResponse200SyncLogEntryJob
    level: str
    message_i18_n: str
    source_entity_id: str
    system: str
    type_: str
    message_args: GetSyncLogsResponse200SyncLogEntryMessageArgs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        domain_id = self.domain_id

        domain_type = self.domain_type

        id = self.id

        is_dry_run = self.is_dry_run

        job = self.job.to_dict()

        level = self.level

        message_i18_n = self.message_i18_n

        source_entity_id = self.source_entity_id

        system = self.system

        type_ = self.type_

        message_args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message_args, Unset):
            message_args = self.message_args.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "domainId": domain_id,
                "domainType": domain_type,
                "id": id,
                "isDryRun": is_dry_run,
                "job": job,
                "level": level,
                "messageI18n": message_i18_n,
                "sourceEntityId": source_entity_id,
                "system": system,
                "type": type_,
            }
        )
        if message_args is not UNSET:
            field_dict["messageArgs"] = message_args

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sync_logs_response_200_sync_log_entry_job import (
            GetSyncLogsResponse200SyncLogEntryJob,
        )
        from ..models.get_sync_logs_response_200_sync_log_entry_message_args import (
            GetSyncLogsResponse200SyncLogEntryMessageArgs,
        )

        d = dict(src_dict)
        date = isoparse(d.pop("date"))

        domain_id = d.pop("domainId")

        domain_type = d.pop("domainType")

        id = d.pop("id")

        is_dry_run = d.pop("isDryRun")

        job = GetSyncLogsResponse200SyncLogEntryJob.from_dict(d.pop("job"))

        level = d.pop("level")

        message_i18_n = d.pop("messageI18n")

        source_entity_id = d.pop("sourceEntityId")

        system = d.pop("system")

        type_ = d.pop("type")

        _message_args = d.pop("messageArgs", UNSET)
        message_args: GetSyncLogsResponse200SyncLogEntryMessageArgs | Unset
        if isinstance(_message_args, Unset):
            message_args = UNSET
        else:
            message_args = GetSyncLogsResponse200SyncLogEntryMessageArgs.from_dict(
                _message_args
            )

        get_sync_logs_response_200_sync_log_entry = cls(
            date=date,
            domain_id=domain_id,
            domain_type=domain_type,
            id=id,
            is_dry_run=is_dry_run,
            job=job,
            level=level,
            message_i18_n=message_i18_n,
            source_entity_id=source_entity_id,
            system=system,
            type_=type_,
            message_args=message_args,
        )

        get_sync_logs_response_200_sync_log_entry.additional_properties = d
        return get_sync_logs_response_200_sync_log_entry

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
