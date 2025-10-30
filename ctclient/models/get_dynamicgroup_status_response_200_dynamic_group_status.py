from enum import Enum


class GetDynamicgroupStatusResponse200DynamicGroupStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    MANUAL = "manual"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
