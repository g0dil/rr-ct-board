from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSyncLogsResponse200MetaPagination")


@_attrs_define
class GetSyncLogsResponse200MetaPagination:
    """
    Attributes:
        current (int | Unset):
        last_page (int | Unset):
        limit (int | Unset):
        total (int | Unset):
    """

    current: int | Unset = UNSET
    last_page: int | Unset = UNSET
    limit: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current = self.current

        last_page = self.last_page

        limit = self.limit

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current is not UNSET:
            field_dict["current"] = current
        if last_page is not UNSET:
            field_dict["lastPage"] = last_page
        if limit is not UNSET:
            field_dict["limit"] = limit
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current = d.pop("current", UNSET)

        last_page = d.pop("lastPage", UNSET)

        limit = d.pop("limit", UNSET)

        total = d.pop("total", UNSET)

        get_sync_logs_response_200_meta_pagination = cls(
            current=current,
            last_page=last_page,
            limit=limit,
            total=total,
        )

        get_sync_logs_response_200_meta_pagination.additional_properties = d
        return get_sync_logs_response_200_meta_pagination

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
