from enum import Enum


class RoutineStepCreateType0Type4ActionKey(str, Enum):
    SPECIALWAIT = "special:wait"

    def __str__(self) -> str:
        return str(self.value)
