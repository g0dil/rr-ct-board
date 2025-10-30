from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.post_create_visibility import PostCreateVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostCreate")


@_attrs_define
class PostCreate:
    """
    Attributes:
        content (None | str):
        title (str):
        visibility (PostCreateVisibility):
        group_id (int):
        expiration_date (datetime.datetime | None | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z'
            Example: 2022-10-19T12:00:00Z.
        publication_date (datetime.datetime | None | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        comments_active (bool | Unset):
        image_ids (list[int] | Unset):
    """

    content: None | str
    title: str
    visibility: PostCreateVisibility
    group_id: int
    expiration_date: datetime.datetime | None | Unset = UNSET
    publication_date: datetime.datetime | None | Unset = UNSET
    comments_active: bool | Unset = UNSET
    image_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: None | str
        content = self.content

        title = self.title

        visibility = self.visibility.value

        group_id = self.group_id

        expiration_date: None | str | Unset
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        elif isinstance(self.expiration_date, datetime.datetime):
            expiration_date = self.expiration_date.isoformat()
        else:
            expiration_date = self.expiration_date

        publication_date: None | str | Unset
        if isinstance(self.publication_date, Unset):
            publication_date = UNSET
        elif isinstance(self.publication_date, datetime.datetime):
            publication_date = self.publication_date.isoformat()
        else:
            publication_date = self.publication_date

        comments_active = self.comments_active

        image_ids: list[int] | Unset = UNSET
        if not isinstance(self.image_ids, Unset):
            image_ids = self.image_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "title": title,
                "visibility": visibility,
                "groupId": group_id,
            }
        )
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if publication_date is not UNSET:
            field_dict["publicationDate"] = publication_date
        if comments_active is not UNSET:
            field_dict["commentsActive"] = comments_active
        if image_ids is not UNSET:
            field_dict["imageIds"] = image_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content = _parse_content(d.pop("content"))

        title = d.pop("title")

        visibility = PostCreateVisibility(d.pop("visibility"))

        group_id = d.pop("groupId")

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

        comments_active = d.pop("commentsActive", UNSET)

        image_ids = cast(list[int], d.pop("imageIds", UNSET))

        post_create = cls(
            content=content,
            title=title,
            visibility=visibility,
            group_id=group_id,
            expiration_date=expiration_date,
            publication_date=publication_date,
            comments_active=comments_active,
            image_ids=image_ids,
        )

        post_create.additional_properties = d
        return post_create

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
