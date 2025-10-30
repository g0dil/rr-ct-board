from enum import Enum


class RoutineStepsItemType1ChildrenItemType0Type4ActionKey(str, Enum):
    SPECIALWAIT = "special:wait"

    def __str__(self) -> str:
        return str(self.value)
