from enum import Enum


class GetGroupRolesResponseFormat(str, Enum):
    DOMAINOBJECT = "domainObject"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
