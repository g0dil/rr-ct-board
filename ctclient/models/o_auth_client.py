from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OAuthClient")


@_attrs_define
class OAuthClient:
    """
    Attributes:
        identifier (str):
        is_confidential (bool):
        name (str):
        redirect_uri (str):
    """

    identifier: str
    is_confidential: bool
    name: str
    redirect_uri: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        is_confidential = self.is_confidential

        name = self.name

        redirect_uri = self.redirect_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "isConfidential": is_confidential,
                "name": name,
                "redirectUri": redirect_uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier")

        is_confidential = d.pop("isConfidential")

        name = d.pop("name")

        redirect_uri = d.pop("redirectUri")

        o_auth_client = cls(
            identifier=identifier,
            is_confidential=is_confidential,
            name=name,
            redirect_uri=redirect_uri,
        )

        o_auth_client.additional_properties = d
        return o_auth_client

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
