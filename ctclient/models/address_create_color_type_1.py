from enum import Enum


class AddressCreateColorType1(str, Enum):
    DEFAULT = "default"
    PARENT = "parent"

    def __str__(self) -> str:
        return str(self.value)
