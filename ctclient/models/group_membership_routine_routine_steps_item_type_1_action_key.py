from enum import Enum


class GroupMembershipRoutineRoutineStepsItemType1ActionKey(str, Enum):
    SPECIALREPEAT = "special:repeat"

    def __str__(self) -> str:
        return str(self.value)
