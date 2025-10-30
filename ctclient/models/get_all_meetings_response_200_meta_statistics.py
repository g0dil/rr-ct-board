from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAllMeetingsResponse200MetaStatistics")


@_attrs_define
class GetAllMeetingsResponse200MetaStatistics:
    """
    Attributes:
        canceled (float):
        completed (float):
        completed_and_not_canceled (float):
        not_canceled (float):
        not_completed (float):
        not_completed_and_not_canceled_and_in_future (float):
        not_completed_and_not_canceled_and_in_past (float):
        total (float):
    """

    canceled: float
    completed: float
    completed_and_not_canceled: float
    not_canceled: float
    not_completed: float
    not_completed_and_not_canceled_and_in_future: float
    not_completed_and_not_canceled_and_in_past: float
    total: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        canceled = self.canceled

        completed = self.completed

        completed_and_not_canceled = self.completed_and_not_canceled

        not_canceled = self.not_canceled

        not_completed = self.not_completed

        not_completed_and_not_canceled_and_in_future = (
            self.not_completed_and_not_canceled_and_in_future
        )

        not_completed_and_not_canceled_and_in_past = (
            self.not_completed_and_not_canceled_and_in_past
        )

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canceled": canceled,
                "completed": completed,
                "completedAndNotCanceled": completed_and_not_canceled,
                "notCanceled": not_canceled,
                "notCompleted": not_completed,
                "notCompletedAndNotCanceledAndInFuture": not_completed_and_not_canceled_and_in_future,
                "notCompletedAndNotCanceledAndInPast": not_completed_and_not_canceled_and_in_past,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        canceled = d.pop("canceled")

        completed = d.pop("completed")

        completed_and_not_canceled = d.pop("completedAndNotCanceled")

        not_canceled = d.pop("notCanceled")

        not_completed = d.pop("notCompleted")

        not_completed_and_not_canceled_and_in_future = d.pop(
            "notCompletedAndNotCanceledAndInFuture"
        )

        not_completed_and_not_canceled_and_in_past = d.pop(
            "notCompletedAndNotCanceledAndInPast"
        )

        total = d.pop("total")

        get_all_meetings_response_200_meta_statistics = cls(
            canceled=canceled,
            completed=completed,
            completed_and_not_canceled=completed_and_not_canceled,
            not_canceled=not_canceled,
            not_completed=not_completed,
            not_completed_and_not_canceled_and_in_future=not_completed_and_not_canceled_and_in_future,
            not_completed_and_not_canceled_and_in_past=not_completed_and_not_canceled_and_in_past,
            total=total,
        )

        get_all_meetings_response_200_meta_statistics.additional_properties = d
        return get_all_meetings_response_200_meta_statistics

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
