from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_properties_property_mappings_es_to_master_item import (
        GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataPropertiesPropertyMappingsESToMasterItem,
    )
    from ..models.get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_properties_property_mappings_master_to_es_item import (
        GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataPropertiesPropertyMappingsMasterToESItem,
    )


T = TypeVar(
    "T",
    bound="GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataProperties",
)


@_attrs_define
class GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataProperties:
    """
    Attributes:
        property_mappings_es_to_master (list[GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200D
            ataPropertiesPropertyMappingsESToMasterItem]):
        property_mappings_master_to_es (list[GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200D
            ataPropertiesPropertyMappingsMasterToESItem]):
    """

    property_mappings_es_to_master: list[
        GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataPropertiesPropertyMappingsESToMasterItem
    ]
    property_mappings_master_to_es: list[
        GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataPropertiesPropertyMappingsMasterToESItem
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_mappings_es_to_master = []
        for (
            property_mappings_es_to_master_item_data
        ) in self.property_mappings_es_to_master:
            property_mappings_es_to_master_item = (
                property_mappings_es_to_master_item_data.to_dict()
            )
            property_mappings_es_to_master.append(property_mappings_es_to_master_item)

        property_mappings_master_to_es = []
        for (
            property_mappings_master_to_es_item_data
        ) in self.property_mappings_master_to_es:
            property_mappings_master_to_es_item = (
                property_mappings_master_to_es_item_data.to_dict()
            )
            property_mappings_master_to_es.append(property_mappings_master_to_es_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyMappingsESToMaster": property_mappings_es_to_master,
                "propertyMappingsMasterToES": property_mappings_master_to_es,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_properties_property_mappings_es_to_master_item import (
            GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataPropertiesPropertyMappingsESToMasterItem,
        )
        from ..models.get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_properties_property_mappings_master_to_es_item import (
            GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataPropertiesPropertyMappingsMasterToESItem,
        )

        d = dict(src_dict)
        property_mappings_es_to_master = []
        _property_mappings_es_to_master = d.pop("propertyMappingsESToMaster")
        for property_mappings_es_to_master_item_data in _property_mappings_es_to_master:
            property_mappings_es_to_master_item = GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataPropertiesPropertyMappingsESToMasterItem.from_dict(
                property_mappings_es_to_master_item_data
            )

            property_mappings_es_to_master.append(property_mappings_es_to_master_item)

        property_mappings_master_to_es = []
        _property_mappings_master_to_es = d.pop("propertyMappingsMasterToES")
        for property_mappings_master_to_es_item_data in _property_mappings_master_to_es:
            property_mappings_master_to_es_item = GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataPropertiesPropertyMappingsMasterToESItem.from_dict(
                property_mappings_master_to_es_item_data
            )

            property_mappings_master_to_es.append(property_mappings_master_to_es_item)

        get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_properties = cls(
            property_mappings_es_to_master=property_mappings_es_to_master,
            property_mappings_master_to_es=property_mappings_master_to_es,
        )

        get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_properties.additional_properties = d
        return get_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_properties

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
