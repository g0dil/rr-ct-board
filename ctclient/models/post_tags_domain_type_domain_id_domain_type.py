from enum import Enum


class PostTagsDomainTypeDomainIdDomainType(str, Enum):
    GROUP = "group"
    PERSON = "person"
    SONG = "song"

    def __str__(self) -> str:
        return str(self.value)
