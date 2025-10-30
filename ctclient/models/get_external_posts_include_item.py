from enum import Enum


class GetExternalPostsIncludeItem(str, Enum):
    LINKINGS = "linkings"

    def __str__(self) -> str:
        return str(self.value)
