from enum import Enum


class PostFeatureUsageBodyDataItemType(str, Enum):
    EVENT = "event"
    FEATURE = "feature"
    TOUR = "tour"

    def __str__(self) -> str:
        return str(self.value)
