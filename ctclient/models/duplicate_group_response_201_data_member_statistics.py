from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DuplicateGroupResponse201DataMemberStatistics")


@_attrs_define
class DuplicateGroupResponse201DataMemberStatistics:
    """
    Attributes:
        active (float):
        leaders (float):
        participants (float):
        requested (float):
        seats_taken (float):
        to_delete (float):
        waiting (float):
    """

    active: float
    leaders: float
    participants: float
    requested: float
    seats_taken: float
    to_delete: float
    waiting: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        leaders = self.leaders

        participants = self.participants

        requested = self.requested

        seats_taken = self.seats_taken

        to_delete = self.to_delete

        waiting = self.waiting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "leaders": leaders,
                "participants": participants,
                "requested": requested,
                "seatsTaken": seats_taken,
                "to_delete": to_delete,
                "waiting": waiting,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        leaders = d.pop("leaders")

        participants = d.pop("participants")

        requested = d.pop("requested")

        seats_taken = d.pop("seatsTaken")

        to_delete = d.pop("to_delete")

        waiting = d.pop("waiting")

        duplicate_group_response_201_data_member_statistics = cls(
            active=active,
            leaders=leaders,
            participants=participants,
            requested=requested,
            seats_taken=seats_taken,
            to_delete=to_delete,
            waiting=waiting,
        )

        duplicate_group_response_201_data_member_statistics.additional_properties = d
        return duplicate_group_response_201_data_member_statistics

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
