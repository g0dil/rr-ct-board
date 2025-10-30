from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkingOpenGraphDataType0Book")


@_attrs_define
class LinkingOpenGraphDataType0Book:
    """
    Example:
        {'authors': ['John Doe', 'Jane Smith'], 'isbn': '123-4567890123', 'releaseDate': '2020-01-01T00:00:00Z', 'tags':
            ['fiction', 'bestseller']}

    Attributes:
        authors (list[str] | Unset): The authors of the book.
        isbn (str | Unset): The International Standard Book Number of the book.
        release_date (datetime.datetime | Unset): The release date of the book.
        tags (list[str] | Unset): Tags associated with the book.
    """

    authors: list[str] | Unset = UNSET
    isbn: str | Unset = UNSET
    release_date: datetime.datetime | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authors: list[str] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = self.authors

        isbn = self.isbn

        release_date: str | Unset = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authors is not UNSET:
            field_dict["authors"] = authors
        if isbn is not UNSET:
            field_dict["isbn"] = isbn
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authors = cast(list[str], d.pop("authors", UNSET))

        isbn = d.pop("isbn", UNSET)

        _release_date = d.pop("releaseDate", UNSET)
        release_date: datetime.datetime | Unset
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date)

        tags = cast(list[str], d.pop("tags", UNSET))

        linking_open_graph_data_type_0_book = cls(
            authors=authors,
            isbn=isbn,
            release_date=release_date,
            tags=tags,
        )

        linking_open_graph_data_type_0_book.additional_properties = d
        return linking_open_graph_data_type_0_book

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
