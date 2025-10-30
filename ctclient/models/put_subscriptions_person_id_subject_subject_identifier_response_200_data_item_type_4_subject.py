from enum import Enum


class PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4Subject(
    str, Enum
):
    MEETINGREQUESTS = "meetingrequests"

    def __str__(self) -> str:
        return str(self.value)
