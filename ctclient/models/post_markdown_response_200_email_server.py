from enum import Enum


class PostMarkdownResponse200EmailServer(str, Enum):
    CHURCHTOOLS = "churchtools"
    OWN = "own"

    def __str__(self) -> str:
        return str(self.value)
