from enum import Enum


class SubscriptionType2Subject(str, Enum):
    POST_SUMMARY = "post_summary"

    def __str__(self) -> str:
        return str(self.value)
