from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFollowupsFollowUpIdCompleteBody")


@_attrs_define
class PostFollowupsFollowUpIdCompleteBody:
    """
    Attributes:
        success_group_id (int | None | Unset):
    """

    success_group_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success_group_id: int | None | Unset
        if isinstance(self.success_group_id, Unset):
            success_group_id = UNSET
        else:
            success_group_id = self.success_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success_group_id is not UNSET:
            field_dict["successGroupId"] = success_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_success_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        success_group_id = _parse_success_group_id(d.pop("successGroupId", UNSET))

        post_followups_follow_up_id_complete_body = cls(
            success_group_id=success_group_id,
        )

        post_followups_follow_up_id_complete_body.additional_properties = d
        return post_followups_follow_up_id_complete_body

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
