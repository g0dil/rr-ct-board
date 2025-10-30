from enum import Enum


class DomainObjectFurtherLinkIcon(str, Enum):
    LINK = "link"

    def __str__(self) -> str:
        return str(self.value)
