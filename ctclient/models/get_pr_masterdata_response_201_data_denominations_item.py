from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetPRMasterdataResponse201DataDenominationsItem")


@_attrs_define
class GetPRMasterdataResponse201DataDenominationsItem:
    """Denomination of a church

    Attributes:
        key (str):  Example: baptist.
        name (str):  Example: Baptist.
        name_translated (str):  Example: Baptisten.
    """

    key: str
    name: str
    name_translated: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        name_translated = self.name_translated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "nameTranslated": name_translated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        name_translated = d.pop("nameTranslated")

        get_pr_masterdata_response_201_data_denominations_item = cls(
            key=key,
            name=name,
            name_translated=name_translated,
        )

        get_pr_masterdata_response_201_data_denominations_item.additional_properties = d
        return get_pr_masterdata_response_201_data_denominations_item

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
