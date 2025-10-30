from enum import Enum


class DomainObjectWikiPageIcon(str, Enum):
    FILE = "file"

    def __str__(self) -> str:
        return str(self.value)
