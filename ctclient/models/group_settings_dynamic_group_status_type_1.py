from enum import Enum


class GroupSettingsDynamicGroupStatusType1(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    MANUAL = "manual"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
