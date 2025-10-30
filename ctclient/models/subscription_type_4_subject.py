from enum import Enum


class SubscriptionType4Subject(str, Enum):
    MEETINGREQUESTS = "meetingrequests"

    def __str__(self) -> str:
        return str(self.value)
