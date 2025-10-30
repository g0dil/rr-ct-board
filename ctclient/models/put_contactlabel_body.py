from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutContactlabelBody")


@_attrs_define
class PutContactlabelBody:
    """
    Attributes:
        is_default (bool): Indicator if label is new default.
        name (str): Name of Contact Label
        sort_key (int): SortKey
    """

    is_default: bool
    name: str
    sort_key: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_default = self.is_default

        name = self.name

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isDefault": is_default,
                "name": name,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_default = d.pop("isDefault")

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        put_contactlabel_body = cls(
            is_default=is_default,
            name=name,
            sort_key=sort_key,
        )

        put_contactlabel_body.additional_properties = d
        return put_contactlabel_body

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
