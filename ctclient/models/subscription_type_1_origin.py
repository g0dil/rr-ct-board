from enum import Enum


class SubscriptionType1Origin(str, Enum):
    DEFAULT = "default"
    GROUP_SETTINGS = "group-settings"

    def __str__(self) -> str:
        return str(self.value)
