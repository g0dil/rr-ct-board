from enum import Enum


class RoutineStepCreateRepeatChildrenItemType0Type1ActionDataContinuationType(
    str, Enum
):
    IMMEDIATELY = "immediately"
    WHEN_COMPLETED = "when-completed"

    def __str__(self) -> str:
        return str(self.value)
