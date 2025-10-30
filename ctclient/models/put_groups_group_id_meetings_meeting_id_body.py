from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutGroupsGroupIdMeetingsMeetingIdBody")


@_attrs_define
class PutGroupsGroupIdMeetingsMeetingIdBody:
    """
    Attributes:
        comment (None | str | Unset):
        end_date (str | Unset):  Example: 2021-11-04T00:00:00Z.
        is_canceled (bool | Unset):  Default: False.
        is_completed (bool | Unset):  Default: False.
        num_guests (int | None | Unset):
        poll_result (None | str | Unset):
        start_date (str | Unset):  Example: 2021-11-04T00:00:00Z.
    """

    comment: None | str | Unset = UNSET
    end_date: str | Unset = UNSET
    is_canceled: bool | Unset = False
    is_completed: bool | Unset = False
    num_guests: int | None | Unset = UNSET
    poll_result: None | str | Unset = UNSET
    start_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        end_date = self.end_date

        is_canceled = self.is_canceled

        is_completed = self.is_completed

        num_guests: int | None | Unset
        if isinstance(self.num_guests, Unset):
            num_guests = UNSET
        else:
            num_guests = self.num_guests

        poll_result: None | str | Unset
        if isinstance(self.poll_result, Unset):
            poll_result = UNSET
        else:
            poll_result = self.poll_result

        start_date = self.start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if is_canceled is not UNSET:
            field_dict["isCanceled"] = is_canceled
        if is_completed is not UNSET:
            field_dict["isCompleted"] = is_completed
        if num_guests is not UNSET:
            field_dict["numGuests"] = num_guests
        if poll_result is not UNSET:
            field_dict["pollResult"] = poll_result
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        end_date = d.pop("endDate", UNSET)

        is_canceled = d.pop("isCanceled", UNSET)

        is_completed = d.pop("isCompleted", UNSET)

        def _parse_num_guests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_guests = _parse_num_guests(d.pop("numGuests", UNSET))

        def _parse_poll_result(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poll_result = _parse_poll_result(d.pop("pollResult", UNSET))

        start_date = d.pop("startDate", UNSET)

        put_groups_group_id_meetings_meeting_id_body = cls(
            comment=comment,
            end_date=end_date,
            is_canceled=is_canceled,
            is_completed=is_completed,
            num_guests=num_guests,
            poll_result=poll_result,
            start_date=start_date,
        )

        put_groups_group_id_meetings_meeting_id_body.additional_properties = d
        return put_groups_group_id_meetings_meeting_id_body

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
