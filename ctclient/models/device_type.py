from enum import Enum


class DeviceType(str, Enum):
    APN = "APN"
    FCM = "FCM"

    def __str__(self) -> str:
        return str(self.value)
