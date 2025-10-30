from enum import Enum


class DomainObjectSongDomainType(str, Enum):
    SONG = "song"

    def __str__(self) -> str:
        return str(self.value)
