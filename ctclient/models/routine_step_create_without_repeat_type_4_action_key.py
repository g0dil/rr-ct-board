from enum import Enum


class RoutineStepCreateWithoutRepeatType4ActionKey(str, Enum):
    SPECIALWAIT = "special:wait"

    def __str__(self) -> str:
        return str(self.value)
