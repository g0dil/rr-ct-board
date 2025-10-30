from enum import Enum


class GetGroupQRCodeCheckinResponse200DataItemDomainType(str, Enum):
    GROUP = "group"

    def __str__(self) -> str:
        return str(self.value)
