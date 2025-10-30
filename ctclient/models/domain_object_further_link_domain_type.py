from enum import Enum


class DomainObjectFurtherLinkDomainType(str, Enum):
    FURTHERLINK = "furtherLink"

    def __str__(self) -> str:
        return str(self.value)
