from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGroupStatisticsResponse200DataUnfiltered")


@_attrs_define
class GetGroupStatisticsResponse200DataUnfiltered:
    """
    Attributes:
        all_places (int): Count of all members (excluding hidden roles and to delete)
        free_places (int | None): Count of free places in group
        requested_places (int): Count of requested places
        taken_places (int): Count of taken places in group
        waitinglist_places (int): Count of people on waiting list
    """

    all_places: int
    free_places: int | None
    requested_places: int
    taken_places: int
    waitinglist_places: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_places = self.all_places

        free_places: int | None
        free_places = self.free_places

        requested_places = self.requested_places

        taken_places = self.taken_places

        waitinglist_places = self.waitinglist_places

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allPlaces": all_places,
                "freePlaces": free_places,
                "requestedPlaces": requested_places,
                "takenPlaces": taken_places,
                "waitinglistPlaces": waitinglist_places,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_places = d.pop("allPlaces")

        def _parse_free_places(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        free_places = _parse_free_places(d.pop("freePlaces"))

        requested_places = d.pop("requestedPlaces")

        taken_places = d.pop("takenPlaces")

        waitinglist_places = d.pop("waitinglistPlaces")

        get_group_statistics_response_200_data_unfiltered = cls(
            all_places=all_places,
            free_places=free_places,
            requested_places=requested_places,
            taken_places=taken_places,
            waitinglist_places=waitinglist_places,
        )

        get_group_statistics_response_200_data_unfiltered.additional_properties = d
        return get_group_statistics_response_200_data_unfiltered

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
