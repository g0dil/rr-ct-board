from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.group_qr_code_checkin_domain_type import GroupQRCodeCheckinDomainType

T = TypeVar("T", bound="GroupQRCodeCheckin")


@_attrs_define
class GroupQRCodeCheckin:
    """
    Attributes:
        domain_id (int):
        domain_type (GroupQRCodeCheckinDomainType):
        downloaded_date (datetime.datetime | None): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z'
            Example: 2022-10-19T12:00:00Z.
        expiry_date (datetime.datetime | None): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        is_queued (bool):
        person_id (int):
        sent_date (datetime.datetime | None): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        token (str):
        used_date (datetime.datetime | None): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
    """

    domain_id: int
    domain_type: GroupQRCodeCheckinDomainType
    downloaded_date: datetime.datetime | None
    expiry_date: datetime.datetime | None
    is_queued: bool
    person_id: int
    sent_date: datetime.datetime | None
    token: str
    used_date: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_id = self.domain_id

        domain_type = self.domain_type.value

        downloaded_date: None | str
        if isinstance(self.downloaded_date, datetime.datetime):
            downloaded_date = self.downloaded_date.isoformat()
        else:
            downloaded_date = self.downloaded_date

        expiry_date: None | str
        if isinstance(self.expiry_date, datetime.datetime):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        is_queued = self.is_queued

        person_id = self.person_id

        sent_date: None | str
        if isinstance(self.sent_date, datetime.datetime):
            sent_date = self.sent_date.isoformat()
        else:
            sent_date = self.sent_date

        token = self.token

        used_date: None | str
        if isinstance(self.used_date, datetime.datetime):
            used_date = self.used_date.isoformat()
        else:
            used_date = self.used_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainId": domain_id,
                "domainType": domain_type,
                "downloadedDate": downloaded_date,
                "expiryDate": expiry_date,
                "isQueued": is_queued,
                "personId": person_id,
                "sentDate": sent_date,
                "token": token,
                "usedDate": used_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_id = d.pop("domainId")

        domain_type = GroupQRCodeCheckinDomainType(d.pop("domainType"))

        def _parse_downloaded_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                downloaded_date_type_0 = isoparse(data)

                return downloaded_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None, data)

        downloaded_date = _parse_downloaded_date(d.pop("downloadedDate"))

        def _parse_expiry_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = isoparse(data)

                return expiry_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None, data)

        expiry_date = _parse_expiry_date(d.pop("expiryDate"))

        is_queued = d.pop("isQueued")

        person_id = d.pop("personId")

        def _parse_sent_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sent_date_type_0 = isoparse(data)

                return sent_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None, data)

        sent_date = _parse_sent_date(d.pop("sentDate"))

        token = d.pop("token")

        def _parse_used_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                used_date_type_0 = isoparse(data)

                return used_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None, data)

        used_date = _parse_used_date(d.pop("usedDate"))

        group_qr_code_checkin = cls(
            domain_id=domain_id,
            domain_type=domain_type,
            downloaded_date=downloaded_date,
            expiry_date=expiry_date,
            is_queued=is_queued,
            person_id=person_id,
            sent_date=sent_date,
            token=token,
            used_date=used_date,
        )

        group_qr_code_checkin.additional_properties = d
        return group_qr_code_checkin

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
