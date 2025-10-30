from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgeGroupUpdate")


@_attrs_define
class AgeGroupUpdate:
    """
    Attributes:
        end (int):  Example: 5.
        name (str):  Example: 3-5.
        sort_key (int):  Example: 3.
        start (int):  Example: 3.
        id (int):  Example: 10.
    """

    end: int
    name: str
    sort_key: int
    start: int
    id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end

        name = self.name

        sort_key = self.sort_key

        start = self.start

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "name": name,
                "sortKey": sort_key,
                "start": start,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end = d.pop("end")

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        start = d.pop("start")

        id = d.pop("id")

        age_group_update = cls(
            end=end,
            name=name,
            sort_key=sort_key,
            start=start,
            id=id,
        )

        age_group_update.additional_properties = d
        return age_group_update

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
