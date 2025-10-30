from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkingOpenGraphDataType0Article")


@_attrs_define
class LinkingOpenGraphDataType0Article:
    """
    Example:
        {'authors': ['John Doe', 'Jane Smith'], 'expirationTime': '2021-01-01T00:00:00Z', 'modifiedTime':
            '2020-01-02T00:00:00Z', 'publishedTime': '2020-01-01T00:00:00Z', 'section': 'News', 'tags': ['news', 'world']}

    Attributes:
        authors (list[str] | Unset): The authors of the article.
        expiration_time (datetime.datetime | Unset): The expiration time of the article.
        modified_time (datetime.datetime | Unset): The last modified time of the article.
        published_time (datetime.datetime | Unset): The publication time of the article.
        section (str | Unset): The section of the website where the article is located.
        tags (list[str] | Unset): Tags associated with the article.
    """

    authors: list[str] | Unset = UNSET
    expiration_time: datetime.datetime | Unset = UNSET
    modified_time: datetime.datetime | Unset = UNSET
    published_time: datetime.datetime | Unset = UNSET
    section: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authors: list[str] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = self.authors

        expiration_time: str | Unset = UNSET
        if not isinstance(self.expiration_time, Unset):
            expiration_time = self.expiration_time.isoformat()

        modified_time: str | Unset = UNSET
        if not isinstance(self.modified_time, Unset):
            modified_time = self.modified_time.isoformat()

        published_time: str | Unset = UNSET
        if not isinstance(self.published_time, Unset):
            published_time = self.published_time.isoformat()

        section = self.section

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authors is not UNSET:
            field_dict["authors"] = authors
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time
        if published_time is not UNSET:
            field_dict["publishedTime"] = published_time
        if section is not UNSET:
            field_dict["section"] = section
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authors = cast(list[str], d.pop("authors", UNSET))

        _expiration_time = d.pop("expirationTime", UNSET)
        expiration_time: datetime.datetime | Unset
        if isinstance(_expiration_time, Unset):
            expiration_time = UNSET
        else:
            expiration_time = isoparse(_expiration_time)

        _modified_time = d.pop("modifiedTime", UNSET)
        modified_time: datetime.datetime | Unset
        if isinstance(_modified_time, Unset):
            modified_time = UNSET
        else:
            modified_time = isoparse(_modified_time)

        _published_time = d.pop("publishedTime", UNSET)
        published_time: datetime.datetime | Unset
        if isinstance(_published_time, Unset):
            published_time = UNSET
        else:
            published_time = isoparse(_published_time)

        section = d.pop("section", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        linking_open_graph_data_type_0_article = cls(
            authors=authors,
            expiration_time=expiration_time,
            modified_time=modified_time,
            published_time=published_time,
            section=section,
            tags=tags,
        )

        linking_open_graph_data_type_0_article.additional_properties = d
        return linking_open_graph_data_type_0_article

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
