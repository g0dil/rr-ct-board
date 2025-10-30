from enum import Enum


class PutPostReportsAnswerBodyDomainType(str, Enum):
    POST = "post"
    POST_COMMENT = "post_comment"

    def __str__(self) -> str:
        return str(self.value)
