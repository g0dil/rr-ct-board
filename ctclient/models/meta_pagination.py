from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meta_pagination_pagination import MetaPaginationPagination


T = TypeVar("T", bound="MetaPagination")


@_attrs_define
class MetaPagination:
    """
    Attributes:
        all_ (int | Unset):
        count (int | Unset):
        pagination (MetaPaginationPagination | Unset):
    """

    all_: int | Unset = UNSET
    count: int | Unset = UNSET
    pagination: MetaPaginationPagination | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        count = self.count

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if count is not UNSET:
            field_dict["count"] = count
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta_pagination_pagination import MetaPaginationPagination

        d = dict(src_dict)
        all_ = d.pop("all", UNSET)

        count = d.pop("count", UNSET)

        _pagination = d.pop("pagination", UNSET)
        pagination: MetaPaginationPagination | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = MetaPaginationPagination.from_dict(_pagination)

        meta_pagination = cls(
            all_=all_,
            count=count,
            pagination=pagination,
        )

        meta_pagination.additional_properties = d
        return meta_pagination

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
