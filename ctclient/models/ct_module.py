from enum import Enum


class CtModule(str, Enum):
    CHURCHCAL = "churchcal"
    CHURCHCHECKIN = "churchcheckin"
    CHURCHDB = "churchdb"
    CHURCHFINANCE = "churchfinance"
    CHURCHGROUP = "churchgroup"
    CHURCHREPORT = "churchreport"
    CHURCHRESOURCE = "churchresource"
    CHURCHSERVICE = "churchservice"
    CHURCHSYNC = "churchsync"
    CHURCHWIKI = "churchwiki"
    FINANCE = "finance"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
