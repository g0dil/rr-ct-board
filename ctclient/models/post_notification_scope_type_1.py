from enum import Enum


class PostNotificationScopeType1(str, Enum):
    GROUP_INTERN = "group_intern"
    GROUP_VISIBLE = "group_visible"

    def __str__(self) -> str:
        return str(self.value)
