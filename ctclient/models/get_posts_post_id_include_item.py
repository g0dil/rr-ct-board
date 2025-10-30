from enum import Enum


class GetPostsPostIdIncludeItem(str, Enum):
    COMMENTS = "comments"
    REACTIONS = "reactions"

    def __str__(self) -> str:
        return str(self.value)
