from enum import Enum


class PutConfigResponse200Orderstatus(str, Enum):
    AUFTRAG = "Auftrag"
    BEDENKZEIT = "Bedenkzeit"
    ENTSCHEIDUNG = "Entscheidung"
    FINDER = "Finder"
    FINDERCOMBO = "FinderCombo"
    MITARBEITER = "Mitarbeiter"
    TESTPHASE = "Testphase"
    UNBEKANNT = "Unbekannt"
    VORLAGESCHULUNGTEST = "Vorlage/Schulung/Test"
    WEBSITECOMBO = "WebsiteCombo"
    ZU_LÖSCHEN = "zu löschen"

    def __str__(self) -> str:
        return str(self.value)
