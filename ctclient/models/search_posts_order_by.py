from enum import Enum


class SearchPostsOrderBy(str, Enum):
    PUBLISHEDDATE = "publishedDate"
    RELEVANCE = "relevance"

    def __str__(self) -> str:
        return str(self.value)
