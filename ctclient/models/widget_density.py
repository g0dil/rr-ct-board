from enum import Enum


class WidgetDensity(str, Enum):
    COMPACT = "compact"
    DEFAULT = "default"
    DIVIDED = "divided"

    def __str__(self) -> str:
        return str(self.value)
