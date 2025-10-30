from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutStatusBody")


@_attrs_define
class PutStatusBody:
    """
    Example:
        {'isMember': True, 'isSearchable': True, 'name': 'Member', 'securityLevelId': 1, 'shorty': 'M', 'sortKey': 10}

    Attributes:
        is_member (bool):
        is_searchable (bool):
        name (str):
        security_level_id (int):
        shorty (str):
        sort_key (int):
    """

    is_member: bool
    is_searchable: bool
    name: str
    security_level_id: int
    shorty: str
    sort_key: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_member = self.is_member

        is_searchable = self.is_searchable

        name = self.name

        security_level_id = self.security_level_id

        shorty = self.shorty

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isMember": is_member,
                "isSearchable": is_searchable,
                "name": name,
                "securityLevelId": security_level_id,
                "shorty": shorty,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_member = d.pop("isMember")

        is_searchable = d.pop("isSearchable")

        name = d.pop("name")

        security_level_id = d.pop("securityLevelId")

        shorty = d.pop("shorty")

        sort_key = d.pop("sortKey")

        put_status_body = cls(
            is_member=is_member,
            is_searchable=is_searchable,
            name=name,
            security_level_id=security_level_id,
            shorty=shorty,
            sort_key=sort_key,
        )

        put_status_body.additional_properties = d
        return put_status_body

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
