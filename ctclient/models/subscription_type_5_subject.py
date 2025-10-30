from enum import Enum


class SubscriptionType5Subject(str, Enum):
    SERVICEREQUESTS = "servicerequests"

    def __str__(self) -> str:
        return str(self.value)
