from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.post_markdown_check_body_input_scope import (
    PostMarkdownCheckBodyInputScope,
)

T = TypeVar("T", bound="PostMarkdownCheckBody")


@_attrs_define
class PostMarkdownCheckBody:
    """
    Attributes:
        input_scope (PostMarkdownCheckBodyInputScope): Validates the provided Markdown content against the specified
            scope's rules and restrictions.
            This ensures the content adheres to the allowed formatting and elements for the given context.
        markdown (str): The Markdown text to be processed
    """

    input_scope: PostMarkdownCheckBodyInputScope
    markdown: str

    def to_dict(self) -> dict[str, Any]:
        input_scope = self.input_scope.value

        markdown = self.markdown

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "inputScope": input_scope,
                "markdown": markdown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_scope = PostMarkdownCheckBodyInputScope(d.pop("inputScope"))

        markdown = d.pop("markdown")

        post_markdown_check_body = cls(
            input_scope=input_scope,
            markdown=markdown,
        )

        return post_markdown_check_body
