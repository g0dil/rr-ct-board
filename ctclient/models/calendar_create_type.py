from enum import Enum


class CalendarCreateType(str, Enum):
    CHURCH = "church"
    GROUP = "group"
    PERSONAL = "personal"

    def __str__(self) -> str:
        return str(self.value)
