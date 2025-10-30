from enum import Enum


class GetSongsIncludeItem(str, Enum):
    ARRANGEMENTS = "arrangements"
    TAGS = "tags"

    def __str__(self) -> str:
        return str(self.value)
