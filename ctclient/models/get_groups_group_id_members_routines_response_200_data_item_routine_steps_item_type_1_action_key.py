from enum import Enum


class GetGroupsGroupIdMembersRoutinesResponse200DataItemRoutineStepsItemType1ActionKey(
    str, Enum
):
    SPECIALREPEAT = "special:repeat"

    def __str__(self) -> str:
        return str(self.value)
