from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteEventsBody")


@_attrs_define
class DeleteEventsBody:
    """
    Attributes:
        dry_run (bool | Unset):
        send_mail (bool | Unset):
    """

    dry_run: bool | Unset = UNSET
    send_mail: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dry_run = self.dry_run

        send_mail = self.send_mail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if send_mail is not UNSET:
            field_dict["sendMail"] = send_mail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dry_run = d.pop("dryRun", UNSET)

        send_mail = d.pop("sendMail", UNSET)

        delete_events_body = cls(
            dry_run=dry_run,
            send_mail=send_mail,
        )

        delete_events_body.additional_properties = d
        return delete_events_body

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
