from enum import Enum


class GetAllDonationReceiptsMode(str, Enum):
    ONEFILE = "onefile"
    TWOFILES = "twofiles"

    def __str__(self) -> str:
        return str(self.value)
