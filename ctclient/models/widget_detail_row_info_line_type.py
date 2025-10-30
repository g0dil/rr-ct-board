from enum import Enum


class WidgetDetailRowInfoLineType(str, Enum):
    INFO_LINE = "info-line"

    def __str__(self) -> str:
        return str(self.value)
