from enum import Enum


class GetAllGroupMembersQueryParamsIncludeItem(str, Enum):
    AGGREGATIONS = "aggregations"
    TAGS = "tags"

    def __str__(self) -> str:
        return str(self.value)
