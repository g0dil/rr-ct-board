from enum import Enum


class PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5Origin(
    str, Enum
):
    DEFAULT = "default"
    GROUP_SETTINGS = "group-settings"

    def __str__(self) -> str:
        return str(self.value)
