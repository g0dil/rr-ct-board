from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_sync_field_mappings_body_property_mappings_es_to_master_item import (
        PutSyncFieldMappingsBodyPropertyMappingsESToMasterItem,
    )
    from ..models.put_sync_field_mappings_body_property_mappings_master_to_es_item import (
        PutSyncFieldMappingsBodyPropertyMappingsMasterToESItem,
    )


T = TypeVar("T", bound="PutSyncFieldMappingsBody")


@_attrs_define
class PutSyncFieldMappingsBody:
    """
    Attributes:
        property_mappings_es_to_master (list[PutSyncFieldMappingsBodyPropertyMappingsESToMasterItem] | Unset):
        property_mappings_master_to_es (list[PutSyncFieldMappingsBodyPropertyMappingsMasterToESItem] | Unset):
    """

    property_mappings_es_to_master: (
        list[PutSyncFieldMappingsBodyPropertyMappingsESToMasterItem] | Unset
    ) = UNSET
    property_mappings_master_to_es: (
        list[PutSyncFieldMappingsBodyPropertyMappingsMasterToESItem] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_mappings_es_to_master: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.property_mappings_es_to_master, Unset):
            property_mappings_es_to_master = []
            for (
                property_mappings_es_to_master_item_data
            ) in self.property_mappings_es_to_master:
                property_mappings_es_to_master_item = (
                    property_mappings_es_to_master_item_data.to_dict()
                )
                property_mappings_es_to_master.append(
                    property_mappings_es_to_master_item
                )

        property_mappings_master_to_es: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.property_mappings_master_to_es, Unset):
            property_mappings_master_to_es = []
            for (
                property_mappings_master_to_es_item_data
            ) in self.property_mappings_master_to_es:
                property_mappings_master_to_es_item = (
                    property_mappings_master_to_es_item_data.to_dict()
                )
                property_mappings_master_to_es.append(
                    property_mappings_master_to_es_item
                )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_mappings_es_to_master is not UNSET:
            field_dict["propertyMappingsESToMaster"] = property_mappings_es_to_master
        if property_mappings_master_to_es is not UNSET:
            field_dict["propertyMappingsMasterToES"] = property_mappings_master_to_es

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_sync_field_mappings_body_property_mappings_es_to_master_item import (
            PutSyncFieldMappingsBodyPropertyMappingsESToMasterItem,
        )
        from ..models.put_sync_field_mappings_body_property_mappings_master_to_es_item import (
            PutSyncFieldMappingsBodyPropertyMappingsMasterToESItem,
        )

        d = dict(src_dict)
        property_mappings_es_to_master = []
        _property_mappings_es_to_master = d.pop("propertyMappingsESToMaster", UNSET)
        for property_mappings_es_to_master_item_data in (
            _property_mappings_es_to_master or []
        ):
            property_mappings_es_to_master_item = (
                PutSyncFieldMappingsBodyPropertyMappingsESToMasterItem.from_dict(
                    property_mappings_es_to_master_item_data
                )
            )

            property_mappings_es_to_master.append(property_mappings_es_to_master_item)

        property_mappings_master_to_es = []
        _property_mappings_master_to_es = d.pop("propertyMappingsMasterToES", UNSET)
        for property_mappings_master_to_es_item_data in (
            _property_mappings_master_to_es or []
        ):
            property_mappings_master_to_es_item = (
                PutSyncFieldMappingsBodyPropertyMappingsMasterToESItem.from_dict(
                    property_mappings_master_to_es_item_data
                )
            )

            property_mappings_master_to_es.append(property_mappings_master_to_es_item)

        put_sync_field_mappings_body = cls(
            property_mappings_es_to_master=property_mappings_es_to_master,
            property_mappings_master_to_es=property_mappings_master_to_es,
        )

        put_sync_field_mappings_body.additional_properties = d
        return put_sync_field_mappings_body

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
