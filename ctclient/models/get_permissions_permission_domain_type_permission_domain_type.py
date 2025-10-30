from enum import Enum


class GetPermissionsPermissionDomainTypePermissionDomainType(str, Enum):
    GROUP_ROLE = "group_role"
    GROUP_TYPE_ROLE = "group_type_role"
    PERSON = "person"
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
