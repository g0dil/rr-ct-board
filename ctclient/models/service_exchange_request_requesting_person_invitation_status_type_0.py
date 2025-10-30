from enum import Enum


class ServiceExchangeRequestRequestingPersonInvitationStatusType0(str, Enum):
    ACCEPTED = "accepted"
    NOT_INVITED = "not_invited"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
