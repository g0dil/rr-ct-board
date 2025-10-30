from enum import Enum


class PatchGroupResponse200DataSettingsDynamicGroupRuleSetType0ItemQueryMethod(
    str, Enum
):
    CHURCHQUERY = "ChurchQuery"

    def __str__(self) -> str:
        return str(self.value)
