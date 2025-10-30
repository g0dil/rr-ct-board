from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateNewStatusJsonBody")


@_attrs_define
class CreateNewStatusJsonBody:
    """
    Attributes:
        is_member (bool):
        name (str):
        shorty (str):
        is_searchable (bool | Unset):  Default: True.
        security_level_id (int | Unset):  Default: 1.
        sort_key (int | Unset):  Default: 10.
    """

    is_member: bool
    name: str
    shorty: str
    is_searchable: bool | Unset = True
    security_level_id: int | Unset = 1
    sort_key: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_member = self.is_member

        name = self.name

        shorty = self.shorty

        is_searchable = self.is_searchable

        security_level_id = self.security_level_id

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isMember": is_member,
                "name": name,
                "shorty": shorty,
            }
        )
        if is_searchable is not UNSET:
            field_dict["isSearchable"] = is_searchable
        if security_level_id is not UNSET:
            field_dict["securityLevelId"] = security_level_id
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_member = d.pop("isMember")

        name = d.pop("name")

        shorty = d.pop("shorty")

        is_searchable = d.pop("isSearchable", UNSET)

        security_level_id = d.pop("securityLevelId", UNSET)

        sort_key = d.pop("sortKey", UNSET)

        create_new_status_json_body = cls(
            is_member=is_member,
            name=name,
            shorty=shorty,
            is_searchable=is_searchable,
            security_level_id=security_level_id,
            sort_key=sort_key,
        )

        create_new_status_json_body.additional_properties = d
        return create_new_status_json_body

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
