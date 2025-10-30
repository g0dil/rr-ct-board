from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPostLinkingsResponse200DataItemType0DataType0MusicAlbum")


@_attrs_define
class GetPostLinkingsResponse200DataItemType0DataType0MusicAlbum:
    """
    Attributes:
        disc (int | Unset):
        url (str | Unset): The URL of the album.
    """

    disc: int | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disc = self.disc

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disc is not UNSET:
            field_dict["disc"] = disc
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disc = d.pop("disc", UNSET)

        url = d.pop("url", UNSET)

        get_post_linkings_response_200_data_item_type_0_data_type_0_music_album = cls(
            disc=disc,
            url=url,
        )

        get_post_linkings_response_200_data_item_type_0_data_type_0_music_album.additional_properties = d
        return get_post_linkings_response_200_data_item_type_0_data_type_0_music_album

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
