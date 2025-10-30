from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateNewStatusResponse201Data")


@_attrs_define
class CreateNewStatusResponse201Data:
    """
    Attributes:
        id (int): ID of status
        is_member (bool): Flag if status is member of the church
        is_searchable (bool): Flag if that status is searchable
        name (str): Status name
        name_translated (str): Translated status name
        security_level_id (int): Only persons with that securitylevel can edit/select/delete that status
        shorty (str): Abbreviation of name.
        sort_key (int): Used to sort all statuses
    """

    id: int
    is_member: bool
    is_searchable: bool
    name: str
    name_translated: str
    security_level_id: int
    shorty: str
    sort_key: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_member = self.is_member

        is_searchable = self.is_searchable

        name = self.name

        name_translated = self.name_translated

        security_level_id = self.security_level_id

        shorty = self.shorty

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "isMember": is_member,
                "isSearchable": is_searchable,
                "name": name,
                "nameTranslated": name_translated,
                "securityLevelId": security_level_id,
                "shorty": shorty,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        is_member = d.pop("isMember")

        is_searchable = d.pop("isSearchable")

        name = d.pop("name")

        name_translated = d.pop("nameTranslated")

        security_level_id = d.pop("securityLevelId")

        shorty = d.pop("shorty")

        sort_key = d.pop("sortKey")

        create_new_status_response_201_data = cls(
            id=id,
            is_member=is_member,
            is_searchable=is_searchable,
            name=name,
            name_translated=name_translated,
            security_level_id=security_level_id,
            shorty=shorty,
            sort_key=sort_key,
        )

        create_new_status_response_201_data.additional_properties = d
        return create_new_status_response_201_data

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
