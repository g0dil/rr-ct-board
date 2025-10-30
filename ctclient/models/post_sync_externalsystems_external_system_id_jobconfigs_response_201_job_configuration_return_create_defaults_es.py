from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="PostSyncExternalsystemsExternalSystemIdJobconfigsResponse201JobConfigurationReturnCreateDefaultsES",
)


@_attrs_define
class PostSyncExternalsystemsExternalSystemIdJobconfigsResponse201JobConfigurationReturnCreateDefaultsES:
    """ """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        post_sync_externalsystems_external_system_id_jobconfigs_response_201_job_configuration_return_create_defaults_es = cls()

        post_sync_externalsystems_external_system_id_jobconfigs_response_201_job_configuration_return_create_defaults_es.additional_properties = d
        return post_sync_externalsystems_external_system_id_jobconfigs_response_201_job_configuration_return_create_defaults_es

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
