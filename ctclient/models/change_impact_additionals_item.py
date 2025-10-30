from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.change_impact_additionals_item_meta import (
        ChangeImpactAdditionalsItemMeta,
    )


T = TypeVar("T", bound="ChangeImpactAdditionalsItem")


@_attrs_define
class ChangeImpactAdditionalsItem:
    """
    Attributes:
        date (datetime.date): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
        id (int):
        is_repeated (bool):
        meta (ChangeImpactAdditionalsItemMeta):
    """

    date: datetime.date
    id: int
    is_repeated: bool
    meta: ChangeImpactAdditionalsItemMeta
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        id = self.id

        is_repeated = self.is_repeated

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "id": id,
                "isRepeated": is_repeated,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_impact_additionals_item_meta import (
            ChangeImpactAdditionalsItemMeta,
        )

        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()

        id = d.pop("id")

        is_repeated = d.pop("isRepeated")

        meta = ChangeImpactAdditionalsItemMeta.from_dict(d.pop("meta"))

        change_impact_additionals_item = cls(
            date=date,
            id=id,
            is_repeated=is_repeated,
            meta=meta,
        )

        change_impact_additionals_item.additional_properties = d
        return change_impact_additionals_item

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
