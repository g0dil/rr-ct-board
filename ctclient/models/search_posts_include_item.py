from enum import Enum


class SearchPostsIncludeItem(str, Enum):
    COMMENTS = "comments"
    LINKINGS = "linkings"
    REACTIONS = "reactions"

    def __str__(self) -> str:
        return str(self.value)
