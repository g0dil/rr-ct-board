from enum import Enum


class RoutineStepCreateType0Type6ActionKey(str, Enum):
    ARCHIVE_GROUP_MEMBER = "archive-group-member"

    def __str__(self) -> str:
        return str(self.value)
