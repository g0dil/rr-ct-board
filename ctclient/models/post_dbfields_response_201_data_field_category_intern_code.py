from enum import Enum


class PostDbfieldsResponse201DataFieldCategoryInternCode(str, Enum):
    F_ADDRESS = "f_address"
    F_CATEGORY = "f_category"
    F_CHURCH = "f_church"
    F_DATASECURITY = "f_datasecurity"
    F_DEP = "f_dep"
    F_GROUP = "f_group"
    F_GROWPATH = "f_growpath"

    def __str__(self) -> str:
        return str(self.value)
