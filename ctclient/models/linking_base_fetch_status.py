from enum import Enum


class LinkingBaseFetchStatus(str, Enum):
    HTTP_ERROR = "http-error"
    SUCCESS = "success"
    TIMEOUT_SHORT = "timeout-short"

    def __str__(self) -> str:
        return str(self.value)
