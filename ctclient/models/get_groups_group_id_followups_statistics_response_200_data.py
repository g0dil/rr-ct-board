from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGroupsGroupIdFollowupsStatisticsResponse200Data")


@_attrs_define
class GetGroupsGroupIdFollowupsStatisticsResponse200Data:
    """
    Attributes:
        count_done (int): Number of follow-ups already completed Example: 19.
        count_due_after_today (int): Number of pending follow-ups due after today Example: 7.
        count_due_before_today (int): Number of pending follow-ups due before today (aka 'overdue') Example: 1.
        count_due_today (int): Number of pending follow-ups due today Example: 1.
        count_due_unspecified (int): Number of pending follow-ups without due date Example: 3.
    """

    count_done: int
    count_due_after_today: int
    count_due_before_today: int
    count_due_today: int
    count_due_unspecified: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count_done = self.count_done

        count_due_after_today = self.count_due_after_today

        count_due_before_today = self.count_due_before_today

        count_due_today = self.count_due_today

        count_due_unspecified = self.count_due_unspecified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "countDone": count_done,
                "countDueAfterToday": count_due_after_today,
                "countDueBeforeToday": count_due_before_today,
                "countDueToday": count_due_today,
                "countDueUnspecified": count_due_unspecified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count_done = d.pop("countDone")

        count_due_after_today = d.pop("countDueAfterToday")

        count_due_before_today = d.pop("countDueBeforeToday")

        count_due_today = d.pop("countDueToday")

        count_due_unspecified = d.pop("countDueUnspecified")

        get_groups_group_id_followups_statistics_response_200_data = cls(
            count_done=count_done,
            count_due_after_today=count_due_after_today,
            count_due_before_today=count_due_before_today,
            count_due_today=count_due_today,
            count_due_unspecified=count_due_unspecified,
        )

        get_groups_group_id_followups_statistics_response_200_data.additional_properties = d
        return get_groups_group_id_followups_statistics_response_200_data

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
