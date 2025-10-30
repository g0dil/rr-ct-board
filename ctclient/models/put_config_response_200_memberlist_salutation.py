from enum import Enum


class PutConfigResponse200MemberlistSalutation(str, Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"

    def __str__(self) -> str:
        return str(self.value)
