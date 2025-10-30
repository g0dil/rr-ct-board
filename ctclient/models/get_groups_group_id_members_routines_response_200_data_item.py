from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_groups_group_id_members_routines_response_200_data_item_group_member_status import (
    GetGroupsGroupIdMembersRoutinesResponse200DataItemGroupMemberStatus,
)

if TYPE_CHECKING:
    from ..models.get_groups_group_id_members_routines_response_200_data_item_routine import (
        GetGroupsGroupIdMembersRoutinesResponse200DataItemRoutine,
    )


T = TypeVar("T", bound="GetGroupsGroupIdMembersRoutinesResponse200DataItem")


@_attrs_define
class GetGroupsGroupIdMembersRoutinesResponse200DataItem:
    """
    Attributes:
        group_id (int):
        group_member_status (GetGroupsGroupIdMembersRoutinesResponse200DataItemGroupMemberStatus):
        group_type_role_id (int):
        id (int):
        routine (GetGroupsGroupIdMembersRoutinesResponse200DataItemRoutine):
    """

    group_id: int
    group_member_status: (
        GetGroupsGroupIdMembersRoutinesResponse200DataItemGroupMemberStatus
    )
    group_type_role_id: int
    id: int
    routine: GetGroupsGroupIdMembersRoutinesResponse200DataItemRoutine
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        group_member_status = self.group_member_status.value

        group_type_role_id = self.group_type_role_id

        id = self.id

        routine = self.routine.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groupId": group_id,
                "groupMemberStatus": group_member_status,
                "groupTypeRoleId": group_type_role_id,
                "id": id,
                "routine": routine,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_groups_group_id_members_routines_response_200_data_item_routine import (
            GetGroupsGroupIdMembersRoutinesResponse200DataItemRoutine,
        )

        d = dict(src_dict)
        group_id = d.pop("groupId")

        group_member_status = (
            GetGroupsGroupIdMembersRoutinesResponse200DataItemGroupMemberStatus(
                d.pop("groupMemberStatus")
            )
        )

        group_type_role_id = d.pop("groupTypeRoleId")

        id = d.pop("id")

        routine = GetGroupsGroupIdMembersRoutinesResponse200DataItemRoutine.from_dict(
            d.pop("routine")
        )

        get_groups_group_id_members_routines_response_200_data_item = cls(
            group_id=group_id,
            group_member_status=group_member_status,
            group_type_role_id=group_type_role_id,
            id=id,
            routine=routine,
        )

        get_groups_group_id_members_routines_response_200_data_item.additional_properties = d
        return get_groups_group_id_members_routines_response_200_data_item

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
