from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesBodyPropertyMappingsMasterToESItem",
)


@_attrs_define
class PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdPropertiesBodyPropertyMappingsMasterToESItem:
    """
    Attributes:
        field_mapping_id (int):
        from_ (str):
        from_filter (str):
        system (str):
        to (str):
        to_filter (str):
    """

    field_mapping_id: int
    from_: str
    from_filter: str
    system: str
    to: str
    to_filter: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_mapping_id = self.field_mapping_id

        from_ = self.from_

        from_filter = self.from_filter

        system = self.system

        to = self.to

        to_filter = self.to_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldMappingId": field_mapping_id,
                "from": from_,
                "fromFilter": from_filter,
                "system": system,
                "to": to,
                "toFilter": to_filter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_mapping_id = d.pop("fieldMappingId")

        from_ = d.pop("from")

        from_filter = d.pop("fromFilter")

        system = d.pop("system")

        to = d.pop("to")

        to_filter = d.pop("toFilter")

        put_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_body_property_mappings_master_to_es_item = cls(
            field_mapping_id=field_mapping_id,
            from_=from_,
            from_filter=from_filter,
            system=system,
            to=to,
            to_filter=to_filter,
        )

        put_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_body_property_mappings_master_to_es_item.additional_properties = d
        return put_sync_externalsystems_external_system_id_jobconfigs_job_id_properties_body_property_mappings_master_to_es_item

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
