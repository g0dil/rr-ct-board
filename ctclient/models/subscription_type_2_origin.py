from enum import Enum


class SubscriptionType2Origin(str, Enum):
    DEFAULT = "default"
    GROUP_SETTINGS = "group-settings"

    def __str__(self) -> str:
        return str(self.value)
