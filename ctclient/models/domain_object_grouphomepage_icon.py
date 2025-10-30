from enum import Enum


class DomainObjectGrouphomepageIcon(str, Enum):
    GLOBE = "globe"

    def __str__(self) -> str:
        return str(self.value)
