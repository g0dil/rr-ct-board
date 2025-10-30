from enum import Enum


class GetPostsIncludeItem(str, Enum):
    COMMENTS = "comments"
    LINKINGS = "linkings"
    REACTIONS = "reactions"

    def __str__(self) -> str:
        return str(self.value)
