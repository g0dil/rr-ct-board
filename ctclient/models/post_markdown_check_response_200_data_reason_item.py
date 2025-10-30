from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostMarkdownCheckResponse200DataReasonItem")


@_attrs_define
class PostMarkdownCheckResponse200DataReasonItem:
    """
    Attributes:
        message (str | Unset): The details of the validation error
        source_line_content (str | Unset): The invalid line from the Markdown source
        source_line_number (int | Unset): The invalid line number in the Markdown source
    """

    message: str | Unset = UNSET
    source_line_content: str | Unset = UNSET
    source_line_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        source_line_content = self.source_line_content

        source_line_number = self.source_line_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if source_line_content is not UNSET:
            field_dict["sourceLineContent"] = source_line_content
        if source_line_number is not UNSET:
            field_dict["sourceLineNumber"] = source_line_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        source_line_content = d.pop("sourceLineContent", UNSET)

        source_line_number = d.pop("sourceLineNumber", UNSET)

        post_markdown_check_response_200_data_reason_item = cls(
            message=message,
            source_line_content=source_line_content,
            source_line_number=source_line_number,
        )

        post_markdown_check_response_200_data_reason_item.additional_properties = d
        return post_markdown_check_response_200_data_reason_item

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
