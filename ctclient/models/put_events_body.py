from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutEventsBody")


@_attrs_define
class PutEventsBody:
    """
    Attributes:
        event_id (int):
        admin_ids (list[int] | Unset):
        is_canceled (bool | Unset):
        note (str | Unset):
    """

    event_id: int
    admin_ids: list[int] | Unset = UNSET
    is_canceled: bool | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        admin_ids: list[int] | Unset = UNSET
        if not isinstance(self.admin_ids, Unset):
            admin_ids = self.admin_ids

        is_canceled = self.is_canceled

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventId": event_id,
            }
        )
        if admin_ids is not UNSET:
            field_dict["adminIds"] = admin_ids
        if is_canceled is not UNSET:
            field_dict["isCanceled"] = is_canceled
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_id = d.pop("eventId")

        admin_ids = cast(list[int], d.pop("adminIds", UNSET))

        is_canceled = d.pop("isCanceled", UNSET)

        note = d.pop("note", UNSET)

        put_events_body = cls(
            event_id=event_id,
            admin_ids=admin_ids,
            is_canceled=is_canceled,
            note=note,
        )

        put_events_body.additional_properties = d
        return put_events_body

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
