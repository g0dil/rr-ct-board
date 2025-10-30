from enum import Enum


class WidgetDetailRowPrimaryType(str, Enum):
    PRIMARY = "primary"

    def __str__(self) -> str:
        return str(self.value)
