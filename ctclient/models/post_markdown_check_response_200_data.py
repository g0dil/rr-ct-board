from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_markdown_check_response_200_data_reason_item import (
        PostMarkdownCheckResponse200DataReasonItem,
    )


T = TypeVar("T", bound="PostMarkdownCheckResponse200Data")


@_attrs_define
class PostMarkdownCheckResponse200Data:
    """
    Attributes:
        is_valid (bool): Indicates if the provided Markdown content adheres to the specified scope's rules. - `true`:
            The content is valid and contains only allowed elements for the given scope - `false`: The content contains
            unsupported elements or formatting. Check the `reason` array for specific validation errors.
        reason (list[PostMarkdownCheckResponse200DataReasonItem]): Array of validation error messages
    """

    is_valid: bool
    reason: list[PostMarkdownCheckResponse200DataReasonItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_valid = self.is_valid

        reason = []
        for reason_item_data in self.reason:
            reason_item = reason_item_data.to_dict()
            reason.append(reason_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isValid": is_valid,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_markdown_check_response_200_data_reason_item import (
            PostMarkdownCheckResponse200DataReasonItem,
        )

        d = dict(src_dict)
        is_valid = d.pop("isValid")

        reason = []
        _reason = d.pop("reason")
        for reason_item_data in _reason:
            reason_item = PostMarkdownCheckResponse200DataReasonItem.from_dict(
                reason_item_data
            )

            reason.append(reason_item)

        post_markdown_check_response_200_data = cls(
            is_valid=is_valid,
            reason=reason,
        )

        post_markdown_check_response_200_data.additional_properties = d
        return post_markdown_check_response_200_data

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
