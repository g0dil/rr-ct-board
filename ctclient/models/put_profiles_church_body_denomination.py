from enum import Enum


class PutProfilesChurchBodyDenomination(str, Enum):
    DENOMINATION_CATHOLIC = "denomination.catholic"
    DENOMINATION_ECUMENICAL = "denomination.ecumenical"
    DENOMINATION_FREE_EVANGELICAL = "denomination.free.evangelical"
    DENOMINATION_NONE = "denomination.none"
    DENOMINATION_ORTHODOX = "denomination.orthodox"
    DENOMINATION_PROTESTANT = "denomination.protestant"

    def __str__(self) -> str:
        return str(self.value)
