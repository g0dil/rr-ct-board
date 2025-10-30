from enum import Enum


class GetSubscriptionsPersonIdResponse200DataItemType5Subject(str, Enum):
    SERVICEREQUESTS = "servicerequests"

    def __str__(self) -> str:
        return str(self.value)
