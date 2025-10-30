from enum import Enum


class HtmlTemplateDomainType(str, Enum):
    BULKLETTER = "bulkletter"
    DONATION_RECEIPT_ATTACHMENT = "donation-receipt-attachment"
    DONATION_RECEIPT_LETTER = "donation-receipt-letter"
    EMAIL = "email"
    GROUPMEMBER_DOCUMENT = "groupmember-document"

    def __str__(self) -> str:
        return str(self.value)
