from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkResult")


@_attrs_define
class BulkResult:
    """
    Attributes:
        guid (str | Unset):
        job_name (str | Unset):
        number_of_queued_jobs (int | Unset):
    """

    guid: str | Unset = UNSET
    job_name: str | Unset = UNSET
    number_of_queued_jobs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guid = self.guid

        job_name = self.job_name

        number_of_queued_jobs = self.number_of_queued_jobs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid is not UNSET:
            field_dict["guid"] = guid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if number_of_queued_jobs is not UNSET:
            field_dict["numberOfQueuedJobs"] = number_of_queued_jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        guid = d.pop("guid", UNSET)

        job_name = d.pop("jobName", UNSET)

        number_of_queued_jobs = d.pop("numberOfQueuedJobs", UNSET)

        bulk_result = cls(
            guid=guid,
            job_name=job_name,
            number_of_queued_jobs=number_of_queued_jobs,
        )

        bulk_result.additional_properties = d
        return bulk_result

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
