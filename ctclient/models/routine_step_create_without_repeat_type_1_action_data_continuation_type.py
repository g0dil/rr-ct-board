from enum import Enum


class RoutineStepCreateWithoutRepeatType1ActionDataContinuationType(str, Enum):
    IMMEDIATELY = "immediately"
    WHEN_COMPLETED = "when-completed"

    def __str__(self) -> str:
        return str(self.value)
