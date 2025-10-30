from enum import Enum


class GetCalendarsAppointmentsIncludeItem(str, Enum):
    BOOKINGS = "bookings"
    EVENT = "event"
    GROUP = "group"
    MEETINGREQUESTS = "meetingRequests"
    TAGS = "tags"
    TITLESUFFIX = "titleSuffix"

    def __str__(self) -> str:
        return str(self.value)
