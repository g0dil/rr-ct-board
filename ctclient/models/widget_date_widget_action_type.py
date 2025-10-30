from enum import Enum


class WidgetDateWidgetActionType(str, Enum):
    DETAILS = "details"
    OTHER = "other"
    PRIMARY = "primary"
    SECONDARY = "secondary"

    def __str__(self) -> str:
        return str(self.value)
