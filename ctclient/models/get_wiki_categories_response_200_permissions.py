from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWikiCategoriesResponse200Permissions")


@_attrs_define
class GetWikiCategoriesResponse200Permissions:
    """
    Attributes:
        edit_master_data (bool | Unset):
    """

    edit_master_data: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edit_master_data = self.edit_master_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edit_master_data is not UNSET:
            field_dict["editMasterData"] = edit_master_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        edit_master_data = d.pop("editMasterData", UNSET)

        get_wiki_categories_response_200_permissions = cls(
            edit_master_data=edit_master_data,
        )

        get_wiki_categories_response_200_permissions.additional_properties = d
        return get_wiki_categories_response_200_permissions

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
