from enum import Enum


class DomainObjectOsmAddressIcon(str, Enum):
    LOCATION_DOT = "location-dot"

    def __str__(self) -> str:
        return str(self.value)
