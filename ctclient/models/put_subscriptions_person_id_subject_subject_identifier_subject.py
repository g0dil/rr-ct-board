from enum import Enum


class PutSubscriptionsPersonIdSubjectSubjectIdentifierSubject(str, Enum):
    GROUP = "group"
    MEETINGREQUESTS = "meetingrequests"
    POST = "post"
    POST_SUMMARY = "post_summary"
    PUBLIC_CHANNEL = "public_channel"
    SERVICEREQUESTS = "servicerequests"

    def __str__(self) -> str:
        return str(self.value)
