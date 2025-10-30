from enum import Enum


class GetGroupsGroupIdIncludeItem(str, Enum):
    HASPERMISSIONS = "hasPermissions"
    MEMBERSTATISTICS = "memberStatistics"
    PLACES = "places"
    PUBLICPOSTSSTATISTIC = "publicPostsStatistic"
    ROLES = "roles"
    SIGNUPCONDITIONS = "signupConditions"
    TAGS = "tags"

    def __str__(self) -> str:
        return str(self.value)
