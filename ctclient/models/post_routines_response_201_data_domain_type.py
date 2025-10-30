from enum import Enum


class PostRoutinesResponse201DataDomainType(str, Enum):
    GROUP_MEMBERSHIP = "group_membership"

    def __str__(self) -> str:
        return str(self.value)
