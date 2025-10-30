from enum import Enum


class GetGroupHomepagesResponse200DataItemIcon(str, Enum):
    GLOBE = "globe"

    def __str__(self) -> str:
        return str(self.value)
