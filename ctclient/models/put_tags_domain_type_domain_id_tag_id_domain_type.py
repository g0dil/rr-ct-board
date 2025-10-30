from enum import Enum


class PutTagsDomainTypeDomainIdTagIdDomainType(str, Enum):
    GROUP = "group"
    PERSON = "person"
    SONG = "song"

    def __str__(self) -> str:
        return str(self.value)
