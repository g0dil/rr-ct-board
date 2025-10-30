from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetJobsResponse200Job")


@_attrs_define
class GetJobsResponse200Job:
    """
    Attributes:
        created_date (str | Unset):
        domain_id (str | Unset):
        domain_type (str | Unset):
        identifier (str | Unset):
        modified_date (str | Unset):
        name (str | Unset):
        status (str | Unset):
    """

    created_date: str | Unset = UNSET
    domain_id: str | Unset = UNSET
    domain_type: str | Unset = UNSET
    identifier: str | Unset = UNSET
    modified_date: str | Unset = UNSET
    name: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_date = self.created_date

        domain_id = self.domain_id

        domain_type = self.domain_type

        identifier = self.identifier

        modified_date = self.modified_date

        name = self.name

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if domain_id is not UNSET:
            field_dict["domainId"] = domain_id
        if domain_type is not UNSET:
            field_dict["domainType"] = domain_type
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_date = d.pop("createdDate", UNSET)

        domain_id = d.pop("domainId", UNSET)

        domain_type = d.pop("domainType", UNSET)

        identifier = d.pop("identifier", UNSET)

        modified_date = d.pop("modifiedDate", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        get_jobs_response_200_job = cls(
            created_date=created_date,
            domain_id=domain_id,
            domain_type=domain_type,
            identifier=identifier,
            modified_date=modified_date,
            name=name,
            status=status,
        )

        get_jobs_response_200_job.additional_properties = d
        return get_jobs_response_200_job

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
