from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateCampusBodyServicesItem")


@_attrs_define
class UpdateCampusBodyServicesItem:
    """
    Attributes:
        day (int):
        note (str):
        repetition (str):
        time (str):
    """

    day: int
    note: str
    repetition: str
    time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        note = self.note

        repetition = self.repetition

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "note": note,
                "repetition": repetition,
                "time": time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = d.pop("day")

        note = d.pop("note")

        repetition = d.pop("repetition")

        time = d.pop("time")

        update_campus_body_services_item = cls(
            day=day,
            note=note,
            repetition=repetition,
            time=time,
        )

        update_campus_body_services_item.additional_properties = d
        return update_campus_body_services_item

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
