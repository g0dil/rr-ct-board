from enum import Enum


class WidgetInfoListDirection(str, Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    WRAPPED = "wrapped"

    def __str__(self) -> str:
        return str(self.value)
