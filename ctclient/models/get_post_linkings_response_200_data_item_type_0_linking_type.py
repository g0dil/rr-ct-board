from enum import Enum


class GetPostLinkingsResponse200DataItemType0LinkingType(str, Enum):
    OPENGRAPH = "opengraph"

    def __str__(self) -> str:
        return str(self.value)
