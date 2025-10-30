from enum import Enum


class DomainObjectSongIcon(str, Enum):
    MUSIC = "music"

    def __str__(self) -> str:
        return str(self.value)
