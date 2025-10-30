from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_category_update_color import GroupCategoryUpdateColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupCategoryUpdate")


@_attrs_define
class GroupCategoryUpdate:
    """
    Attributes:
        color (GroupCategoryUpdateColor): A color in ChurchTools
        name (str):  Example: Gottesdienst.
        sort_key (int):  Example: 5.
        id (int):  Example: 4.
        description (None | str | Unset):  Example: Wir feiern Gottesdienst!.
    """

    color: GroupCategoryUpdateColor
    name: str
    sort_key: int
    id: int
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.value

        name = self.name

        sort_key = self.sort_key

        id = self.id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "name": name,
                "sortKey": sort_key,
                "id": id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = GroupCategoryUpdateColor(d.pop("color"))

        name = d.pop("name")

        sort_key = d.pop("sortKey")

        id = d.pop("id")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        group_category_update = cls(
            color=color,
            name=name,
            sort_key=sort_key,
            id=id,
            description=description,
        )

        group_category_update.additional_properties = d
        return group_category_update

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
