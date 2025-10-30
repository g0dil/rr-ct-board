from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_chat_response_200_data_status import (
    UpdateChatResponse200DataStatus,
)

T = TypeVar("T", bound="UpdateChatResponse200Data")


@_attrs_define
class UpdateChatResponse200Data:
    """
    Example:
        {'creator': 1, 'domainId': 9, 'guid': '681F54E3-2EB7-40A4-84F0-EFF8E8F05727', 'prefix': 'ctg', 'roomname':
            'Technik', 'status': 'STARTED'}

    Attributes:
        creator (int | None):
        domain_id (int):
        guid (str):
        prefix (str):
        roomname (None | str):
        status (UpdateChatResponse200DataStatus): status of chat room Example: STARTED.
    """

    creator: int | None
    domain_id: int
    guid: str
    prefix: str
    roomname: None | str
    status: UpdateChatResponse200DataStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator: int | None
        creator = self.creator

        domain_id = self.domain_id

        guid = self.guid

        prefix = self.prefix

        roomname: None | str
        roomname = self.roomname

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creator": creator,
                "domainId": domain_id,
                "guid": guid,
                "prefix": prefix,
                "roomname": roomname,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_creator(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        creator = _parse_creator(d.pop("creator"))

        domain_id = d.pop("domainId")

        guid = d.pop("guid")

        prefix = d.pop("prefix")

        def _parse_roomname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        roomname = _parse_roomname(d.pop("roomname"))

        status = UpdateChatResponse200DataStatus(d.pop("status"))

        update_chat_response_200_data = cls(
            creator=creator,
            domain_id=domain_id,
            guid=guid,
            prefix=prefix,
            roomname=roomname,
            status=status,
        )

        update_chat_response_200_data.additional_properties = d
        return update_chat_response_200_data

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
