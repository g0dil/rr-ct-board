from enum import Enum


class GetGroupsGroupIdMembersRoutinesResponse200DataItemRoutineStepsItemType1ChildrenItemType0Type1ActionDataSuccessGroupMemberStatusType0(
    str, Enum
):
    ACTIVE = "active"
    REQUESTED = "requested"
    TO_DELETE = "to_delete"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
