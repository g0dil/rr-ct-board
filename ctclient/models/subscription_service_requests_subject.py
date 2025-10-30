from enum import Enum


class SubscriptionServiceRequestsSubject(str, Enum):
    SERVICEREQUESTS = "servicerequests"

    def __str__(self) -> str:
        return str(self.value)
