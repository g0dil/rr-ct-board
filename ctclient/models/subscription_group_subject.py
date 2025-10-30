from enum import Enum


class SubscriptionGroupSubject(str, Enum):
    GROUP = "group"

    def __str__(self) -> str:
        return str(self.value)
