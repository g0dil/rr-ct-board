from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.job_group_status_jobs import JobGroupStatusJobs


T = TypeVar("T", bound="JobGroupStatus")


@_attrs_define
class JobGroupStatus:
    """
    Attributes:
        jobs (JobGroupStatusJobs):
        name (str): Name of Job Group. `__single__` is For Jobs Which don't Belong to a Group Example:
            donation_receipt-1.
        total (int): Total Jobs in Queue of This Job Group Example: 4.
    """

    jobs: JobGroupStatusJobs
    name: str
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jobs = self.jobs.to_dict()

        name = self.name

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobs": jobs,
                "name": name,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_group_status_jobs import JobGroupStatusJobs

        d = dict(src_dict)
        jobs = JobGroupStatusJobs.from_dict(d.pop("jobs"))

        name = d.pop("name")

        total = d.pop("total")

        job_group_status = cls(
            jobs=jobs,
            name=name,
            total=total,
        )

        job_group_status.additional_properties = d
        return job_group_status

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
