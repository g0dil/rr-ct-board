from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_article import (
        GetPostLinkingsResponse200DataItemType0DataType0Article,
    )
    from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_audios_item import (
        GetPostLinkingsResponse200DataItemType0DataType0AudiosItem,
    )
    from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_book import (
        GetPostLinkingsResponse200DataItemType0DataType0Book,
    )
    from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_images_item import (
        GetPostLinkingsResponse200DataItemType0DataType0ImagesItem,
    )
    from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_music import (
        GetPostLinkingsResponse200DataItemType0DataType0Music,
    )
    from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_profile import (
        GetPostLinkingsResponse200DataItemType0DataType0Profile,
    )
    from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_videos_item import (
        GetPostLinkingsResponse200DataItemType0DataType0VideosItem,
    )


T = TypeVar("T", bound="GetPostLinkingsResponse200DataItemType0DataType0")


@_attrs_define
class GetPostLinkingsResponse200DataItemType0DataType0:
    """
    Attributes:
        article (GetPostLinkingsResponse200DataItemType0DataType0Article | Unset):  Example: {'authors': ['John Doe',
            'Jane Smith'], 'expirationTime': '2021-01-01T00:00:00Z', 'modifiedTime': '2020-01-02T00:00:00Z',
            'publishedTime': '2020-01-01T00:00:00Z', 'section': 'News', 'tags': ['news', 'world']}.
        audios (list[GetPostLinkingsResponse200DataItemType0DataType0AudiosItem] | Unset):
        book (GetPostLinkingsResponse200DataItemType0DataType0Book | Unset):  Example: {'authors': ['John Doe', 'Jane
            Smith'], 'isbn': '123-4567890123', 'releaseDate': '2020-01-01T00:00:00Z', 'tags': ['fiction', 'bestseller']}.
        description (str | Unset): A brief description of the OpenGraph content.
        determiner (str | Unset): The determiner for the noun in the content.
        images (list[GetPostLinkingsResponse200DataItemType0DataType0ImagesItem] | Unset):
        locale (str | Unset): The locale of the OpenGraph object.
        locales_alternate (list[str] | Unset): Alternate locales available.
        music (GetPostLinkingsResponse200DataItemType0DataType0Music | Unset):
        profile (GetPostLinkingsResponse200DataItemType0DataType0Profile | Unset):  Example: {'firstName': 'John',
            'gender': 'male', 'lastName': 'Doe', 'username': 'johndoe'}.
        site_name (str | Unset): The site name of the OpenGraph object.
        title (str | Unset): The title of the OpenGraph object.
        type_ (str | Unset): The type of OpenGraph object.
        url (str | Unset): The URL of the OpenGraph object.
        videos (list[GetPostLinkingsResponse200DataItemType0DataType0VideosItem] | Unset):
    """

    article: GetPostLinkingsResponse200DataItemType0DataType0Article | Unset = UNSET
    audios: list[GetPostLinkingsResponse200DataItemType0DataType0AudiosItem] | Unset = (
        UNSET
    )
    book: GetPostLinkingsResponse200DataItemType0DataType0Book | Unset = UNSET
    description: str | Unset = UNSET
    determiner: str | Unset = UNSET
    images: list[GetPostLinkingsResponse200DataItemType0DataType0ImagesItem] | Unset = (
        UNSET
    )
    locale: str | Unset = UNSET
    locales_alternate: list[str] | Unset = UNSET
    music: GetPostLinkingsResponse200DataItemType0DataType0Music | Unset = UNSET
    profile: GetPostLinkingsResponse200DataItemType0DataType0Profile | Unset = UNSET
    site_name: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    url: str | Unset = UNSET
    videos: list[GetPostLinkingsResponse200DataItemType0DataType0VideosItem] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        article: dict[str, Any] | Unset = UNSET
        if not isinstance(self.article, Unset):
            article = self.article.to_dict()

        audios: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.audios, Unset):
            audios = []
            for audios_item_data in self.audios:
                audios_item = audios_item_data.to_dict()
                audios.append(audios_item)

        book: dict[str, Any] | Unset = UNSET
        if not isinstance(self.book, Unset):
            book = self.book.to_dict()

        description = self.description

        determiner = self.determiner

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        locale = self.locale

        locales_alternate: list[str] | Unset = UNSET
        if not isinstance(self.locales_alternate, Unset):
            locales_alternate = self.locales_alternate

        music: dict[str, Any] | Unset = UNSET
        if not isinstance(self.music, Unset):
            music = self.music.to_dict()

        profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        site_name = self.site_name

        title = self.title

        type_ = self.type_

        url = self.url

        videos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.videos, Unset):
            videos = []
            for videos_item_data in self.videos:
                videos_item = videos_item_data.to_dict()
                videos.append(videos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if article is not UNSET:
            field_dict["article"] = article
        if audios is not UNSET:
            field_dict["audios"] = audios
        if book is not UNSET:
            field_dict["book"] = book
        if description is not UNSET:
            field_dict["description"] = description
        if determiner is not UNSET:
            field_dict["determiner"] = determiner
        if images is not UNSET:
            field_dict["images"] = images
        if locale is not UNSET:
            field_dict["locale"] = locale
        if locales_alternate is not UNSET:
            field_dict["localesAlternate"] = locales_alternate
        if music is not UNSET:
            field_dict["music"] = music
        if profile is not UNSET:
            field_dict["profile"] = profile
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url
        if videos is not UNSET:
            field_dict["videos"] = videos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_article import (
            GetPostLinkingsResponse200DataItemType0DataType0Article,
        )
        from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_audios_item import (
            GetPostLinkingsResponse200DataItemType0DataType0AudiosItem,
        )
        from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_book import (
            GetPostLinkingsResponse200DataItemType0DataType0Book,
        )
        from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_images_item import (
            GetPostLinkingsResponse200DataItemType0DataType0ImagesItem,
        )
        from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_music import (
            GetPostLinkingsResponse200DataItemType0DataType0Music,
        )
        from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_profile import (
            GetPostLinkingsResponse200DataItemType0DataType0Profile,
        )
        from ..models.get_post_linkings_response_200_data_item_type_0_data_type_0_videos_item import (
            GetPostLinkingsResponse200DataItemType0DataType0VideosItem,
        )

        d = dict(src_dict)
        _article = d.pop("article", UNSET)
        article: GetPostLinkingsResponse200DataItemType0DataType0Article | Unset
        if isinstance(_article, Unset):
            article = UNSET
        else:
            article = GetPostLinkingsResponse200DataItemType0DataType0Article.from_dict(
                _article
            )

        audios = []
        _audios = d.pop("audios", UNSET)
        for audios_item_data in _audios or []:
            audios_item = (
                GetPostLinkingsResponse200DataItemType0DataType0AudiosItem.from_dict(
                    audios_item_data
                )
            )

            audios.append(audios_item)

        _book = d.pop("book", UNSET)
        book: GetPostLinkingsResponse200DataItemType0DataType0Book | Unset
        if isinstance(_book, Unset):
            book = UNSET
        else:
            book = GetPostLinkingsResponse200DataItemType0DataType0Book.from_dict(_book)

        description = d.pop("description", UNSET)

        determiner = d.pop("determiner", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = (
                GetPostLinkingsResponse200DataItemType0DataType0ImagesItem.from_dict(
                    images_item_data
                )
            )

            images.append(images_item)

        locale = d.pop("locale", UNSET)

        locales_alternate = cast(list[str], d.pop("localesAlternate", UNSET))

        _music = d.pop("music", UNSET)
        music: GetPostLinkingsResponse200DataItemType0DataType0Music | Unset
        if isinstance(_music, Unset):
            music = UNSET
        else:
            music = GetPostLinkingsResponse200DataItemType0DataType0Music.from_dict(
                _music
            )

        _profile = d.pop("profile", UNSET)
        profile: GetPostLinkingsResponse200DataItemType0DataType0Profile | Unset
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = GetPostLinkingsResponse200DataItemType0DataType0Profile.from_dict(
                _profile
            )

        site_name = d.pop("siteName", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        videos = []
        _videos = d.pop("videos", UNSET)
        for videos_item_data in _videos or []:
            videos_item = (
                GetPostLinkingsResponse200DataItemType0DataType0VideosItem.from_dict(
                    videos_item_data
                )
            )

            videos.append(videos_item)

        get_post_linkings_response_200_data_item_type_0_data_type_0 = cls(
            article=article,
            audios=audios,
            book=book,
            description=description,
            determiner=determiner,
            images=images,
            locale=locale,
            locales_alternate=locales_alternate,
            music=music,
            profile=profile,
            site_name=site_name,
            title=title,
            type_=type_,
            url=url,
            videos=videos,
        )

        get_post_linkings_response_200_data_item_type_0_data_type_0.additional_properties = d
        return get_post_linkings_response_200_data_item_type_0_data_type_0

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
