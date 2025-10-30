from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sync_log_entry_job_external_system import (
        SyncLogEntryJobExternalSystem,
    )


T = TypeVar("T", bound="SyncLogEntryJob")


@_attrs_define
class SyncLogEntryJob:
    """
    Attributes:
        external_system (SyncLogEntryJobExternalSystem):
        id (int):
        name (str):
    """

    external_system: SyncLogEntryJobExternalSystem
    id: int
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_system = self.external_system.to_dict()

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalSystem": external_system,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_log_entry_job_external_system import (
            SyncLogEntryJobExternalSystem,
        )

        d = dict(src_dict)
        external_system = SyncLogEntryJobExternalSystem.from_dict(
            d.pop("externalSystem")
        )

        id = d.pop("id")

        name = d.pop("name")

        sync_log_entry_job = cls(
            external_system=external_system,
            id=id,
            name=name,
        )

        sync_log_entry_job.additional_properties = d
        return sync_log_entry_job

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
