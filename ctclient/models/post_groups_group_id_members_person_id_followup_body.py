from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostGroupsGroupIdMembersPersonIdFollowupBody")


@_attrs_define
class PostGroupsGroupIdMembersPersonIdFollowupBody:
    """
    Attributes:
        comment (str):
        follow_up_successful (bool):
        add_diff_days (int | Unset):
        target_group_id (int | Unset):
        target_role_id (int | Unset):
    """

    comment: str
    follow_up_successful: bool
    add_diff_days: int | Unset = UNSET
    target_group_id: int | Unset = UNSET
    target_role_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        follow_up_successful = self.follow_up_successful

        add_diff_days = self.add_diff_days

        target_group_id = self.target_group_id

        target_role_id = self.target_role_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "followUpSuccessful": follow_up_successful,
            }
        )
        if add_diff_days is not UNSET:
            field_dict["addDiffDays"] = add_diff_days
        if target_group_id is not UNSET:
            field_dict["targetGroupId"] = target_group_id
        if target_role_id is not UNSET:
            field_dict["targetRoleId"] = target_role_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment")

        follow_up_successful = d.pop("followUpSuccessful")

        add_diff_days = d.pop("addDiffDays", UNSET)

        target_group_id = d.pop("targetGroupId", UNSET)

        target_role_id = d.pop("targetRoleId", UNSET)

        post_groups_group_id_members_person_id_followup_body = cls(
            comment=comment,
            follow_up_successful=follow_up_successful,
            add_diff_days=add_diff_days,
            target_group_id=target_group_id,
            target_role_id=target_role_id,
        )

        post_groups_group_id_members_person_id_followup_body.additional_properties = d
        return post_groups_group_id_members_person_id_followup_body

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
