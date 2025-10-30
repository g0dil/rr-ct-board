from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_sync_executions_response_200_meta_pagination import (
        GetSyncExecutionsResponse200MetaPagination,
    )


T = TypeVar("T", bound="GetSyncExecutionsResponse200Meta")


@_attrs_define
class GetSyncExecutionsResponse200Meta:
    """
    Attributes:
        count (int):
        pagination (GetSyncExecutionsResponse200MetaPagination):
    """

    count: int
    pagination: GetSyncExecutionsResponse200MetaPagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sync_executions_response_200_meta_pagination import (
            GetSyncExecutionsResponse200MetaPagination,
        )

        d = dict(src_dict)
        count = d.pop("count")

        pagination = GetSyncExecutionsResponse200MetaPagination.from_dict(
            d.pop("pagination")
        )

        get_sync_executions_response_200_meta = cls(
            count=count,
            pagination=pagination,
        )

        get_sync_executions_response_200_meta.additional_properties = d
        return get_sync_executions_response_200_meta

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
