from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonMasterDataGroupTypesItem")


@_attrs_define
class PersonMasterDataGroupTypesItem:
    """
    Attributes:
        name_plural_translated (str | Unset):  Example: Kleingruppen.
        name_translated (str | Unset):  Example: Kleingruppe.
    """

    name_plural_translated: str | Unset = UNSET
    name_translated: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_plural_translated = self.name_plural_translated

        name_translated = self.name_translated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_plural_translated is not UNSET:
            field_dict["namePluralTranslated"] = name_plural_translated
        if name_translated is not UNSET:
            field_dict["nameTranslated"] = name_translated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name_plural_translated = d.pop("namePluralTranslated", UNSET)

        name_translated = d.pop("nameTranslated", UNSET)

        person_master_data_group_types_item = cls(
            name_plural_translated=name_plural_translated,
            name_translated=name_translated,
        )

        person_master_data_group_types_item.additional_properties = d
        return person_master_data_group_types_item

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
