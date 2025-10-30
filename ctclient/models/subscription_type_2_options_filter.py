from enum import Enum


class SubscriptionType2OptionsFilter(str, Enum):
    ALL = "all"
    FEATURED_GROUPS = "featured_groups"
    MY_CAMPUS = "my_campus"
    MY_GROUPS = "my_groups"

    def __str__(self) -> str:
        return str(self.value)
