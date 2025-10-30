from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_markdown_markdown_conversion_request_options import (
        PostMarkdownMarkdownConversionRequestOptions,
    )
    from ..models.post_markdown_markdown_conversion_request_sources_item import (
        PostMarkdownMarkdownConversionRequestSourcesItem,
    )


T = TypeVar("T", bound="PostMarkdownMarkdownConversionRequest")


@_attrs_define
class PostMarkdownMarkdownConversionRequest:
    """Schema for validating markdown conversion requests

    Attributes:
        sources (list[PostMarkdownMarkdownConversionRequestSourcesItem]):
        options (PostMarkdownMarkdownConversionRequestOptions | Unset): Global options for all sources
    """

    sources: list[PostMarkdownMarkdownConversionRequestSourcesItem]
    options: PostMarkdownMarkdownConversionRequestOptions | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sources": sources,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_markdown_markdown_conversion_request_options import (
            PostMarkdownMarkdownConversionRequestOptions,
        )
        from ..models.post_markdown_markdown_conversion_request_sources_item import (
            PostMarkdownMarkdownConversionRequestSourcesItem,
        )

        d = dict(src_dict)
        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = PostMarkdownMarkdownConversionRequestSourcesItem.from_dict(
                sources_item_data
            )

            sources.append(sources_item)

        _options = d.pop("options", UNSET)
        options: PostMarkdownMarkdownConversionRequestOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = PostMarkdownMarkdownConversionRequestOptions.from_dict(_options)

        post_markdown_markdown_conversion_request = cls(
            sources=sources,
            options=options,
        )

        return post_markdown_markdown_conversion_request
