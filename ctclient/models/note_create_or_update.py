from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoteCreateOrUpdate")


@_attrs_define
class NoteCreateOrUpdate:
    """
    Attributes:
        security_level_id (int | None):
        text (str):
        comment_viewer_id (int | None | Unset):
    """

    security_level_id: int | None
    text: str
    comment_viewer_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        security_level_id: int | None
        security_level_id = self.security_level_id

        text = self.text

        comment_viewer_id: int | None | Unset
        if isinstance(self.comment_viewer_id, Unset):
            comment_viewer_id = UNSET
        else:
            comment_viewer_id = self.comment_viewer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "securityLevelId": security_level_id,
                "text": text,
            }
        )
        if comment_viewer_id is not UNSET:
            field_dict["commentViewerId"] = comment_viewer_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_security_level_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        security_level_id = _parse_security_level_id(d.pop("securityLevelId"))

        text = d.pop("text")

        def _parse_comment_viewer_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        comment_viewer_id = _parse_comment_viewer_id(d.pop("commentViewerId", UNSET))

        note_create_or_update = cls(
            security_level_id=security_level_id,
            text=text,
            comment_viewer_id=comment_viewer_id,
        )

        note_create_or_update.additional_properties = d
        return note_create_or_update

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
