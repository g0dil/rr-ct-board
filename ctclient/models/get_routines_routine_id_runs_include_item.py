from enum import Enum


class GetRoutinesRoutineIdRunsIncludeItem(str, Enum):
    DOMAINOBJECT = "domainObject"

    def __str__(self) -> str:
        return str(self.value)
