from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.post_sync_logs_body_logs_item_level import PostSyncLogsBodyLogsItemLevel
from ..models.post_sync_logs_body_logs_item_system import PostSyncLogsBodyLogsItemSystem
from ..models.post_sync_logs_body_logs_item_type import PostSyncLogsBodyLogsItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_sync_logs_body_logs_item_args import PostSyncLogsBodyLogsItemArgs
    from ..models.post_sync_logs_body_logs_item_changes_item import (
        PostSyncLogsBodyLogsItemChangesItem,
    )


T = TypeVar("T", bound="PostSyncLogsBodyLogsItem")


@_attrs_define
class PostSyncLogsBodyLogsItem:
    """
    Attributes:
        args (PostSyncLogsBodyLogsItemArgs): Arguments for Translation Key
        date (datetime.datetime):  Example: 2021-02-19T10:44:12Z.
        domain_id (None | str):
        domain_type (None | str):
        is_dry_run (bool):
        job_id (int):
        level (PostSyncLogsBodyLogsItemLevel):  Example: info.
        message_key (str): Translation Key
        source_entity_id (None | str):
        system (PostSyncLogsBodyLogsItemSystem):  Example: es.
        type_ (PostSyncLogsBodyLogsItemType):
        changes (list[PostSyncLogsBodyLogsItemChangesItem] | Unset):
    """

    args: PostSyncLogsBodyLogsItemArgs
    date: datetime.datetime
    domain_id: None | str
    domain_type: None | str
    is_dry_run: bool
    job_id: int
    level: PostSyncLogsBodyLogsItemLevel
    message_key: str
    source_entity_id: None | str
    system: PostSyncLogsBodyLogsItemSystem
    type_: PostSyncLogsBodyLogsItemType
    changes: list[PostSyncLogsBodyLogsItemChangesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args = self.args.to_dict()

        date = self.date.isoformat()

        domain_id: None | str
        domain_id = self.domain_id

        domain_type: None | str
        domain_type = self.domain_type

        is_dry_run = self.is_dry_run

        job_id = self.job_id

        level = self.level.value

        message_key = self.message_key

        source_entity_id: None | str
        source_entity_id = self.source_entity_id

        system = self.system.value

        type_ = self.type_.value

        changes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = []
            for changes_item_data in self.changes:
                changes_item = changes_item_data.to_dict()
                changes.append(changes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "args": args,
                "date": date,
                "domainId": domain_id,
                "domainType": domain_type,
                "isDryRun": is_dry_run,
                "jobId": job_id,
                "level": level,
                "messageKey": message_key,
                "sourceEntityId": source_entity_id,
                "system": system,
                "type": type_,
            }
        )
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_sync_logs_body_logs_item_args import (
            PostSyncLogsBodyLogsItemArgs,
        )
        from ..models.post_sync_logs_body_logs_item_changes_item import (
            PostSyncLogsBodyLogsItemChangesItem,
        )

        d = dict(src_dict)
        args = PostSyncLogsBodyLogsItemArgs.from_dict(d.pop("args"))

        date = isoparse(d.pop("date"))

        def _parse_domain_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain_id = _parse_domain_id(d.pop("domainId"))

        def _parse_domain_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        domain_type = _parse_domain_type(d.pop("domainType"))

        is_dry_run = d.pop("isDryRun")

        job_id = d.pop("jobId")

        level = PostSyncLogsBodyLogsItemLevel(d.pop("level"))

        message_key = d.pop("messageKey")

        def _parse_source_entity_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_entity_id = _parse_source_entity_id(d.pop("sourceEntityId"))

        system = PostSyncLogsBodyLogsItemSystem(d.pop("system"))

        type_ = PostSyncLogsBodyLogsItemType(d.pop("type"))

        changes = []
        _changes = d.pop("changes", UNSET)
        for changes_item_data in _changes or []:
            changes_item = PostSyncLogsBodyLogsItemChangesItem.from_dict(
                changes_item_data
            )

            changes.append(changes_item)

        post_sync_logs_body_logs_item = cls(
            args=args,
            date=date,
            domain_id=domain_id,
            domain_type=domain_type,
            is_dry_run=is_dry_run,
            job_id=job_id,
            level=level,
            message_key=message_key,
            source_entity_id=source_entity_id,
            system=system,
            type_=type_,
            changes=changes,
        )

        post_sync_logs_body_logs_item.additional_properties = d
        return post_sync_logs_body_logs_item

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
