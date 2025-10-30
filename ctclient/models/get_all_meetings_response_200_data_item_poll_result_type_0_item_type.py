from enum import Enum


class GetAllMeetingsResponse200DataItemPollResultType0ItemType(str, Enum):
    CAPTION = "caption"
    CHECKBOX = "checkbox"
    COLOR = "color"
    INPUT = "input"
    SELECT = "select"
    TEXTAREA = "textarea"

    def __str__(self) -> str:
        return str(self.value)
