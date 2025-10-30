from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPersonMasterdataResponse200DataFollowUpIntervalsItem")


@_attrs_define
class GetPersonMasterdataResponse200DataFollowUpIntervalsItem:
    """
    Attributes:
        count (int):  Example: 1.
        days_diff (int):  Example: 7.
        follow_up_id (int):  Example: 1.
        id (int):  Example: 1.
        info (str | Unset):  Example: Anruf 1 soll erfolgen.<br>Bitte sei nett zu der Person:).
    """

    count: int
    days_diff: int
    follow_up_id: int
    id: int
    info: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        days_diff = self.days_diff

        follow_up_id = self.follow_up_id

        id = self.id

        info = self.info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "daysDiff": days_diff,
                "followUpId": follow_up_id,
                "id": id,
            }
        )
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        days_diff = d.pop("daysDiff")

        follow_up_id = d.pop("followUpId")

        id = d.pop("id")

        info = d.pop("info", UNSET)

        get_person_masterdata_response_200_data_follow_up_intervals_item = cls(
            count=count,
            days_diff=days_diff,
            follow_up_id=follow_up_id,
            id=id,
            info=info,
        )

        get_person_masterdata_response_200_data_follow_up_intervals_item.additional_properties = d
        return get_person_masterdata_response_200_data_follow_up_intervals_item

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
