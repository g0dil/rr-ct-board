from enum import Enum


class WebsiteDataCalendarDomainType(str, Enum):
    CALENDAR = "calendar"

    def __str__(self) -> str:
        return str(self.value)
