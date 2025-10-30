from enum import Enum


class DomainObjectEventIcon(str, Enum):
    CALENDAR_DAY = "calendar-day"

    def __str__(self) -> str:
        return str(self.value)
