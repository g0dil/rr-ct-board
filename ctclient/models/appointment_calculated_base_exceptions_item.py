from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.appointment_calculated_base_exceptions_item_meta import (
        AppointmentCalculatedBaseExceptionsItemMeta,
    )


T = TypeVar("T", bound="AppointmentCalculatedBaseExceptionsItem")


@_attrs_define
class AppointmentCalculatedBaseExceptionsItem:
    """
    Attributes:
        date (datetime.date):  Example: 2022-01-01.
        id (int):  Example: 1.
        meta (AppointmentCalculatedBaseExceptionsItemMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z',
            'createdPerson': {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
    """

    date: datetime.date
    id: int
    meta: AppointmentCalculatedBaseExceptionsItemMeta
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        id = self.id

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "id": id,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appointment_calculated_base_exceptions_item_meta import (
            AppointmentCalculatedBaseExceptionsItemMeta,
        )

        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()

        id = d.pop("id")

        meta = AppointmentCalculatedBaseExceptionsItemMeta.from_dict(d.pop("meta"))

        appointment_calculated_base_exceptions_item = cls(
            date=date,
            id=id,
            meta=meta,
        )

        appointment_calculated_base_exceptions_item.additional_properties = d
        return appointment_calculated_base_exceptions_item

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
