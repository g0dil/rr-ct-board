from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.markdown_conversion_request_options_default_output_scope import (
    MarkdownConversionRequestOptionsDefaultOutputScope,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkdownConversionRequestOptions")


@_attrs_define
class MarkdownConversionRequestOptions:
    """Global options for all sources

    Attributes:
        common_language (str | Unset):
        default_output_scope (MarkdownConversionRequestOptionsDefaultOutputScope | Unset):
    """

    common_language: str | Unset = UNSET
    default_output_scope: MarkdownConversionRequestOptionsDefaultOutputScope | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        common_language = self.common_language

        default_output_scope: str | Unset = UNSET
        if not isinstance(self.default_output_scope, Unset):
            default_output_scope = self.default_output_scope.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if common_language is not UNSET:
            field_dict["commonLanguage"] = common_language
        if default_output_scope is not UNSET:
            field_dict["defaultOutputScope"] = default_output_scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        common_language = d.pop("commonLanguage", UNSET)

        _default_output_scope = d.pop("defaultOutputScope", UNSET)
        default_output_scope: MarkdownConversionRequestOptionsDefaultOutputScope | Unset
        if isinstance(_default_output_scope, Unset):
            default_output_scope = UNSET
        else:
            default_output_scope = MarkdownConversionRequestOptionsDefaultOutputScope(
                _default_output_scope
            )

        markdown_conversion_request_options = cls(
            common_language=common_language,
            default_output_scope=default_output_scope,
        )

        return markdown_conversion_request_options
