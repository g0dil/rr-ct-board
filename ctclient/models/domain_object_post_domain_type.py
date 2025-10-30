from enum import Enum


class DomainObjectPostDomainType(str, Enum):
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
