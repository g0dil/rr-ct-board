from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomModuleDataValue")


@_attrs_define
class CustomModuleDataValue:
    """
    Attributes:
        data_category_id (int):
        id (int):
        domain_id (int | Unset):
        domain_type (str | Unset):
        value (str | Unset):
    """

    data_category_id: int
    id: int
    domain_id: int | Unset = UNSET
    domain_type: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_category_id = self.data_category_id

        id = self.id

        domain_id = self.domain_id

        domain_type = self.domain_type

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataCategoryId": data_category_id,
                "id": id,
            }
        )
        if domain_id is not UNSET:
            field_dict["domainId"] = domain_id
        if domain_type is not UNSET:
            field_dict["domainType"] = domain_type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_category_id = d.pop("dataCategoryId")

        id = d.pop("id")

        domain_id = d.pop("domainId", UNSET)

        domain_type = d.pop("domainType", UNSET)

        value = d.pop("value", UNSET)

        custom_module_data_value = cls(
            data_category_id=data_category_id,
            id=id,
            domain_id=domain_id,
            domain_type=domain_type,
            value=value,
        )

        custom_module_data_value.additional_properties = d
        return custom_module_data_value

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
