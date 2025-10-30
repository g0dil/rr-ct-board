from enum import Enum


class RoutineUpdateStepsItemType0RepositionItemType1(str, Enum):
    FINISHED = "finished"
    NOT_STARTED = "not-started"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
