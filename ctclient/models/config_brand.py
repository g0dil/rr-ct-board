from enum import Enum


class ConfigBrand(str, Enum):
    CHURCHTOOLS = "ChurchTools"
    VEREINTOOLS = "VereinTools"

    def __str__(self) -> str:
        return str(self.value)
