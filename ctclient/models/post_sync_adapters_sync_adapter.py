from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSyncAdaptersSyncAdapter")


@_attrs_define
class PostSyncAdaptersSyncAdapter:
    """
    Attributes:
        name (str | Unset):  Example: churchtools.
        token (str | Unset):  Example: kfghsjdlkfigblszurglizeifuz4.
        url (str | Unset):  Example: http://localhost:8090.
    """

    name: str | Unset = UNSET
    token: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        token = self.token

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if token is not UNSET:
            field_dict["token"] = token
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        token = d.pop("token", UNSET)

        url = d.pop("url", UNSET)

        post_sync_adapters_sync_adapter = cls(
            name=name,
            token=token,
            url=url,
        )

        post_sync_adapters_sync_adapter.additional_properties = d
        return post_sync_adapters_sync_adapter

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
