from enum import Enum


class DomainObjectGrouphomepageDomainType(str, Enum):
    GROUPHOMEPAGE = "grouphomepage"

    def __str__(self) -> str:
        return str(self.value)
