from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_new_campus_response_201_data import (
        CreateNewCampusResponse201Data,
    )
    from ..models.create_new_campus_response_201_meta import (
        CreateNewCampusResponse201Meta,
    )


T = TypeVar("T", bound="CreateNewCampusResponse201")


@_attrs_define
class CreateNewCampusResponse201:
    """
    Attributes:
        data (CreateNewCampusResponse201Data | Unset): Campus with possible address.
        meta (CreateNewCampusResponse201Meta | Unset):
    """

    data: CreateNewCampusResponse201Data | Unset = UNSET
    meta: CreateNewCampusResponse201Meta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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
        from ..models.create_new_campus_response_201_data import (
            CreateNewCampusResponse201Data,
        )
        from ..models.create_new_campus_response_201_meta import (
            CreateNewCampusResponse201Meta,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: CreateNewCampusResponse201Data | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CreateNewCampusResponse201Data.from_dict(_data)

        _meta = d.pop("meta", UNSET)
        meta: CreateNewCampusResponse201Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = CreateNewCampusResponse201Meta.from_dict(_meta)

        create_new_campus_response_201 = cls(
            data=data,
            meta=meta,
        )

        create_new_campus_response_201.additional_properties = d
        return create_new_campus_response_201

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
