from enum import Enum


class PostLinkingLinkingsItemType0LinkingType(str, Enum):
    OPENGRAPH = "opengraph"

    def __str__(self) -> str:
        return str(self.value)
