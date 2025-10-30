from enum import Enum


class GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5Subject(
    str, Enum
):
    SERVICEREQUESTS = "servicerequests"

    def __str__(self) -> str:
        return str(self.value)
