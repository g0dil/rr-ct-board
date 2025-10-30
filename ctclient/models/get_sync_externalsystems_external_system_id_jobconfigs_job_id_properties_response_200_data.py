from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_external_system import (
        GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataExternalSystem,
    )
    from ..models.get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_properties import (
        GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataProperties,
    )


T = TypeVar(
    "T",
    bound="GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200Data",
)


@_attrs_define
class GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200Data:
    """
    Attributes:
        domain_type (str):
        external_system (GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataExternalSystem):
        properties (GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataProperties):
    """

    domain_type: str
    external_system: GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataExternalSystem
    properties: GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataProperties
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_type = self.domain_type

        external_system = self.external_system.to_dict()

        properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainType": domain_type,
                "externalSystem": external_system,
                "properties": properties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_external_system import (
            GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataExternalSystem,
        )
        from ..models.get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_properties import (
            GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataProperties,
        )

        d = dict(src_dict)
        domain_type = d.pop("domainType")

        external_system = GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataExternalSystem.from_dict(
            d.pop("externalSystem")
        )

        properties = GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataProperties.from_dict(
            d.pop("properties")
        )

        get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data = cls(
            domain_type=domain_type,
            external_system=external_system,
            properties=properties,
        )

        get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data.additional_properties = d
        return get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data

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
