from enum import Enum


class AddressColor(str, Enum):
    DEFAULT = "default"
    PARENT = "parent"

    def __str__(self) -> str:
        return str(self.value)
