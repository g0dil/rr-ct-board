from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomModuleDataCategory")


@_attrs_define
class CustomModuleDataCategory:
    """
    Attributes:
        custom_module_id (int):
        description (str):
        name (str):
        shorty (str):
        id (int):
        schema (str | Unset):
        security_level_id (float | Unset):
    """

    custom_module_id: int
    description: str
    name: str
    shorty: str
    id: int
    schema: str | Unset = UNSET
    security_level_id: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_module_id = self.custom_module_id

        description = self.description

        name = self.name

        shorty = self.shorty

        id = self.id

        schema = self.schema

        security_level_id = self.security_level_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customModuleId": custom_module_id,
                "description": description,
                "name": name,
                "shorty": shorty,
                "id": id,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema
        if security_level_id is not UNSET:
            field_dict["securityLevelId"] = security_level_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_module_id = d.pop("customModuleId")

        description = d.pop("description")

        name = d.pop("name")

        shorty = d.pop("shorty")

        id = d.pop("id")

        schema = d.pop("schema", UNSET)

        security_level_id = d.pop("securityLevelId", UNSET)

        custom_module_data_category = cls(
            custom_module_id=custom_module_id,
            description=description,
            name=name,
            shorty=shorty,
            id=id,
            schema=schema,
            security_level_id=security_level_id,
        )

        custom_module_data_category.additional_properties = d
        return custom_module_data_category

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
