from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostPersonsAbsencesBody")


@_attrs_define
class PostPersonsAbsencesBody:
    """
    Attributes:
        absence_reason_id (int): ID of absence reason. Example: 1.
        comment (str):  Example: Vaccation with Family.
        end_date (datetime.date | Unset): Date used for all-day absences. If endTime is present, endDate is ignored.
            Example: 2020-11-15.
        end_time (datetime.datetime | Unset):  Example: 2020-11-30T15:00:00Z.
        start_date (datetime.date | Unset): Date used for all-day absences. If startTime is present, startDate is
            ignored. Example: 2020-11-12.
        start_time (datetime.datetime | Unset):  Example: 2020-11-20T15:00:00Z.
    """

    absence_reason_id: int
    comment: str
    end_date: datetime.date | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        absence_reason_id = self.absence_reason_id

        comment = self.comment

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "absenceReasonId": absence_reason_id,
                "comment": comment,
            }
        )
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        absence_reason_id = d.pop("absenceReasonId")

        comment = d.pop("comment")

        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        _end_time = d.pop("endTime", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        post_persons_absences_body = cls(
            absence_reason_id=absence_reason_id,
            comment=comment,
            end_date=end_date,
            end_time=end_time,
            start_date=start_date,
            start_time=start_time,
        )

        post_persons_absences_body.additional_properties = d
        return post_persons_absences_body

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
