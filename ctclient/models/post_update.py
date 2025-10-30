from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.post_update_visibility import PostUpdateVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUpdate")


@_attrs_define
class PostUpdate:
    """
    Attributes:
        comments_active (bool | Unset):
        content (None | str | Unset):
        expiration_date (datetime.datetime | None | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z'
            Example: 2022-10-19T12:00:00Z.
        image_ids (list[int] | Unset):
        publication_date (datetime.datetime | None | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        title (str | Unset):
        visibility (PostUpdateVisibility | Unset):
    """

    comments_active: bool | Unset = UNSET
    content: None | str | Unset = UNSET
    expiration_date: datetime.datetime | None | Unset = UNSET
    image_ids: list[int] | Unset = UNSET
    publication_date: datetime.datetime | None | Unset = UNSET
    title: str | Unset = UNSET
    visibility: PostUpdateVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments_active = self.comments_active

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        expiration_date: None | str | Unset
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        elif isinstance(self.expiration_date, datetime.datetime):
            expiration_date = self.expiration_date.isoformat()
        else:
            expiration_date = self.expiration_date

        image_ids: list[int] | Unset = UNSET
        if not isinstance(self.image_ids, Unset):
            image_ids = self.image_ids

        publication_date: None | str | Unset
        if isinstance(self.publication_date, Unset):
            publication_date = UNSET
        elif isinstance(self.publication_date, datetime.datetime):
            publication_date = self.publication_date.isoformat()
        else:
            publication_date = self.publication_date

        title = self.title

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments_active is not UNSET:
            field_dict["commentsActive"] = comments_active
        if content is not UNSET:
            field_dict["content"] = content
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if image_ids is not UNSET:
            field_dict["imageIds"] = image_ids
        if publication_date is not UNSET:
            field_dict["publicationDate"] = publication_date
        if title is not UNSET:
            field_dict["title"] = title
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments_active = d.pop("commentsActive", UNSET)

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_expiration_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_date_type_0 = isoparse(data)

                return expiration_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration_date = _parse_expiration_date(d.pop("expirationDate", UNSET))

        image_ids = cast(list[int], d.pop("imageIds", UNSET))

        def _parse_publication_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publication_date_type_0 = isoparse(data)

                return publication_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        publication_date = _parse_publication_date(d.pop("publicationDate", UNSET))

        title = d.pop("title", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: PostUpdateVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = PostUpdateVisibility(_visibility)

        post_update = cls(
            comments_active=comments_active,
            content=content,
            expiration_date=expiration_date,
            image_ids=image_ids,
            publication_date=publication_date,
            title=title,
            visibility=visibility,
        )

        post_update.additional_properties = d
        return post_update

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
