from enum import Enum


class FieldMappingEntrySystem(str, Enum):
    EXTERNALSYSTEM = "externalSystem"
    MASTER = "master"

    def __str__(self) -> str:
        return str(self.value)
