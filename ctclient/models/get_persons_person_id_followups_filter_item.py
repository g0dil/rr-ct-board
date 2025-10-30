from enum import Enum


class GetPersonsPersonIdFollowupsFilterItem(str, Enum):
    DONE = "done"
    DUE_AFTER_TODAY = "due-after-today"
    DUE_BEFORE_TODAY = "due-before-today"
    DUE_TODAY = "due-today"
    DUE_UNSPECIFIED = "due-unspecified"

    def __str__(self) -> str:
        return str(self.value)
