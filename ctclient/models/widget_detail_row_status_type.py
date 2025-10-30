from enum import Enum


class WidgetDetailRowStatusType(str, Enum):
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
