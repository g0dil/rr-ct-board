from enum import Enum


class DomainObjectPostIcon(str, Enum):
    NEWSPAPER = "newspaper"

    def __str__(self) -> str:
        return str(self.value)
