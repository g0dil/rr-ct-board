from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_master_data_relationship_types_item_function_keys_item import (
    PersonMasterDataRelationshipTypesItemFunctionKeysItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonMasterDataRelationshipTypesItem")


@_attrs_define
class PersonMasterDataRelationshipTypesItem:
    """
    Attributes:
        degree_name_a (str):
        degree_name_b (str):
        id (int):
        include_in_export (bool):
        name (str):
        name_translated (str):
        security_level_id (int):
        sort_key (int):
        export_title (str | Unset):
        function_keys (list[PersonMasterDataRelationshipTypesItemFunctionKeysItem] | Unset):
    """

    degree_name_a: str
    degree_name_b: str
    id: int
    include_in_export: bool
    name: str
    name_translated: str
    security_level_id: int
    sort_key: int
    export_title: str | Unset = UNSET
    function_keys: (
        list[PersonMasterDataRelationshipTypesItemFunctionKeysItem] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        degree_name_a = self.degree_name_a

        degree_name_b = self.degree_name_b

        id = self.id

        include_in_export = self.include_in_export

        name = self.name

        name_translated = self.name_translated

        security_level_id = self.security_level_id

        sort_key = self.sort_key

        export_title = self.export_title

        function_keys: list[str] | Unset = UNSET
        if not isinstance(self.function_keys, Unset):
            function_keys = []
            for function_keys_item_data in self.function_keys:
                function_keys_item = function_keys_item_data.value
                function_keys.append(function_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "degreeNameA": degree_name_a,
                "degreeNameB": degree_name_b,
                "id": id,
                "includeInExport": include_in_export,
                "name": name,
                "nameTranslated": name_translated,
                "securityLevelId": security_level_id,
                "sortKey": sort_key,
            }
        )
        if export_title is not UNSET:
            field_dict["exportTitle"] = export_title
        if function_keys is not UNSET:
            field_dict["functionKeys"] = function_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        degree_name_a = d.pop("degreeNameA")

        degree_name_b = d.pop("degreeNameB")

        id = d.pop("id")

        include_in_export = d.pop("includeInExport")

        name = d.pop("name")

        name_translated = d.pop("nameTranslated")

        security_level_id = d.pop("securityLevelId")

        sort_key = d.pop("sortKey")

        export_title = d.pop("exportTitle", UNSET)

        function_keys = []
        _function_keys = d.pop("functionKeys", UNSET)
        for function_keys_item_data in _function_keys or []:
            function_keys_item = PersonMasterDataRelationshipTypesItemFunctionKeysItem(
                function_keys_item_data
            )

            function_keys.append(function_keys_item)

        person_master_data_relationship_types_item = cls(
            degree_name_a=degree_name_a,
            degree_name_b=degree_name_b,
            id=id,
            include_in_export=include_in_export,
            name=name,
            name_translated=name_translated,
            security_level_id=security_level_id,
            sort_key=sort_key,
            export_title=export_title,
            function_keys=function_keys,
        )

        person_master_data_relationship_types_item.additional_properties = d
        return person_master_data_relationship_types_item

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
