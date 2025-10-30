from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartStopEventChatBody")


@_attrs_define
class StartStopEventChatBody:
    """
    Attributes:
        enabled (bool | Unset):
        trigger_chat_invite_mail (bool | Unset):
    """

    enabled: bool | Unset = UNSET
    trigger_chat_invite_mail: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        trigger_chat_invite_mail = self.trigger_chat_invite_mail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if trigger_chat_invite_mail is not UNSET:
            field_dict["triggerChatInviteMail"] = trigger_chat_invite_mail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        trigger_chat_invite_mail = d.pop("triggerChatInviteMail", UNSET)

        start_stop_event_chat_body = cls(
            enabled=enabled,
            trigger_chat_invite_mail=trigger_chat_invite_mail,
        )

        start_stop_event_chat_body.additional_properties = d
        return start_stop_event_chat_body

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
