from enum import Enum


class DomainObjectCalendarDomainType(str, Enum):
    CALENDAR = "calendar"

    def __str__(self) -> str:
        return str(self.value)
