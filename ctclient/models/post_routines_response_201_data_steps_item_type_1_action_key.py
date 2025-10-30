from enum import Enum


class PostRoutinesResponse201DataStepsItemType1ActionKey(str, Enum):
    SPECIALREPEAT = "special:repeat"

    def __str__(self) -> str:
        return str(self.value)
