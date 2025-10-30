from enum import Enum


class DomainObjectOsmAddressDomainType(str, Enum):
    OSM_ADDRESS = "osm-address"

    def __str__(self) -> str:
        return str(self.value)
