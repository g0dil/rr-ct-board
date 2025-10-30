from enum import Enum


class GetGroupHomepagesResponse200DataItemDomainType(str, Enum):
    GROUPHOMEPAGE = "grouphomepage"

    def __str__(self) -> str:
        return str(self.value)
