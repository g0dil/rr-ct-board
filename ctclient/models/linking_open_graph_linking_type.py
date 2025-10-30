from enum import Enum


class LinkingOpenGraphLinkingType(str, Enum):
    OPENGRAPH = "opengraph"

    def __str__(self) -> str:
        return str(self.value)
