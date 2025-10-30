from enum import Enum


class GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1Subject(
    str, Enum
):
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
