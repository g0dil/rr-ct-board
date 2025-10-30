from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_tags_domain_type_domain_id_response_200_data_item import (
        GetTagsDomainTypeDomainIdResponse200DataItem,
    )
    from ..models.get_tags_domain_type_domain_id_response_200_meta import (
        GetTagsDomainTypeDomainIdResponse200Meta,
    )


T = TypeVar("T", bound="GetTagsDomainTypeDomainIdResponse200")


@_attrs_define
class GetTagsDomainTypeDomainIdResponse200:
    """
    Attributes:
        data (list[GetTagsDomainTypeDomainIdResponse200DataItem] | Unset):
        meta (GetTagsDomainTypeDomainIdResponse200Meta | Unset):
    """

    data: list[GetTagsDomainTypeDomainIdResponse200DataItem] | Unset = UNSET
    meta: GetTagsDomainTypeDomainIdResponse200Meta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_tags_domain_type_domain_id_response_200_data_item import (
            GetTagsDomainTypeDomainIdResponse200DataItem,
        )
        from ..models.get_tags_domain_type_domain_id_response_200_meta import (
            GetTagsDomainTypeDomainIdResponse200Meta,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = GetTagsDomainTypeDomainIdResponse200DataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        _meta = d.pop("meta", UNSET)
        meta: GetTagsDomainTypeDomainIdResponse200Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GetTagsDomainTypeDomainIdResponse200Meta.from_dict(_meta)

        get_tags_domain_type_domain_id_response_200 = cls(
            data=data,
            meta=meta,
        )

        get_tags_domain_type_domain_id_response_200.additional_properties = d
        return get_tags_domain_type_domain_id_response_200

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
