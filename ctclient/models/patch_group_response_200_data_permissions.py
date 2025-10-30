from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchGroupResponse200DataPermissions")


@_attrs_define
class PatchGroupResponse200DataPermissions:
    """
    Attributes:
        start_chat (bool): Current user can start chat.
        use_chat (bool): Current user can use the chat.
    """

    start_chat: bool
    use_chat: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_chat = self.start_chat

        use_chat = self.use_chat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startChat": start_chat,
                "useChat": use_chat,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_chat = d.pop("startChat")

        use_chat = d.pop("useChat")

        patch_group_response_200_data_permissions = cls(
            start_chat=start_chat,
            use_chat=use_chat,
        )

        patch_group_response_200_data_permissions.additional_properties = d
        return patch_group_response_200_data_permissions

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
