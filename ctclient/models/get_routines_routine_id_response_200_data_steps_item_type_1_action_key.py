from enum import Enum


class GetRoutinesRoutineIdResponse200DataStepsItemType1ActionKey(str, Enum):
    SPECIALREPEAT = "special:repeat"

    def __str__(self) -> str:
        return str(self.value)
