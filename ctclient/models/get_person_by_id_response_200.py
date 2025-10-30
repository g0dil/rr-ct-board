from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_person_by_id_response_200_data import GetPersonByIdResponse200Data


T = TypeVar("T", bound="GetPersonByIdResponse200")


@_attrs_define
class GetPersonByIdResponse200:
    """
    Attributes:
        data (GetPersonByIdResponse200Data | Unset): A person object includes all fields the logged in user may see
            depending on the security level. Additional DB fields, created by the admin, are also part of the response.
            Those fields have the same name as the column name.
    """

    data: GetPersonByIdResponse200Data | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_person_by_id_response_200_data import (
            GetPersonByIdResponse200Data,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: GetPersonByIdResponse200Data | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GetPersonByIdResponse200Data.from_dict(_data)

        get_person_by_id_response_200 = cls(
            data=data,
        )

        get_person_by_id_response_200.additional_properties = d
        return get_person_by_id_response_200

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
