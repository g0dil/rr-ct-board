from enum import Enum


class RoutineStepsItemType1ChildrenItemType0Type1ActionKey(str, Enum):
    CREATE_FOLLOW_UP = "create-follow-up"

    def __str__(self) -> str:
        return str(self.value)
