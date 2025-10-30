from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linking_open_graph_data_type_0_article import (
        LinkingOpenGraphDataType0Article,
    )
    from ..models.linking_open_graph_data_type_0_audios_item import (
        LinkingOpenGraphDataType0AudiosItem,
    )
    from ..models.linking_open_graph_data_type_0_book import (
        LinkingOpenGraphDataType0Book,
    )
    from ..models.linking_open_graph_data_type_0_images_item import (
        LinkingOpenGraphDataType0ImagesItem,
    )
    from ..models.linking_open_graph_data_type_0_music import (
        LinkingOpenGraphDataType0Music,
    )
    from ..models.linking_open_graph_data_type_0_profile import (
        LinkingOpenGraphDataType0Profile,
    )
    from ..models.linking_open_graph_data_type_0_videos_item import (
        LinkingOpenGraphDataType0VideosItem,
    )


T = TypeVar("T", bound="LinkingOpenGraphDataType0")


@_attrs_define
class LinkingOpenGraphDataType0:
    """
    Attributes:
        article (LinkingOpenGraphDataType0Article | Unset):  Example: {'authors': ['John Doe', 'Jane Smith'],
            'expirationTime': '2021-01-01T00:00:00Z', 'modifiedTime': '2020-01-02T00:00:00Z', 'publishedTime':
            '2020-01-01T00:00:00Z', 'section': 'News', 'tags': ['news', 'world']}.
        audios (list[LinkingOpenGraphDataType0AudiosItem] | Unset):
        book (LinkingOpenGraphDataType0Book | Unset):  Example: {'authors': ['John Doe', 'Jane Smith'], 'isbn':
            '123-4567890123', 'releaseDate': '2020-01-01T00:00:00Z', 'tags': ['fiction', 'bestseller']}.
        description (str | Unset): A brief description of the OpenGraph content.
        determiner (str | Unset): The determiner for the noun in the content.
        images (list[LinkingOpenGraphDataType0ImagesItem] | Unset):
        locale (str | Unset): The locale of the OpenGraph object.
        locales_alternate (list[str] | Unset): Alternate locales available.
        music (LinkingOpenGraphDataType0Music | Unset):
        profile (LinkingOpenGraphDataType0Profile | Unset):  Example: {'firstName': 'John', 'gender': 'male',
            'lastName': 'Doe', 'username': 'johndoe'}.
        site_name (str | Unset): The site name of the OpenGraph object.
        title (str | Unset): The title of the OpenGraph object.
        type_ (str | Unset): The type of OpenGraph object.
        url (str | Unset): The URL of the OpenGraph object.
        videos (list[LinkingOpenGraphDataType0VideosItem] | Unset):
    """

    article: LinkingOpenGraphDataType0Article | Unset = UNSET
    audios: list[LinkingOpenGraphDataType0AudiosItem] | Unset = UNSET
    book: LinkingOpenGraphDataType0Book | Unset = UNSET
    description: str | Unset = UNSET
    determiner: str | Unset = UNSET
    images: list[LinkingOpenGraphDataType0ImagesItem] | Unset = UNSET
    locale: str | Unset = UNSET
    locales_alternate: list[str] | Unset = UNSET
    music: LinkingOpenGraphDataType0Music | Unset = UNSET
    profile: LinkingOpenGraphDataType0Profile | Unset = UNSET
    site_name: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    url: str | Unset = UNSET
    videos: list[LinkingOpenGraphDataType0VideosItem] | Unset = UNSET
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
        from ..models.linking_open_graph_data_type_0_article import (
            LinkingOpenGraphDataType0Article,
        )
        from ..models.linking_open_graph_data_type_0_audios_item import (
            LinkingOpenGraphDataType0AudiosItem,
        )
        from ..models.linking_open_graph_data_type_0_book import (
            LinkingOpenGraphDataType0Book,
        )
        from ..models.linking_open_graph_data_type_0_images_item import (
            LinkingOpenGraphDataType0ImagesItem,
        )
        from ..models.linking_open_graph_data_type_0_music import (
            LinkingOpenGraphDataType0Music,
        )
        from ..models.linking_open_graph_data_type_0_profile import (
            LinkingOpenGraphDataType0Profile,
        )
        from ..models.linking_open_graph_data_type_0_videos_item import (
            LinkingOpenGraphDataType0VideosItem,
        )

        d = dict(src_dict)
        _article = d.pop("article", UNSET)
        article: LinkingOpenGraphDataType0Article | Unset
        if isinstance(_article, Unset):
            article = UNSET
        else:
            article = LinkingOpenGraphDataType0Article.from_dict(_article)

        audios = []
        _audios = d.pop("audios", UNSET)
        for audios_item_data in _audios or []:
            audios_item = LinkingOpenGraphDataType0AudiosItem.from_dict(
                audios_item_data
            )

            audios.append(audios_item)

        _book = d.pop("book", UNSET)
        book: LinkingOpenGraphDataType0Book | Unset
        if isinstance(_book, Unset):
            book = UNSET
        else:
            book = LinkingOpenGraphDataType0Book.from_dict(_book)

        description = d.pop("description", UNSET)

        determiner = d.pop("determiner", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = LinkingOpenGraphDataType0ImagesItem.from_dict(
                images_item_data
            )

            images.append(images_item)

        locale = d.pop("locale", UNSET)

        locales_alternate = cast(list[str], d.pop("localesAlternate", UNSET))

        _music = d.pop("music", UNSET)
        music: LinkingOpenGraphDataType0Music | Unset
        if isinstance(_music, Unset):
            music = UNSET
        else:
            music = LinkingOpenGraphDataType0Music.from_dict(_music)

        _profile = d.pop("profile", UNSET)
        profile: LinkingOpenGraphDataType0Profile | Unset
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = LinkingOpenGraphDataType0Profile.from_dict(_profile)

        site_name = d.pop("siteName", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        videos = []
        _videos = d.pop("videos", UNSET)
        for videos_item_data in _videos or []:
            videos_item = LinkingOpenGraphDataType0VideosItem.from_dict(
                videos_item_data
            )

            videos.append(videos_item)

        linking_open_graph_data_type_0 = cls(
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

        linking_open_graph_data_type_0.additional_properties = d
        return linking_open_graph_data_type_0

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
