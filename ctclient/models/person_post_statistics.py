from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonPostStatistics")


@_attrs_define
class PersonPostStatistics:
    """
    Attributes:
        count_banned (float):
        count_expiration_future (float):
        count_expiration_past (float):
        count_publication_future (float):
        count_published (float):
        total (float | Unset):
    """

    count_banned: float
    count_expiration_future: float
    count_expiration_past: float
    count_publication_future: float
    count_published: float
    total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count_banned = self.count_banned

        count_expiration_future = self.count_expiration_future

        count_expiration_past = self.count_expiration_past

        count_publication_future = self.count_publication_future

        count_published = self.count_published

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "countBanned": count_banned,
                "countExpirationFuture": count_expiration_future,
                "countExpirationPast": count_expiration_past,
                "countPublicationFuture": count_publication_future,
                "countPublished": count_published,
            }
        )
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count_banned = d.pop("countBanned")

        count_expiration_future = d.pop("countExpirationFuture")

        count_expiration_past = d.pop("countExpirationPast")

        count_publication_future = d.pop("countPublicationFuture")

        count_published = d.pop("countPublished")

        total = d.pop("total", UNSET)

        person_post_statistics = cls(
            count_banned=count_banned,
            count_expiration_future=count_expiration_future,
            count_expiration_past=count_expiration_past,
            count_publication_future=count_publication_future,
            count_published=count_published,
            total=total,
        )

        person_post_statistics.additional_properties = d
        return person_post_statistics

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
