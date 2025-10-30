from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_dynamicgroups_response_200_meta import (
        GetDynamicgroupsResponse200Meta,
    )


T = TypeVar("T", bound="GetDynamicgroupsResponse200")


@_attrs_define
class GetDynamicgroupsResponse200:
    """
    Attributes:
        data (list[int] | Unset):
        meta (GetDynamicgroupsResponse200Meta | Unset):
    """

    data: list[int] | Unset = UNSET
    meta: GetDynamicgroupsResponse200Meta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[int] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data

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
        from ..models.get_dynamicgroups_response_200_meta import (
            GetDynamicgroupsResponse200Meta,
        )

        d = dict(src_dict)
        data = cast(list[int], d.pop("data", UNSET))

        _meta = d.pop("meta", UNSET)
        meta: GetDynamicgroupsResponse200Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GetDynamicgroupsResponse200Meta.from_dict(_meta)

        get_dynamicgroups_response_200 = cls(
            data=data,
            meta=meta,
        )

        get_dynamicgroups_response_200.additional_properties = d
        return get_dynamicgroups_response_200

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
