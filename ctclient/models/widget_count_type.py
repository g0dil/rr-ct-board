from enum import Enum


class WidgetCountType(str, Enum):
    BUBBLE = "bubble"
    REGULAR = "regular"

    def __str__(self) -> str:
        return str(self.value)
