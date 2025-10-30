from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkJobRequestBody")


@_attrs_define
class BulkJobRequestBody:
    """
    Attributes:
        domain_object_identifiers (Any | Unset):
        job_data (Any | Unset): The data that should be used for the bulk job. Example for the setMaxMembers Job:
            {"maxMembers": 10}
    """

    domain_object_identifiers: Any | Unset = UNSET
    job_data: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_object_identifiers = self.domain_object_identifiers

        job_data = self.job_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_object_identifiers is not UNSET:
            field_dict["domainObjectIdentifiers"] = domain_object_identifiers
        if job_data is not UNSET:
            field_dict["jobData"] = job_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_object_identifiers = d.pop("domainObjectIdentifiers", UNSET)

        job_data = d.pop("jobData", UNSET)

        bulk_job_request_body = cls(
            domain_object_identifiers=domain_object_identifiers,
            job_data=job_data,
        )

        bulk_job_request_body.additional_properties = d
        return bulk_job_request_body

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
