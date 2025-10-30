from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linking_open_graph_data_type_0_music_album import (
        LinkingOpenGraphDataType0MusicAlbum,
    )
    from ..models.linking_open_graph_data_type_0_music_songs_item import (
        LinkingOpenGraphDataType0MusicSongsItem,
    )


T = TypeVar("T", bound="LinkingOpenGraphDataType0Music")


@_attrs_define
class LinkingOpenGraphDataType0Music:
    """
    Attributes:
        album (LinkingOpenGraphDataType0MusicAlbum | Unset):
        creators (list[str] | Unset): The creators of the music.
        duration (int | Unset): The duration of the music in seconds.
        musicians (list[str] | Unset): The musicians involved in the music.
        release_date (datetime.datetime | Unset): The release date of the music.
        songs (list[LinkingOpenGraphDataType0MusicSongsItem] | Unset):
    """

    album: LinkingOpenGraphDataType0MusicAlbum | Unset = UNSET
    creators: list[str] | Unset = UNSET
    duration: int | Unset = UNSET
    musicians: list[str] | Unset = UNSET
    release_date: datetime.datetime | Unset = UNSET
    songs: list[LinkingOpenGraphDataType0MusicSongsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        album: dict[str, Any] | Unset = UNSET
        if not isinstance(self.album, Unset):
            album = self.album.to_dict()

        creators: list[str] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = self.creators

        duration = self.duration

        musicians: list[str] | Unset = UNSET
        if not isinstance(self.musicians, Unset):
            musicians = self.musicians

        release_date: str | Unset = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        songs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.songs, Unset):
            songs = []
            for songs_item_data in self.songs:
                songs_item = songs_item_data.to_dict()
                songs.append(songs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if album is not UNSET:
            field_dict["album"] = album
        if creators is not UNSET:
            field_dict["creators"] = creators
        if duration is not UNSET:
            field_dict["duration"] = duration
        if musicians is not UNSET:
            field_dict["musicians"] = musicians
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if songs is not UNSET:
            field_dict["songs"] = songs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linking_open_graph_data_type_0_music_album import (
            LinkingOpenGraphDataType0MusicAlbum,
        )
        from ..models.linking_open_graph_data_type_0_music_songs_item import (
            LinkingOpenGraphDataType0MusicSongsItem,
        )

        d = dict(src_dict)
        _album = d.pop("album", UNSET)
        album: LinkingOpenGraphDataType0MusicAlbum | Unset
        if isinstance(_album, Unset):
            album = UNSET
        else:
            album = LinkingOpenGraphDataType0MusicAlbum.from_dict(_album)

        creators = cast(list[str], d.pop("creators", UNSET))

        duration = d.pop("duration", UNSET)

        musicians = cast(list[str], d.pop("musicians", UNSET))

        _release_date = d.pop("releaseDate", UNSET)
        release_date: datetime.datetime | Unset
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date)

        songs = []
        _songs = d.pop("songs", UNSET)
        for songs_item_data in _songs or []:
            songs_item = LinkingOpenGraphDataType0MusicSongsItem.from_dict(
                songs_item_data
            )

            songs.append(songs_item)

        linking_open_graph_data_type_0_music = cls(
            album=album,
            creators=creators,
            duration=duration,
            musicians=musicians,
            release_date=release_date,
            songs=songs,
        )

        linking_open_graph_data_type_0_music.additional_properties = d
        return linking_open_graph_data_type_0_music

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
