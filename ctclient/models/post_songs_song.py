from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSongsSong")


@_attrs_define
class PostSongsSong:
    """Song information

    Attributes:
        category_id (int):
        name (str):  Example: Hallelujah.
        author (None | str | Unset):  Example: Matthias Claudius.
        ccli (None | str | Unset):  Example: 123456789.
        copyright_ (None | str | Unset):  Example: Public Domain.
        should_practice (bool | Unset):  Default: False. Example: True.
    """

    category_id: int
    name: str
    author: None | str | Unset = UNSET
    ccli: None | str | Unset = UNSET
    copyright_: None | str | Unset = UNSET
    should_practice: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        name = self.name

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        ccli: None | str | Unset
        if isinstance(self.ccli, Unset):
            ccli = UNSET
        else:
            ccli = self.ccli

        copyright_: None | str | Unset
        if isinstance(self.copyright_, Unset):
            copyright_ = UNSET
        else:
            copyright_ = self.copyright_

        should_practice = self.should_practice

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "categoryId": category_id,
                "name": name,
            }
        )
        if author is not UNSET:
            field_dict["author"] = author
        if ccli is not UNSET:
            field_dict["ccli"] = ccli
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if should_practice is not UNSET:
            field_dict["shouldPractice"] = should_practice

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_id = d.pop("categoryId")

        name = d.pop("name")

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_ccli(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ccli = _parse_ccli(d.pop("ccli", UNSET))

        def _parse_copyright_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        copyright_ = _parse_copyright_(d.pop("copyright", UNSET))

        should_practice = d.pop("shouldPractice", UNSET)

        post_songs_song = cls(
            category_id=category_id,
            name=name,
            author=author,
            ccli=ccli,
            copyright_=copyright_,
            should_practice=should_practice,
        )

        post_songs_song.additional_properties = d
        return post_songs_song

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
