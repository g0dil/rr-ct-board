from enum import Enum


class WidgetDateWidgetSettingsType0Density(str, Enum):
    COMPACT = "compact"
    DEFAULT = "default"
    DIVIDED = "divided"

    def __str__(self) -> str:
        return str(self.value)
