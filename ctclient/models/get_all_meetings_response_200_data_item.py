from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_all_meetings_response_200_data_item_attendances import (
        GetAllMeetingsResponse200DataItemAttendances,
    )
    from ..models.get_all_meetings_response_200_data_item_date_from import (
        GetAllMeetingsResponse200DataItemDateFrom,
    )
    from ..models.get_all_meetings_response_200_data_item_date_to import (
        GetAllMeetingsResponse200DataItemDateTo,
    )
    from ..models.get_all_meetings_response_200_data_item_end_date import (
        GetAllMeetingsResponse200DataItemEndDate,
    )
    from ..models.get_all_meetings_response_200_data_item_meta import (
        GetAllMeetingsResponse200DataItemMeta,
    )
    from ..models.get_all_meetings_response_200_data_item_poll_result_type_0_item import (
        GetAllMeetingsResponse200DataItemPollResultType0Item,
    )
    from ..models.get_all_meetings_response_200_data_item_start_date import (
        GetAllMeetingsResponse200DataItemStartDate,
    )
    from ..models.get_all_meetings_response_200_data_item_statistics import (
        GetAllMeetingsResponse200DataItemStatistics,
    )


T = TypeVar("T", bound="GetAllMeetingsResponse200DataItem")


@_attrs_define
class GetAllMeetingsResponse200DataItem:
    """
    Attributes:
        end_date (GetAllMeetingsResponse200DataItemEndDate): End of the group meeting
        group_id (int):
        id (int):
        meta (GetAllMeetingsResponse200DataItemMeta):
        start_date (GetAllMeetingsResponse200DataItemStartDate): Start of the group meeting
        statistics (GetAllMeetingsResponse200DataItemStatistics):
        attendances (GetAllMeetingsResponse200DataItemAttendances | Unset): Map of person IDs to attendance status
        comment (None | str | Unset):
        date_from (GetAllMeetingsResponse200DataItemDateFrom | Unset):
        date_to (GetAllMeetingsResponse200DataItemDateTo | Unset):
        has_editing_started (bool | Unset):
        is_canceled (bool | Unset):
        is_completed (bool | Unset):
        num_guests (int | None | Unset):
        poll_result (list[GetAllMeetingsResponse200DataItemPollResultType0Item] | None | Unset):
    """

    end_date: GetAllMeetingsResponse200DataItemEndDate
    group_id: int
    id: int
    meta: GetAllMeetingsResponse200DataItemMeta
    start_date: GetAllMeetingsResponse200DataItemStartDate
    statistics: GetAllMeetingsResponse200DataItemStatistics
    attendances: GetAllMeetingsResponse200DataItemAttendances | Unset = UNSET
    comment: None | str | Unset = UNSET
    date_from: GetAllMeetingsResponse200DataItemDateFrom | Unset = UNSET
    date_to: GetAllMeetingsResponse200DataItemDateTo | Unset = UNSET
    has_editing_started: bool | Unset = UNSET
    is_canceled: bool | Unset = UNSET
    is_completed: bool | Unset = UNSET
    num_guests: int | None | Unset = UNSET
    poll_result: (
        list[GetAllMeetingsResponse200DataItemPollResultType0Item] | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date.to_dict()

        group_id = self.group_id

        id = self.id

        meta = self.meta.to_dict()

        start_date = self.start_date.to_dict()

        statistics = self.statistics.to_dict()

        attendances: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attendances, Unset):
            attendances = self.attendances.to_dict()

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        date_from: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_from, Unset):
            date_from = self.date_from.to_dict()

        date_to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_to, Unset):
            date_to = self.date_to.to_dict()

        has_editing_started = self.has_editing_started

        is_canceled = self.is_canceled

        is_completed = self.is_completed

        num_guests: int | None | Unset
        if isinstance(self.num_guests, Unset):
            num_guests = UNSET
        else:
            num_guests = self.num_guests

        poll_result: list[dict[str, Any]] | None | Unset
        if isinstance(self.poll_result, Unset):
            poll_result = UNSET
        elif isinstance(self.poll_result, list):
            poll_result = []
            for poll_result_type_0_item_data in self.poll_result:
                poll_result_type_0_item = poll_result_type_0_item_data.to_dict()
                poll_result.append(poll_result_type_0_item)

        else:
            poll_result = self.poll_result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endDate": end_date,
                "groupId": group_id,
                "id": id,
                "meta": meta,
                "startDate": start_date,
                "statistics": statistics,
            }
        )
        if attendances is not UNSET:
            field_dict["attendances"] = attendances
        if comment is not UNSET:
            field_dict["comment"] = comment
        if date_from is not UNSET:
            field_dict["dateFrom"] = date_from
        if date_to is not UNSET:
            field_dict["dateTo"] = date_to
        if has_editing_started is not UNSET:
            field_dict["hasEditingStarted"] = has_editing_started
        if is_canceled is not UNSET:
            field_dict["isCanceled"] = is_canceled
        if is_completed is not UNSET:
            field_dict["isCompleted"] = is_completed
        if num_guests is not UNSET:
            field_dict["numGuests"] = num_guests
        if poll_result is not UNSET:
            field_dict["pollResult"] = poll_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_all_meetings_response_200_data_item_attendances import (
            GetAllMeetingsResponse200DataItemAttendances,
        )
        from ..models.get_all_meetings_response_200_data_item_date_from import (
            GetAllMeetingsResponse200DataItemDateFrom,
        )
        from ..models.get_all_meetings_response_200_data_item_date_to import (
            GetAllMeetingsResponse200DataItemDateTo,
        )
        from ..models.get_all_meetings_response_200_data_item_end_date import (
            GetAllMeetingsResponse200DataItemEndDate,
        )
        from ..models.get_all_meetings_response_200_data_item_meta import (
            GetAllMeetingsResponse200DataItemMeta,
        )
        from ..models.get_all_meetings_response_200_data_item_poll_result_type_0_item import (
            GetAllMeetingsResponse200DataItemPollResultType0Item,
        )
        from ..models.get_all_meetings_response_200_data_item_start_date import (
            GetAllMeetingsResponse200DataItemStartDate,
        )
        from ..models.get_all_meetings_response_200_data_item_statistics import (
            GetAllMeetingsResponse200DataItemStatistics,
        )

        d = dict(src_dict)
        end_date = GetAllMeetingsResponse200DataItemEndDate.from_dict(d.pop("endDate"))

        group_id = d.pop("groupId")

        id = d.pop("id")

        meta = GetAllMeetingsResponse200DataItemMeta.from_dict(d.pop("meta"))

        start_date = GetAllMeetingsResponse200DataItemStartDate.from_dict(
            d.pop("startDate")
        )

        statistics = GetAllMeetingsResponse200DataItemStatistics.from_dict(
            d.pop("statistics")
        )

        _attendances = d.pop("attendances", UNSET)
        attendances: GetAllMeetingsResponse200DataItemAttendances | Unset
        if isinstance(_attendances, Unset):
            attendances = UNSET
        else:
            attendances = GetAllMeetingsResponse200DataItemAttendances.from_dict(
                _attendances
            )

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        _date_from = d.pop("dateFrom", UNSET)
        date_from: GetAllMeetingsResponse200DataItemDateFrom | Unset
        if isinstance(_date_from, Unset):
            date_from = UNSET
        else:
            date_from = GetAllMeetingsResponse200DataItemDateFrom.from_dict(_date_from)

        _date_to = d.pop("dateTo", UNSET)
        date_to: GetAllMeetingsResponse200DataItemDateTo | Unset
        if isinstance(_date_to, Unset):
            date_to = UNSET
        else:
            date_to = GetAllMeetingsResponse200DataItemDateTo.from_dict(_date_to)

        has_editing_started = d.pop("hasEditingStarted", UNSET)

        is_canceled = d.pop("isCanceled", UNSET)

        is_completed = d.pop("isCompleted", UNSET)

        def _parse_num_guests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_guests = _parse_num_guests(d.pop("numGuests", UNSET))

        def _parse_poll_result(
            data: object,
        ) -> list[GetAllMeetingsResponse200DataItemPollResultType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                poll_result_type_0 = []
                _poll_result_type_0 = data
                for poll_result_type_0_item_data in _poll_result_type_0:
                    poll_result_type_0_item = (
                        GetAllMeetingsResponse200DataItemPollResultType0Item.from_dict(
                            poll_result_type_0_item_data
                        )
                    )

                    poll_result_type_0.append(poll_result_type_0_item)

                return poll_result_type_0
            except:  # noqa: E722
                pass
            return cast(
                list[GetAllMeetingsResponse200DataItemPollResultType0Item]
                | None
                | Unset,
                data,
            )

        poll_result = _parse_poll_result(d.pop("pollResult", UNSET))

        get_all_meetings_response_200_data_item = cls(
            end_date=end_date,
            group_id=group_id,
            id=id,
            meta=meta,
            start_date=start_date,
            statistics=statistics,
            attendances=attendances,
            comment=comment,
            date_from=date_from,
            date_to=date_to,
            has_editing_started=has_editing_started,
            is_canceled=is_canceled,
            is_completed=is_completed,
            num_guests=num_guests,
            poll_result=poll_result,
        )

        get_all_meetings_response_200_data_item.additional_properties = d
        return get_all_meetings_response_200_data_item

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
