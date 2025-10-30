from enum import Enum


class SubscriptionType3Subject(str, Enum):
    PUBLIC_CHANNEL = "public_channel"

    def __str__(self) -> str:
        return str(self.value)
