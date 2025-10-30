from enum import Enum


class PutConfigResponse200VerificationStatus(str, Enum):
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    NOT_VERIFIED = "not_verified"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
