from enum import Enum


class PostGroupsGroupIdPlacesResponse201DataMarkerColorType1(str, Enum):
    DEFAULT = "default"
    PARENT = "parent"

    def __str__(self) -> str:
        return str(self.value)
