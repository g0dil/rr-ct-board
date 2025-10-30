from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_body_es_item import (
        PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBodyEsItem,
    )
    from ..models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_body_master_item import (
        PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBodyMasterItem,
    )


T = TypeVar(
    "T", bound="PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBody"
)


@_attrs_define
class PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBody:
    """
    Attributes:
        es (list[PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBodyEsItem]):
        master (list[PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBodyMasterItem]):
    """

    es: list[PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBodyEsItem]
    master: list[
        PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBodyMasterItem
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
        from ..models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_body_es_item import (
            PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBodyEsItem,
        )
        from ..models.put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_body_master_item import (
            PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBodyMasterItem,
        )

        d = dict(src_dict)
        es = []
        _es = d.pop("es")
        for es_item_data in _es:
            es_item = PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBodyEsItem.from_dict(
                es_item_data
            )

            es.append(es_item)

        master = []
        _master = d.pop("master")
        for master_item_data in _master:
            master_item = PutSyncExternalsystemsExternalSystemIdJobconfigsJobIdFilterBodyMasterItem.from_dict(
                master_item_data
            )

            master.append(master_item)

        put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_body = cls(
            es=es,
            master=master,
        )

        put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_body.additional_properties = d
        return put_sync_externalsystems_external_system_id_jobconfigs_job_id_filter_body

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
