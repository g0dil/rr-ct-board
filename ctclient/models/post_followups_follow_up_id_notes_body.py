from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostFollowupsFollowUpIdNotesBody")


@_attrs_define
class PostFollowupsFollowUpIdNotesBody:
    """
    Attributes:
        comment (str):
        comment_viewer_id (int | None):
    """

    comment: str
    comment_viewer_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        comment_viewer_id: int | None
        comment_viewer_id = self.comment_viewer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "commentViewerId": comment_viewer_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment")

        def _parse_comment_viewer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        comment_viewer_id = _parse_comment_viewer_id(d.pop("commentViewerId"))

        post_followups_follow_up_id_notes_body = cls(
            comment=comment,
            comment_viewer_id=comment_viewer_id,
        )

        post_followups_follow_up_id_notes_body.additional_properties = d
        return post_followups_follow_up_id_notes_body

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
