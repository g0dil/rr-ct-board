from enum import Enum


class WidgetBaseEmptyStrategy(str, Enum):
    HIDE = "HIDE"
    SHOW = "SHOW"

    def __str__(self) -> str:
        return str(self.value)
