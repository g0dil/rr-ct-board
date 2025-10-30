from enum import Enum


class SubscriptionMeetingRequestsSubject(str, Enum):
    MEETINGREQUESTS = "meetingrequests"

    def __str__(self) -> str:
        return str(self.value)
