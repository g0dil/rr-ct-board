from enum import Enum


class UpdateNoteDomainType(str, Enum):
    FOLLOW_UP = "follow_up"
    GROUP = "group"
    PERSON = "person"
    SONG_ARRANGEMENT = "song_arrangement"

    def __str__(self) -> str:
        return str(self.value)
