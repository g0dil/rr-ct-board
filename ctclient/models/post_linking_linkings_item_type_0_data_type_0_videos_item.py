from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_linking_linkings_item_type_0_data_type_0_videos_item_actors_item import (
        PostLinkingLinkingsItemType0DataType0VideosItemActorsItem,
    )


T = TypeVar("T", bound="PostLinkingLinkingsItemType0DataType0VideosItem")


@_attrs_define
class PostLinkingLinkingsItemType0DataType0VideosItem:
    """
    Example:
        {'actors': [], 'directors': ['John Doe'], 'duration': 120, 'height': 720, 'releaseDate': '2020-01-01T00:00:00Z',
            'secureUrl': 'https://secure.example.com/video.mp4', 'tags': ['example', 'video'], 'type': 'video/mp4', 'url':
            'https://example.com/video.mp4', 'width': 1280, 'writers': ['Jane Smith']}

    Attributes:
        actors (list[PostLinkingLinkingsItemType0DataType0VideosItemActorsItem] | Unset):
        directors (list[str] | Unset):
        duration (int | Unset): The duration of the video in seconds.
        height (int | Unset): The height of the video in pixels.
        release_date (datetime.datetime | Unset): The release date of the video.
        secure_url (str | Unset): The secure URL of the video.
        tags (list[str] | Unset): Tags associated with the video.
        type_ (str | Unset): The MIME type of the video.
        url (str | Unset): The URL of the video.
        width (int | Unset): The width of the video in pixels.
        writers (list[str] | Unset):
    """

    actors: list[PostLinkingLinkingsItemType0DataType0VideosItemActorsItem] | Unset = (
        UNSET
    )
    directors: list[str] | Unset = UNSET
    duration: int | Unset = UNSET
    height: int | Unset = UNSET
    release_date: datetime.datetime | Unset = UNSET
    secure_url: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    type_: str | Unset = UNSET
    url: str | Unset = UNSET
    width: int | Unset = UNSET
    writers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actors, Unset):
            actors = []
            for actors_item_data in self.actors:
                actors_item = actors_item_data.to_dict()
                actors.append(actors_item)

        directors: list[str] | Unset = UNSET
        if not isinstance(self.directors, Unset):
            directors = self.directors

        duration = self.duration

        height = self.height

        release_date: str | Unset = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        secure_url = self.secure_url

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        type_ = self.type_

        url = self.url

        width = self.width

        writers: list[str] | Unset = UNSET
        if not isinstance(self.writers, Unset):
            writers = self.writers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actors is not UNSET:
            field_dict["actors"] = actors
        if directors is not UNSET:
            field_dict["directors"] = directors
        if duration is not UNSET:
            field_dict["duration"] = duration
        if height is not UNSET:
            field_dict["height"] = height
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if secure_url is not UNSET:
            field_dict["secureUrl"] = secure_url
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url
        if width is not UNSET:
            field_dict["width"] = width
        if writers is not UNSET:
            field_dict["writers"] = writers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_linking_linkings_item_type_0_data_type_0_videos_item_actors_item import (
            PostLinkingLinkingsItemType0DataType0VideosItemActorsItem,
        )

        d = dict(src_dict)
        actors = []
        _actors = d.pop("actors", UNSET)
        for actors_item_data in _actors or []:
            actors_item = (
                PostLinkingLinkingsItemType0DataType0VideosItemActorsItem.from_dict(
                    actors_item_data
                )
            )

            actors.append(actors_item)

        directors = cast(list[str], d.pop("directors", UNSET))

        duration = d.pop("duration", UNSET)

        height = d.pop("height", UNSET)

        _release_date = d.pop("releaseDate", UNSET)
        release_date: datetime.datetime | Unset
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date)

        secure_url = d.pop("secureUrl", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        width = d.pop("width", UNSET)

        writers = cast(list[str], d.pop("writers", UNSET))

        post_linking_linkings_item_type_0_data_type_0_videos_item = cls(
            actors=actors,
            directors=directors,
            duration=duration,
            height=height,
            release_date=release_date,
            secure_url=secure_url,
            tags=tags,
            type_=type_,
            url=url,
            width=width,
            writers=writers,
        )

        post_linking_linkings_item_type_0_data_type_0_videos_item.additional_properties = d
        return post_linking_linkings_item_type_0_data_type_0_videos_item

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
