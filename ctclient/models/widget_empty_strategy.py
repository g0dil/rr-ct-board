from enum import Enum


class WidgetEmptyStrategy(str, Enum):
    HIDE = "HIDE"
    SHOW = "SHOW"

    def __str__(self) -> str:
        return str(self.value)
