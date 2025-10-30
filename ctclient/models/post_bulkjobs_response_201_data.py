from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostBulkjobsResponse201Data")


@_attrs_define
class PostBulkjobsResponse201Data:
    """
    Attributes:
        job_group (str | Unset):
        job_guid (str | Unset):
        number_of_queued_jobs (int | Unset):
    """

    job_group: str | Unset = UNSET
    job_guid: str | Unset = UNSET
    number_of_queued_jobs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_group = self.job_group

        job_guid = self.job_guid

        number_of_queued_jobs = self.number_of_queued_jobs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_group is not UNSET:
            field_dict["jobGroup"] = job_group
        if job_guid is not UNSET:
            field_dict["jobGuid"] = job_guid
        if number_of_queued_jobs is not UNSET:
            field_dict["numberOfQueuedJobs"] = number_of_queued_jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_group = d.pop("jobGroup", UNSET)

        job_guid = d.pop("jobGuid", UNSET)

        number_of_queued_jobs = d.pop("numberOfQueuedJobs", UNSET)

        post_bulkjobs_response_201_data = cls(
            job_group=job_group,
            job_guid=job_guid,
            number_of_queued_jobs=number_of_queued_jobs,
        )

        post_bulkjobs_response_201_data.additional_properties = d
        return post_bulkjobs_response_201_data

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
