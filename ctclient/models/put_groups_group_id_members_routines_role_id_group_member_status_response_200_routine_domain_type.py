from enum import Enum


class PutGroupsGroupIdMembersRoutinesRoleIdGroupMemberStatusResponse200RoutineDomainType(
    str, Enum
):
    GROUP_MEMBERSHIP = "group_membership"

    def __str__(self) -> str:
        return str(self.value)
