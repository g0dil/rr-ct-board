from enum import Enum


class GetGroupsGroupIdMembersRoutinesResponse200DataItemRoutineDomainType(str, Enum):
    GROUP_MEMBERSHIP = "group_membership"

    def __str__(self) -> str:
        return str(self.value)
