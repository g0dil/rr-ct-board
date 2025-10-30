from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="GetSyncJobconfigsResponse200JobConfigurationReturnExternalSystem"
)


@_attrs_define
class GetSyncJobconfigsResponse200JobConfigurationReturnExternalSystem:
    """
    Attributes:
        adapter (str | Unset):
        id (int | Unset):
        job_configs_count (int | Unset):
        name (str | Unset):
    """

    adapter: str | Unset = UNSET
    id: int | Unset = UNSET
    job_configs_count: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adapter = self.adapter

        id = self.id

        job_configs_count = self.job_configs_count

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adapter is not UNSET:
            field_dict["adapter"] = adapter
        if id is not UNSET:
            field_dict["id"] = id
        if job_configs_count is not UNSET:
            field_dict["jobConfigsCount"] = job_configs_count
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        adapter = d.pop("adapter", UNSET)

        id = d.pop("id", UNSET)

        job_configs_count = d.pop("jobConfigsCount", UNSET)

        name = d.pop("name", UNSET)

        get_sync_jobconfigs_response_200_job_configuration_return_external_system = cls(
            adapter=adapter,
            id=id,
            job_configs_count=job_configs_count,
            name=name,
        )

        get_sync_jobconfigs_response_200_job_configuration_return_external_system.additional_properties = d
        return get_sync_jobconfigs_response_200_job_configuration_return_external_system

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
