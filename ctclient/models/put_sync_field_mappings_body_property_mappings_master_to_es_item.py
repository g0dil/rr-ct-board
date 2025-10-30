from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_sync_field_mappings_body_property_mappings_master_to_es_item_value_mapping import (
        PutSyncFieldMappingsBodyPropertyMappingsMasterToESItemValueMapping,
    )


T = TypeVar("T", bound="PutSyncFieldMappingsBodyPropertyMappingsMasterToESItem")


@_attrs_define
class PutSyncFieldMappingsBodyPropertyMappingsMasterToESItem:
    """
    Attributes:
        from_ (str | Unset):
        from_filter (str | Unset):
        others (list[Any] | Unset):
        to (str | Unset):
        to_filter (str | Unset):
        value_mapping (PutSyncFieldMappingsBodyPropertyMappingsMasterToESItemValueMapping | Unset):
    """

    from_: str | Unset = UNSET
    from_filter: str | Unset = UNSET
    others: list[Any] | Unset = UNSET
    to: str | Unset = UNSET
    to_filter: str | Unset = UNSET
    value_mapping: (
        PutSyncFieldMappingsBodyPropertyMappingsMasterToESItemValueMapping | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        from_filter = self.from_filter

        others: list[Any] | Unset = UNSET
        if not isinstance(self.others, Unset):
            others = self.others

        to = self.to

        to_filter = self.to_filter

        value_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_mapping, Unset):
            value_mapping = self.value_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if from_filter is not UNSET:
            field_dict["fromFilter"] = from_filter
        if others is not UNSET:
            field_dict["others"] = others
        if to is not UNSET:
            field_dict["to"] = to
        if to_filter is not UNSET:
            field_dict["toFilter"] = to_filter
        if value_mapping is not UNSET:
            field_dict["valueMapping"] = value_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_sync_field_mappings_body_property_mappings_master_to_es_item_value_mapping import (
            PutSyncFieldMappingsBodyPropertyMappingsMasterToESItemValueMapping,
        )

        d = dict(src_dict)
        from_ = d.pop("from", UNSET)

        from_filter = d.pop("fromFilter", UNSET)

        others = cast(list[Any], d.pop("others", UNSET))

        to = d.pop("to", UNSET)

        to_filter = d.pop("toFilter", UNSET)

        _value_mapping = d.pop("valueMapping", UNSET)
        value_mapping: (
            PutSyncFieldMappingsBodyPropertyMappingsMasterToESItemValueMapping | Unset
        )
        if isinstance(_value_mapping, Unset):
            value_mapping = UNSET
        else:
            value_mapping = PutSyncFieldMappingsBodyPropertyMappingsMasterToESItemValueMapping.from_dict(
                _value_mapping
            )

        put_sync_field_mappings_body_property_mappings_master_to_es_item = cls(
            from_=from_,
            from_filter=from_filter,
            others=others,
            to=to,
            to_filter=to_filter,
            value_mapping=value_mapping,
        )

        put_sync_field_mappings_body_property_mappings_master_to_es_item.additional_properties = d
        return put_sync_field_mappings_body_property_mappings_master_to_es_item

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
