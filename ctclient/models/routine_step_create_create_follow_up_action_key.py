from enum import Enum


class RoutineStepCreateCreateFollowUpActionKey(str, Enum):
    CREATE_FOLLOW_UP = "create-follow-up"

    def __str__(self) -> str:
        return str(self.value)
