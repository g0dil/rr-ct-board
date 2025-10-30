from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_external_system_access_header_values import (
        PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataExternalSystemAccessHeaderValues,
    )


T = TypeVar(
    "T",
    bound="PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataExternalSystem",
)


@_attrs_define
class PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataExternalSystem:
    """
    Attributes:
        access_header_values (PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataExternalSyst
            emAccessHeaderValues): Key Value Pairs that define the access to the external system
        adapter (str):
        name (str):
        id (int | Unset): Not necessary when creating a new external system
    """

    access_header_values: PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataExternalSystemAccessHeaderValues
    adapter: str
    name: str
    id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_header_values = self.access_header_values.to_dict()

        adapter = self.adapter

        name = self.name

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessHeaderValues": access_header_values,
                "adapter": adapter,
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_external_system_access_header_values import (
            PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataExternalSystemAccessHeaderValues,
        )

        d = dict(src_dict)
        access_header_values = PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesResponse200DataExternalSystemAccessHeaderValues.from_dict(
            d.pop("accessHeaderValues")
        )

        adapter = d.pop("adapter")

        name = d.pop("name")

        id = d.pop("id", UNSET)

        put_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_external_system = cls(
            access_header_values=access_header_values,
            adapter=adapter,
            name=name,
            id=id,
        )

        put_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_external_system.additional_properties = d
        return put_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_response_200_data_external_system

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
