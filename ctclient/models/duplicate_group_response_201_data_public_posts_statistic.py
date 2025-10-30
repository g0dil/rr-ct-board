from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="DuplicateGroupResponse201DataPublicPostsStatistic")


@_attrs_define
class DuplicateGroupResponse201DataPublicPostsStatistic:
    """
    Attributes:
        count (float):
        last_post_date (datetime.datetime | None): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
    """

    count: float
    last_post_date: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        last_post_date: None | str
        if isinstance(self.last_post_date, datetime.datetime):
            last_post_date = self.last_post_date.isoformat()
        else:
            last_post_date = self.last_post_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "lastPostDate": last_post_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        def _parse_last_post_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_post_date_type_0 = isoparse(data)

                return last_post_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None, data)

        last_post_date = _parse_last_post_date(d.pop("lastPostDate"))

        duplicate_group_response_201_data_public_posts_statistic = cls(
            count=count,
            last_post_date=last_post_date,
        )

        duplicate_group_response_201_data_public_posts_statistic.additional_properties = d
        return duplicate_group_response_201_data_public_posts_statistic

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
