from enum import Enum


class GetGroupsGroupedGroupBy(str, Enum):
    AGEGROUP = "ageGroup"
    CAMPUS = "campus"
    GROUPCATEGORY = "groupCategory"
    GROUPSTATUS = "groupStatus"
    GROUPTYPE = "groupType"
    ISOPENFORMEMBERS = "isOpenForMembers"
    TARGETGROUP = "targetGroup"
    VISIBILITY = "visibility"

    def __str__(self) -> str:
        return str(self.value)
