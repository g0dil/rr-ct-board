from enum import Enum


class WidgetActionType(str, Enum):
    DETAILS = "details"
    OTHER = "other"
    PRIMARY = "primary"
    SECONDARY = "secondary"

    def __str__(self) -> str:
        return str(self.value)
