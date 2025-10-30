from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostPostsPostIdCommentsBody")


@_attrs_define
class PostPostsPostIdCommentsBody:
    """
    Attributes:
        content (str):
        post_id (int):
        parent_comment_id (int | None | Unset):
    """

    content: str
    post_id: int
    parent_comment_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        post_id = self.post_id

        parent_comment_id: int | None | Unset
        if isinstance(self.parent_comment_id, Unset):
            parent_comment_id = UNSET
        else:
            parent_comment_id = self.parent_comment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "postId": post_id,
            }
        )
        if parent_comment_id is not UNSET:
            field_dict["parentCommentId"] = parent_comment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        post_id = d.pop("postId")

        def _parse_parent_comment_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_comment_id = _parse_parent_comment_id(d.pop("parentCommentId", UNSET))

        post_posts_post_id_comments_body = cls(
            content=content,
            post_id=post_id,
            parent_comment_id=parent_comment_id,
        )

        post_posts_post_id_comments_body.additional_properties = d
        return post_posts_post_id_comments_body

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
