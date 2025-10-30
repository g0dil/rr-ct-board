from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenGraphAudio")


@_attrs_define
class OpenGraphAudio:
    """
    Example:
        {'secureUrl': 'https://secure.example.com/audio.mp3', 'type': 'audio/mpeg', 'url':
            'https://example.com/audio.mp3'}

    Attributes:
        secure_url (str | Unset): The secure URL of the audio.
        type_ (str | Unset): The MIME type of the audio.
        url (str | Unset): The URL of the audio.
    """

    secure_url: str | Unset = UNSET
    type_: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secure_url = self.secure_url

        type_ = self.type_

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secure_url is not UNSET:
            field_dict["secureUrl"] = secure_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secure_url = d.pop("secureUrl", UNSET)

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        open_graph_audio = cls(
            secure_url=secure_url,
            type_=type_,
            url=url,
        )

        open_graph_audio.additional_properties = d
        return open_graph_audio

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
