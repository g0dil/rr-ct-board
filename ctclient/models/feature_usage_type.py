from enum import Enum


class FeatureUsageType(str, Enum):
    EVENT = "event"
    FEATURE = "feature"
    TOUR = "tour"

    def __str__(self) -> str:
        return str(self.value)
