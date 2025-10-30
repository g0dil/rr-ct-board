from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkdownConversionRequestSourcesItemOptions")


@_attrs_define
class MarkdownConversionRequestSourcesItemOptions:
    """Additional processing options

    Attributes:
        allow_html (bool | Unset):  Default: False.
        max_length (int | Unset):
        language (str | Unset):
    """

    allow_html: bool | Unset = False
    max_length: int | Unset = UNSET
    language: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allow_html = self.allow_html

        max_length = self.max_length

        language = self.language

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allow_html is not UNSET:
            field_dict["allowHtml"] = allow_html
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_html = d.pop("allowHtml", UNSET)

        max_length = d.pop("maxLength", UNSET)

        language = d.pop("language", UNSET)

        markdown_conversion_request_sources_item_options = cls(
            allow_html=allow_html,
            max_length=max_length,
            language=language,
        )

        return markdown_conversion_request_sources_item_options
