from enum import Enum


class WidgetDateOrientation(str, Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

    def __str__(self) -> str:
        return str(self.value)
