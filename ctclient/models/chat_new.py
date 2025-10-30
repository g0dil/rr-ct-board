from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChatNew")


@_attrs_define
class ChatNew:
    """
    Example:
        {'domainId': 9, 'guid': '681F54E3-2EB7-40A4-84F0-EFF8E8F05727', 'prefix': 'ctg', 'roomname': 'Technik'}

    Attributes:
        domain_id (int):
        guid (str):
        prefix (str):
        roomname (str):
    """

    domain_id: int
    guid: str
    prefix: str
    roomname: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_id = self.domain_id

        guid = self.guid

        prefix = self.prefix

        roomname = self.roomname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainId": domain_id,
                "guid": guid,
                "prefix": prefix,
                "roomname": roomname,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_id = d.pop("domainId")

        guid = d.pop("guid")

        prefix = d.pop("prefix")

        roomname = d.pop("roomname")

        chat_new = cls(
            domain_id=domain_id,
            guid=guid,
            prefix=prefix,
            roomname=roomname,
        )

        chat_new.additional_properties = d
        return chat_new

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
