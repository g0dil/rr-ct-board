from enum import Enum


class SubscriptionType0Subject(str, Enum):
    GROUP = "group"

    def __str__(self) -> str:
        return str(self.value)
