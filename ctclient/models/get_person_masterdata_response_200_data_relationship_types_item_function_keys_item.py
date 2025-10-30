from enum import Enum


class GetPersonMasterdataResponse200DataRelationshipTypesItemFunctionKeysItem(
    str, Enum
):
    NODELETE = "nodelete"
    NODUPLICATE = "noduplicate"
    OPENDUPLICATE = "openduplicate"

    def __str__(self) -> str:
        return str(self.value)
