from enum import Enum


class SearchPostsGroupVisibility(str, Enum):
    HIDDEN = "hidden"
    INTERNAL = "internal"
    PUBLIC = "public"
    RESTRICTED = "restricted"

    def __str__(self) -> str:
        return str(self.value)
