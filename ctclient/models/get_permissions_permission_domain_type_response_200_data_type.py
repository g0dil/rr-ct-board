from enum import Enum


class GetPermissionsPermissionDomainTypeResponse200DataType(str, Enum):
    GRANT = "grant"
    REVOKE = "revoke"

    def __str__(self) -> str:
        return str(self.value)
