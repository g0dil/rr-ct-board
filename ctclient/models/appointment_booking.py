from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppointmentBooking")


@_attrs_define
class AppointmentBooking:
    """
    Attributes:
        id (int | Unset):
        minpost (str | Unset):
        minpre (str | Unset):
        resource_id (str | Unset):
        status_id (int | Unset):
    """

    id: int | Unset = UNSET
    minpost: str | Unset = UNSET
    minpre: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    status_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        minpost = self.minpost

        minpre = self.minpre

        resource_id = self.resource_id

        status_id = self.status_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if minpost is not UNSET:
            field_dict["minpost"] = minpost
        if minpre is not UNSET:
            field_dict["minpre"] = minpre
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if status_id is not UNSET:
            field_dict["status_id"] = status_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        minpost = d.pop("minpost", UNSET)

        minpre = d.pop("minpre", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        status_id = d.pop("status_id", UNSET)

        appointment_booking = cls(
            id=id,
            minpost=minpost,
            minpre=minpre,
            resource_id=resource_id,
            status_id=status_id,
        )

        appointment_booking.additional_properties = d
        return appointment_booking

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
