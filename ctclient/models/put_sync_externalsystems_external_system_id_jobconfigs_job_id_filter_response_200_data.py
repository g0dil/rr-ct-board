from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200_data_es_item import (
        PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataEsItem,
    )
    from ..models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200_data_master_item import (
        PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataMasterItem,
    )


T = TypeVar(
    "T",
    bound="PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200Data",
)


@_attrs_define
class PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200Data:
    """
    Attributes:
        es (list[PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataEsItem]):
        master (list[PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataMasterItem]):
    """

    es: list[
        PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataEsItem
    ]
    master: list[
        PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataMasterItem
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        es = []
        for es_item_data in self.es:
            es_item = es_item_data.to_dict()
            es.append(es_item)

        master = []
        for master_item_data in self.master:
            master_item = master_item_data.to_dict()
            master.append(master_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "es": es,
                "master": master,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200_data_es_item import (
            PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataEsItem,
        )
        from ..models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200_data_master_item import (
            PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataMasterItem,
        )

        d = dict(src_dict)
        es = []
        _es = d.pop("es")
        for es_item_data in _es:
            es_item = PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataEsItem.from_dict(
                es_item_data
            )

            es.append(es_item)

        master = []
        _master = d.pop("master")
        for master_item_data in _master:
            master_item = PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterResponse200DataMasterItem.from_dict(
                master_item_data
            )

            master.append(master_item)

        put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200_data = cls(
            es=es,
            master=master,
        )

        put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200_data.additional_properties = d
        return put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_response_200_data

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
