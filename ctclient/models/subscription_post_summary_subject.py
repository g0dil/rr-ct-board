from enum import Enum


class SubscriptionPostSummarySubject(str, Enum):
    POST_SUMMARY = "post_summary"

    def __str__(self) -> str:
        return str(self.value)
