from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar(
    "T",
    bound="PostPersonIdEventsEventIdServicesServiceIdExchangerequestsBodyRequestingPersonPrivacyPolicyAgreement",
)


@_attrs_define
class PostPersonIdEventsEventIdServicesServiceIdExchangerequestsBodyRequestingPersonPrivacyPolicyAgreement:
    """
    Attributes:
        date (datetime.date | None): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
        type_id (int | None):
        who_id (int | None):
    """

    date: datetime.date | None
    type_id: int | None
    who_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: None | str
        if isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        type_id: int | None
        type_id = self.type_id

        who_id: int | None
        who_id = self.who_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "typeId": type_id,
                "whoId": who_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data).date()

                return date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None, data)

        date = _parse_date(d.pop("date"))

        def _parse_type_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        type_id = _parse_type_id(d.pop("typeId"))

        def _parse_who_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        who_id = _parse_who_id(d.pop("whoId"))

        post_person_id_events_event_id_services_service_id_exchangerequests_body_requesting_person_privacy_policy_agreement = cls(
            date=date,
            type_id=type_id,
            who_id=who_id,
        )

        post_person_id_events_event_id_services_service_id_exchangerequests_body_requesting_person_privacy_policy_agreement.additional_properties = d
        return post_person_id_events_event_id_services_service_id_exchangerequests_body_requesting_person_privacy_policy_agreement

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
