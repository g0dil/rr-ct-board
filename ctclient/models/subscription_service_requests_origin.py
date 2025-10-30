from enum import Enum


class SubscriptionServiceRequestsOrigin(str, Enum):
    DEFAULT = "default"
    GROUP_SETTINGS = "group-settings"

    def __str__(self) -> str:
        return str(self.value)
