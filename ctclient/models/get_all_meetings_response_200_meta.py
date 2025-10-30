from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_all_meetings_response_200_meta_pagination import (
        GetAllMeetingsResponse200MetaPagination,
    )
    from ..models.get_all_meetings_response_200_meta_statistics import (
        GetAllMeetingsResponse200MetaStatistics,
    )


T = TypeVar("T", bound="GetAllMeetingsResponse200Meta")


@_attrs_define
class GetAllMeetingsResponse200Meta:
    """
    Attributes:
        statistics (GetAllMeetingsResponse200MetaStatistics):
        all_ (int | Unset):
        count (int | Unset):
        pagination (GetAllMeetingsResponse200MetaPagination | Unset):
    """

    statistics: GetAllMeetingsResponse200MetaStatistics
    all_: int | Unset = UNSET
    count: int | Unset = UNSET
    pagination: GetAllMeetingsResponse200MetaPagination | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statistics = self.statistics.to_dict()

        all_ = self.all_

        count = self.count

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statistics": statistics,
            }
        )
        if all_ is not UNSET:
            field_dict["all"] = all_
        if count is not UNSET:
            field_dict["count"] = count
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_all_meetings_response_200_meta_pagination import (
            GetAllMeetingsResponse200MetaPagination,
        )
        from ..models.get_all_meetings_response_200_meta_statistics import (
            GetAllMeetingsResponse200MetaStatistics,
        )

        d = dict(src_dict)
        statistics = GetAllMeetingsResponse200MetaStatistics.from_dict(
            d.pop("statistics")
        )

        all_ = d.pop("all", UNSET)

        count = d.pop("count", UNSET)

        _pagination = d.pop("pagination", UNSET)
        pagination: GetAllMeetingsResponse200MetaPagination | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = GetAllMeetingsResponse200MetaPagination.from_dict(_pagination)

        get_all_meetings_response_200_meta = cls(
            statistics=statistics,
            all_=all_,
            count=count,
            pagination=pagination,
        )

        get_all_meetings_response_200_meta.additional_properties = d
        return get_all_meetings_response_200_meta

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
