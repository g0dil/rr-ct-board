from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.post_markdown_markdown_conversion_request_sources_item_input_scope import (
    PostMarkdownMarkdownConversionRequestSourcesItemInputScope,
)
from ..models.post_markdown_markdown_conversion_request_sources_item_output_formats_item import (
    PostMarkdownMarkdownConversionRequestSourcesItemOutputFormatsItem,
)
from ..models.post_markdown_markdown_conversion_request_sources_item_output_scopes_item import (
    PostMarkdownMarkdownConversionRequestSourcesItemOutputScopesItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_markdown_markdown_conversion_request_sources_item_options import (
        PostMarkdownMarkdownConversionRequestSourcesItemOptions,
    )


T = TypeVar("T", bound="PostMarkdownMarkdownConversionRequestSourcesItem")


@_attrs_define
class PostMarkdownMarkdownConversionRequestSourcesItem:
    """
    Attributes:
        short_name (str): A short identifier for the source
        input_scope (PostMarkdownMarkdownConversionRequestSourcesItemInputScope): The scope of the input content
        output_scopes (list[PostMarkdownMarkdownConversionRequestSourcesItemOutputScopesItem]): List of scopes for the
            output content
        output_formats (list[PostMarkdownMarkdownConversionRequestSourcesItemOutputFormatsItem]): List of output formats
            for the processed markdown content
        markdown (str): The markdown content to be processed
        options (PostMarkdownMarkdownConversionRequestSourcesItemOptions | Unset): Additional processing options
    """

    short_name: str
    input_scope: PostMarkdownMarkdownConversionRequestSourcesItemInputScope
    output_scopes: list[
        PostMarkdownMarkdownConversionRequestSourcesItemOutputScopesItem
    ]
    output_formats: list[
        PostMarkdownMarkdownConversionRequestSourcesItemOutputFormatsItem
    ]
    markdown: str
    options: PostMarkdownMarkdownConversionRequestSourcesItemOptions | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        short_name = self.short_name

        input_scope = self.input_scope.value

        output_scopes = []
        for output_scopes_item_data in self.output_scopes:
            output_scopes_item = output_scopes_item_data.value
            output_scopes.append(output_scopes_item)

        output_formats = []
        for output_formats_item_data in self.output_formats:
            output_formats_item = output_formats_item_data.value
            output_formats.append(output_formats_item)

        markdown = self.markdown

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "shortName": short_name,
                "inputScope": input_scope,
                "outputScopes": output_scopes,
                "outputFormats": output_formats,
                "markdown": markdown,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_markdown_markdown_conversion_request_sources_item_options import (
            PostMarkdownMarkdownConversionRequestSourcesItemOptions,
        )

        d = dict(src_dict)
        short_name = d.pop("shortName")

        input_scope = PostMarkdownMarkdownConversionRequestSourcesItemInputScope(
            d.pop("inputScope")
        )

        output_scopes = []
        _output_scopes = d.pop("outputScopes")
        for output_scopes_item_data in _output_scopes:
            output_scopes_item = (
                PostMarkdownMarkdownConversionRequestSourcesItemOutputScopesItem(
                    output_scopes_item_data
                )
            )

            output_scopes.append(output_scopes_item)

        output_formats = []
        _output_formats = d.pop("outputFormats")
        for output_formats_item_data in _output_formats:
            output_formats_item = (
                PostMarkdownMarkdownConversionRequestSourcesItemOutputFormatsItem(
                    output_formats_item_data
                )
            )

            output_formats.append(output_formats_item)

        markdown = d.pop("markdown")

        _options = d.pop("options", UNSET)
        options: PostMarkdownMarkdownConversionRequestSourcesItemOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = PostMarkdownMarkdownConversionRequestSourcesItemOptions.from_dict(
                _options
            )

        post_markdown_markdown_conversion_request_sources_item = cls(
            short_name=short_name,
            input_scope=input_scope,
            output_scopes=output_scopes,
            output_formats=output_formats,
            markdown=markdown,
            options=options,
        )

        return post_markdown_markdown_conversion_request_sources_item
