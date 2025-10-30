from enum import Enum


class AddressUpdateColorType1(str, Enum):
    DEFAULT = "default"
    PARENT = "parent"

    def __str__(self) -> str:
        return str(self.value)
