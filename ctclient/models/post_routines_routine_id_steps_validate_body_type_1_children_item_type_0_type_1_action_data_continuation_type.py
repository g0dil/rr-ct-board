from enum import Enum


class PostRoutinesRoutineIdStepsValidateBodyType1ChildrenItemType0Type1ActionDataContinuationType(
    str, Enum
):
    IMMEDIATELY = "immediately"
    WHEN_COMPLETED = "when-completed"

    def __str__(self) -> str:
        return str(self.value)
