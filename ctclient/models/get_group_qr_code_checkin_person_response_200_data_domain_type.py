from enum import Enum


class GetGroupQRCodeCheckinPersonResponse200DataDomainType(str, Enum):
    GROUP = "group"

    def __str__(self) -> str:
        return str(self.value)
