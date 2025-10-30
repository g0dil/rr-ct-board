from enum import Enum


class RoutineStepCreateWaitActionKey(str, Enum):
    SPECIALWAIT = "special:wait"

    def __str__(self) -> str:
        return str(self.value)
