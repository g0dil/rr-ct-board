from enum import Enum


class SubscriptionGroupOrigin(str, Enum):
    DEFAULT = "default"
    GROUP_SETTINGS = "group-settings"

    def __str__(self) -> str:
        return str(self.value)
