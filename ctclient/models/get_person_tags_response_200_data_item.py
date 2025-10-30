from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_person_tags_response_200_data_item_color import (
    GetPersonTagsResponse200DataItemColor,
)

T = TypeVar("T", bound="GetPersonTagsResponse200DataItem")


@_attrs_define
class GetPersonTagsResponse200DataItem:
    """
    Attributes:
        color (GetPersonTagsResponse200DataItemColor): A color in ChurchTools
        description (str):
        id (int):
        name (str):
        modified_at (str):
        modified_by (int):
        modified_date (str):
        modified_pid (str):
    """

    color: GetPersonTagsResponse200DataItemColor
    description: str
    id: int
    name: str
    modified_at: str
    modified_by: int
    modified_date: str
    modified_pid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color.value

        description = self.description

        id = self.id

        name = self.name

        modified_at = self.modified_at

        modified_by = self.modified_by

        modified_date = self.modified_date

        modified_pid = self.modified_pid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "color": color,
                "description": description,
                "id": id,
                "name": name,
                "modifiedAt": modified_at,
                "modifiedBy": modified_by,
                "modifiedDate": modified_date,
                "modifiedPid": modified_pid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = GetPersonTagsResponse200DataItemColor(d.pop("color"))

        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        modified_at = d.pop("modifiedAt")

        modified_by = d.pop("modifiedBy")

        modified_date = d.pop("modifiedDate")

        modified_pid = d.pop("modifiedPid")

        get_person_tags_response_200_data_item = cls(
            color=color,
            description=description,
            id=id,
            name=name,
            modified_at=modified_at,
            modified_by=modified_by,
            modified_date=modified_date,
            modified_pid=modified_pid,
        )

        get_person_tags_response_200_data_item.additional_properties = d
        return get_person_tags_response_200_data_item

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
