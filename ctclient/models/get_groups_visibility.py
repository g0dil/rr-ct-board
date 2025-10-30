from enum import Enum


class GetGroupsVisibility(str, Enum):
    HIDDEN = "hidden"
    INTERN = "intern"
    PUBLIC = "public"
    RESTRICTED = "restricted"

    def __str__(self) -> str:
        return str(self.value)
