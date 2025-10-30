from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFilesDomainTypeDomainIdentifierLinkBody")


@_attrs_define
class PostFilesDomainTypeDomainIdentifierLinkBody:
    """
    Attributes:
        name (None | str):  Example: Example Link.
        security_level_id (int | None | Unset):  Example: 2.
        url (str | Unset):  Example: https://www.example.com.
    """

    name: None | str
    security_level_id: int | None | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str
        name = self.name

        security_level_id: int | None | Unset
        if isinstance(self.security_level_id, Unset):
            security_level_id = UNSET
        else:
            security_level_id = self.security_level_id

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if security_level_id is not UNSET:
            field_dict["securityLevelId"] = security_level_id
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_security_level_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        security_level_id = _parse_security_level_id(d.pop("securityLevelId", UNSET))

        url = d.pop("url", UNSET)

        post_files_domain_type_domain_identifier_link_body = cls(
            name=name,
            security_level_id=security_level_id,
            url=url,
        )

        post_files_domain_type_domain_identifier_link_body.additional_properties = d
        return post_files_domain_type_domain_identifier_link_body

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
