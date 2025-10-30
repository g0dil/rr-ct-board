from enum import Enum


class WidgetDetailRowPropertiesType(str, Enum):
    PROPERTIES = "properties"

    def __str__(self) -> str:
        return str(self.value)
