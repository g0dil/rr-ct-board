from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAllLogsResponse200Log")


@_attrs_define
class GetAllLogsResponse200Log:
    """ChurchTools writes log messages for many events and changes. This can be an update for a person or the deletion of
    an event. You can use the log to debug your system and follow error messages. This is a versitile tool.

        Attributes:
            date (datetime.datetime | Unset): Timestamp of log Example: 2020-05-01T20:07:36Z.
            domain_id (int | Unset): Analog to the domain type, the ID is the explicit resource. Example: 1.
            domain_type (str | Unset): The domain type tells us, where in ChurchTools the action was performed. Example:
                mail.
            id (int | Unset):  Example: 2.
            level (int | Unset): The log level indicates the importance. 1 = Warning, 2 = Notice, 3 = Info. Example: 1.
            message (str | Unset):  Example: Help page called: 0:main (1).
            person_id (int | Unset): If the person ID is `-1`, that means, no person but the system itself has logged that
                message. Example: 2.
            simulate_person_id (int | None | Unset): If a person is simulated by an administrator, we log the personId as
                well. This makes it possible to see if a person did the action or an admin, who simulated that person. Example:
                5.
    """

    date: datetime.datetime | Unset = UNSET
    domain_id: int | Unset = UNSET
    domain_type: str | Unset = UNSET
    id: int | Unset = UNSET
    level: int | Unset = UNSET
    message: str | Unset = UNSET
    person_id: int | Unset = UNSET
    simulate_person_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        domain_id = self.domain_id

        domain_type = self.domain_type

        id = self.id

        level = self.level

        message = self.message

        person_id = self.person_id

        simulate_person_id: int | None | Unset
        if isinstance(self.simulate_person_id, Unset):
            simulate_person_id = UNSET
        else:
            simulate_person_id = self.simulate_person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if domain_id is not UNSET:
            field_dict["domainId"] = domain_id
        if domain_type is not UNSET:
            field_dict["domainType"] = domain_type
        if id is not UNSET:
            field_dict["id"] = id
        if level is not UNSET:
            field_dict["level"] = level
        if message is not UNSET:
            field_dict["message"] = message
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if simulate_person_id is not UNSET:
            field_dict["simulatePersonId"] = simulate_person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        domain_id = d.pop("domainId", UNSET)

        domain_type = d.pop("domainType", UNSET)

        id = d.pop("id", UNSET)

        level = d.pop("level", UNSET)

        message = d.pop("message", UNSET)

        person_id = d.pop("personId", UNSET)

        def _parse_simulate_person_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        simulate_person_id = _parse_simulate_person_id(d.pop("simulatePersonId", UNSET))

        get_all_logs_response_200_log = cls(
            date=date,
            domain_id=domain_id,
            domain_type=domain_type,
            id=id,
            level=level,
            message=message,
            person_id=person_id,
            simulate_person_id=simulate_person_id,
        )

        get_all_logs_response_200_log.additional_properties = d
        return get_all_logs_response_200_log

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
