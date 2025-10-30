from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatUpdate")


@_attrs_define
class ChatUpdate:
    """
    Example:
        {'creator': 1, 'domainId': 9, 'prefix': 'ctg', 'roomname': 'Technik', 'status': 'STARTED'}

    Attributes:
        creator (int | Unset):
        domain_id (int | Unset):
        prefix (str | Unset):
        roomname (str | Unset):
        status (str | Unset):
    """

    creator: int | Unset = UNSET
    domain_id: int | Unset = UNSET
    prefix: str | Unset = UNSET
    roomname: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator = self.creator

        domain_id = self.domain_id

        prefix = self.prefix

        roomname = self.roomname

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator is not UNSET:
            field_dict["creator"] = creator
        if domain_id is not UNSET:
            field_dict["domainId"] = domain_id
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if roomname is not UNSET:
            field_dict["roomname"] = roomname
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator = d.pop("creator", UNSET)

        domain_id = d.pop("domainId", UNSET)

        prefix = d.pop("prefix", UNSET)

        roomname = d.pop("roomname", UNSET)

        status = d.pop("status", UNSET)

        chat_update = cls(
            creator=creator,
            domain_id=domain_id,
            prefix=prefix,
            roomname=roomname,
            status=status,
        )

        chat_update.additional_properties = d
        return chat_update

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
