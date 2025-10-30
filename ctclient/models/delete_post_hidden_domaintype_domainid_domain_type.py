from enum import Enum


class DeletePostHiddenDomaintypeDomainidDomainType(str, Enum):
    ACTOR = "actor"
    GROUP = "group"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
