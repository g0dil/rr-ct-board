from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateNewCampusBody")


@_attrs_define
class CreateNewCampusBody:
    """
    Example:
        {'name': 'Stuttgart', 'shorty': 'S', 'sortKey': 10}

    Attributes:
        name (str):
        shorty (str):
        sort_key (int | Unset):  Default: 10.
    """

    name: str
    shorty: str
    sort_key: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        shorty = self.shorty

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "shorty": shorty,
            }
        )
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        shorty = d.pop("shorty")

        sort_key = d.pop("sortKey", UNSET)

        create_new_campus_body = cls(
            name=name,
            shorty=shorty,
            sort_key=sort_key,
        )

        create_new_campus_body.additional_properties = d
        return create_new_campus_body

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
