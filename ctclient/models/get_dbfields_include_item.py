from enum import Enum


class GetDbfieldsIncludeItem(str, Enum):
    OPTIONS = "options"

    def __str__(self) -> str:
        return str(self.value)
