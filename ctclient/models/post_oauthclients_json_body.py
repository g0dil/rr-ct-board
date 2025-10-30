from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostOauthclientsJsonBody")


@_attrs_define
class PostOauthclientsJsonBody:
    """
    Attributes:
        is_confidential (bool | Unset):
        name (str | Unset):
        redirect_uri (str | Unset):
    """

    is_confidential: bool | Unset = UNSET
    name: str | Unset = UNSET
    redirect_uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_confidential = self.is_confidential

        name = self.name

        redirect_uri = self.redirect_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_confidential is not UNSET:
            field_dict["isConfidential"] = is_confidential
        if name is not UNSET:
            field_dict["name"] = name
        if redirect_uri is not UNSET:
            field_dict["redirectUri"] = redirect_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_confidential = d.pop("isConfidential", UNSET)

        name = d.pop("name", UNSET)

        redirect_uri = d.pop("redirectUri", UNSET)

        post_oauthclients_json_body = cls(
            is_confidential=is_confidential,
            name=name,
            redirect_uri=redirect_uri,
        )

        post_oauthclients_json_body.additional_properties = d
        return post_oauthclients_json_body

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
