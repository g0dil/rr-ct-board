from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteEventEventserviceBody")


@_attrs_define
class DeleteEventEventserviceBody:
    """
    Attributes:
        event_id (int):
        event_service_id (int):
        comment (str | Unset):
    """

    event_id: int
    event_service_id: int
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        event_service_id = self.event_service_id

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventId": event_id,
                "eventServiceId": event_service_id,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_id = d.pop("eventId")

        event_service_id = d.pop("eventServiceId")

        comment = d.pop("comment", UNSET)

        delete_event_eventservice_body = cls(
            event_id=event_id,
            event_service_id=event_service_id,
            comment=comment,
        )

        delete_event_eventservice_body.additional_properties = d
        return delete_event_eventservice_body

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
