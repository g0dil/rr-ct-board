from enum import Enum


class WidgetDetailItemRowEntryType(str, Enum):
    ENTRY = "entry"

    def __str__(self) -> str:
        return str(self.value)
