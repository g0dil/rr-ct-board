from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckinBody")


@_attrs_define
class CheckinBody:
    """Either groupMeetingId or date must be provided. If only date is provided it will try to find a meeting at that date
    or else create a new one.

        Attributes:
            date (datetime.datetime | None | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
                2022-10-19T12:00:00Z.
            group_meeting_id (int | None | Unset):
            printer_id (int | Unset): optional printer ID, if a name tag should be printed out
            token (str | Unset): optional token of a ticket that is to be validated
    """

    date: datetime.datetime | None | Unset = UNSET
    group_meeting_id: int | None | Unset = UNSET
    printer_id: int | Unset = UNSET
    token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        group_meeting_id: int | None | Unset
        if isinstance(self.group_meeting_id, Unset):
            group_meeting_id = UNSET
        else:
            group_meeting_id = self.group_meeting_id

        printer_id = self.printer_id

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if group_meeting_id is not UNSET:
            field_dict["groupMeetingId"] = group_meeting_id
        if printer_id is not UNSET:
            field_dict["printerId"] = printer_id
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_group_meeting_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_meeting_id = _parse_group_meeting_id(d.pop("groupMeetingId", UNSET))

        printer_id = d.pop("printerId", UNSET)

        token = d.pop("token", UNSET)

        checkin_body = cls(
            date=date,
            group_meeting_id=group_meeting_id,
            printer_id=printer_id,
            token=token,
        )

        checkin_body.additional_properties = d
        return checkin_body

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
