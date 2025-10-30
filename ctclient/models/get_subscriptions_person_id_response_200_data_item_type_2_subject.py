from enum import Enum


class GetSubscriptionsPersonIdResponse200DataItemType2Subject(str, Enum):
    POST_SUMMARY = "post_summary"

    def __str__(self) -> str:
        return str(self.value)
