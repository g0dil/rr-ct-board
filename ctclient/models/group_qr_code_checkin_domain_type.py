from enum import Enum


class GroupQRCodeCheckinDomainType(str, Enum):
    GROUP = "group"

    def __str__(self) -> str:
        return str(self.value)
