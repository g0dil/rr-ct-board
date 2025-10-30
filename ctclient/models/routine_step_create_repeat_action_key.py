from enum import Enum


class RoutineStepCreateRepeatActionKey(str, Enum):
    SPECIALREPEAT = "special:repeat"

    def __str__(self) -> str:
        return str(self.value)
