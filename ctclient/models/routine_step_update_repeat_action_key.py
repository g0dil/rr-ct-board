from enum import Enum


class RoutineStepUpdateRepeatActionKey(str, Enum):
    SPECIALREPEAT = "special:repeat"

    def __str__(self) -> str:
        return str(self.value)
