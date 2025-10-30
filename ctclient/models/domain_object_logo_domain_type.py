from enum import Enum


class DomainObjectLogoDomainType(str, Enum):
    LOGO = "logo"

    def __str__(self) -> str:
        return str(self.value)
