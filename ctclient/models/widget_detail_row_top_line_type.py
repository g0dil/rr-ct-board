from enum import Enum


class WidgetDetailRowTopLineType(str, Enum):
    TOP_LINE = "top-line"

    def __str__(self) -> str:
        return str(self.value)
