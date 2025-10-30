from enum import Enum


class SubscriptionPublicChannelSubject(str, Enum):
    PUBLIC_CHANNEL = "public_channel"

    def __str__(self) -> str:
        return str(self.value)
