from enum import Enum


class GetAllDonationReceiptsCleardoublepage(str, Enum):
    ALL = "all"
    DONATION_ATTACHMENT = "donation_attachment"
    DONATION_COVER_LETTER = "donation_cover_letter"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
