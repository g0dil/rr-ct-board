from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JobGroupStatusJobs")


@_attrs_define
class JobGroupStatusJobs:
    """
    Attributes:
        buried (int): Number of Buried Jobs Example: 1.
        deleted (int): Number of Deleted Jobs (but still in Queue listed) Example: 1.
        pending (int): Number of Pending Jobs Example: 1.
        running (int): Number of Running Jobs Example: 1.
    """

    buried: int
    deleted: int
    pending: int
    running: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buried = self.buried

        deleted = self.deleted

        pending = self.pending

        running = self.running

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buried": buried,
                "deleted": deleted,
                "pending": pending,
                "running": running,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        buried = d.pop("buried")

        deleted = d.pop("deleted")

        pending = d.pop("pending")

        running = d.pop("running")

        job_group_status_jobs = cls(
            buried=buried,
            deleted=deleted,
            pending=pending,
            running=running,
        )

        job_group_status_jobs.additional_properties = d
        return job_group_status_jobs

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
