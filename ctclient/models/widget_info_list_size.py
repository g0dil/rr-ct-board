from enum import Enum


class WidgetInfoListSize(str, Enum):
    MEDIUM = "medium"
    SMALL = "small"

    def __str__(self) -> str:
        return str(self.value)
