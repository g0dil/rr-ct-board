from enum import Enum


class DomainObjectCalendarIcon(str, Enum):
    CALENDAR = "calendar"

    def __str__(self) -> str:
        return str(self.value)
