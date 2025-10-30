from enum import Enum


class PutPostsPostIdHiddenDomainTypeDomainType(str, Enum):
    ACTOR = "actor"
    GROUP = "group"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
