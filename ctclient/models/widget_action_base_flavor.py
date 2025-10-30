from enum import Enum


class WidgetActionBaseFlavor(str, Enum):
    ACCENT = "accent"
    BASIC = "basic"
    CONSTRUCTIVE = "constructive"
    DESTRUCTIVE = "destructive"
    MAGIC = "magic"

    def __str__(self) -> str:
        return str(self.value)
