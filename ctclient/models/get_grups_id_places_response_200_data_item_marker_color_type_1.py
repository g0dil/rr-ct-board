from enum import Enum


class GetGrupsIdPlacesResponse200DataItemMarkerColorType1(str, Enum):
    DEFAULT = "default"
    PARENT = "parent"

    def __str__(self) -> str:
        return str(self.value)
