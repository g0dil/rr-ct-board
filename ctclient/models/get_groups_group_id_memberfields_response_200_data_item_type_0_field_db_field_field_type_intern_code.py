from enum import Enum


class GetGroupsGroupIdMemberfieldsResponse200DataItemType0FieldDbFieldFieldTypeInternCode(
    str, Enum
):
    API = "api"
    CHECKBOX = "checkbox"
    DATE = "date"
    DATETIME = "datetime"
    MULTISELECT = "multiselect"
    NUMBER = "number"
    RADIOSELECT = "radioselect"
    SELECT = "select"
    TEXT = "text"
    TEXTAREA = "textarea"

    def __str__(self) -> str:
        return str(self.value)
