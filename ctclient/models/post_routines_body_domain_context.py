from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_routines_body_domain_context_group_member_status import (
    PostRoutinesBodyDomainContextGroupMemberStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostRoutinesBodyDomainContext")


@_attrs_define
class PostRoutinesBodyDomainContext:
    """Attributes of the context in which this routine is going to be executed.

    Attributes:
        group_id (int):
        group_type_role_id (int):
        group_member_status (PostRoutinesBodyDomainContextGroupMemberStatus | Unset):
    """

    group_id: int
    group_type_role_id: int
    group_member_status: PostRoutinesBodyDomainContextGroupMemberStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        group_type_role_id = self.group_type_role_id

        group_member_status: str | Unset = UNSET
        if not isinstance(self.group_member_status, Unset):
            group_member_status = self.group_member_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groupId": group_id,
                "groupTypeRoleId": group_type_role_id,
            }
        )
        if group_member_status is not UNSET:
            field_dict["groupMemberStatus"] = group_member_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = d.pop("groupId")

        group_type_role_id = d.pop("groupTypeRoleId")

        _group_member_status = d.pop("groupMemberStatus", UNSET)
        group_member_status: PostRoutinesBodyDomainContextGroupMemberStatus | Unset
        if isinstance(_group_member_status, Unset):
            group_member_status = UNSET
        else:
            group_member_status = PostRoutinesBodyDomainContextGroupMemberStatus(
                _group_member_status
            )

        post_routines_body_domain_context = cls(
            group_id=group_id,
            group_type_role_id=group_type_role_id,
            group_member_status=group_member_status,
        )

        post_routines_body_domain_context.additional_properties = d
        return post_routines_body_domain_context

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
