from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_status_name import GroupStatusName

T = TypeVar("T", bound="GroupStatus")


@_attrs_define
class GroupStatus:
    """
    Attributes:
        id (int):  Example: 1.
        name (GroupStatusName):  Example: active.
        name_translated (str):  Example: Aktiv.
        sort_key (int):  Example: 1.
    """

    id: int
    name: GroupStatusName
    name_translated: str
    sort_key: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name.value

        name_translated = self.name_translated

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "nameTranslated": name_translated,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = GroupStatusName(d.pop("name"))

        name_translated = d.pop("nameTranslated")

        sort_key = d.pop("sortKey")

        group_status = cls(
            id=id,
            name=name,
            name_translated=name_translated,
            sort_key=sort_key,
        )

        group_status.additional_properties = d
        return group_status

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
