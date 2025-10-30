from enum import Enum


class PostDbfieldsBodyFieldTypeInternCode(str, Enum):
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
