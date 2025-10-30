from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.calculate_booking_conflicts_response_200_data_item_status_id import (
    CalculateBookingConflictsResponse200DataItemStatusId,
)

T = TypeVar("T", bound="CalculateBookingConflictsResponse200DataItem")


@_attrs_define
class CalculateBookingConflictsResponse200DataItem:
    """
    Attributes:
        booking_id (int):
        end_date (datetime.datetime): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        start_date (datetime.datetime): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        status_id (CalculateBookingConflictsResponse200DataItemStatusId): 1 = PENDING, 2 = CONFIRMED, 3 = CANCELED, 99 =
            DELETED
        title (str):
    """

    booking_id: int
    end_date: datetime.datetime
    start_date: datetime.datetime
    status_id: CalculateBookingConflictsResponse200DataItemStatusId
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        booking_id = self.booking_id

        end_date = self.end_date.isoformat()

        start_date = self.start_date.isoformat()

        status_id = self.status_id.value

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookingId": booking_id,
                "endDate": end_date,
                "startDate": start_date,
                "statusId": status_id,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        booking_id = d.pop("bookingId")

        end_date = isoparse(d.pop("endDate"))

        start_date = isoparse(d.pop("startDate"))

        status_id = CalculateBookingConflictsResponse200DataItemStatusId(
            d.pop("statusId")
        )

        title = d.pop("title")

        calculate_booking_conflicts_response_200_data_item = cls(
            booking_id=booking_id,
            end_date=end_date,
            start_date=start_date,
            status_id=status_id,
            title=title,
        )

        calculate_booking_conflicts_response_200_data_item.additional_properties = d
        return calculate_booking_conflicts_response_200_data_item

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
