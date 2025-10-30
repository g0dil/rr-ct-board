from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200_data_es_item_values import (
        PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataEsItemValues,
    )


T = TypeVar(
    "T",
    bound="PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataEsItem",
)


@_attrs_define
class PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataEsItem:
    """
    Attributes:
        field (str):
        system (str):
        values (PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataEsItemValues):
    """

    field: str
    system: str
    values: PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataEsItemValues
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        system = self.system

        values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "system": system,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200_data_es_item_values import (
            PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataEsItemValues,
        )

        d = dict(src_dict)
        field = d.pop("field")

        system = d.pop("system")

        values = PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataEsItemValues.from_dict(
            d.pop("values")
        )

        put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200_data_es_item = cls(
            field=field,
            system=system,
            values=values,
        )

        put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200_data_es_item.additional_properties = d
        return put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200_data_es_item

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
