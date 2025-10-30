from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGroupsGroupIdResponse200DataFollowUp")


@_attrs_define
class GetGroupsGroupIdResponse200DataFollowUp:
    """
    Attributes:
        send_reminder_mails (bool | Unset):  Example: True.
        target_group_member_status_id (int | None | Unset):
        target_object_id (int | None | Unset):
        target_type_id (int | Unset):
        type_id (int | None | Unset):  Example: 1.
    """

    send_reminder_mails: bool | Unset = UNSET
    target_group_member_status_id: int | None | Unset = UNSET
    target_object_id: int | None | Unset = UNSET
    target_type_id: int | Unset = UNSET
    type_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        send_reminder_mails = self.send_reminder_mails

        target_group_member_status_id: int | None | Unset
        if isinstance(self.target_group_member_status_id, Unset):
            target_group_member_status_id = UNSET
        else:
            target_group_member_status_id = self.target_group_member_status_id

        target_object_id: int | None | Unset
        if isinstance(self.target_object_id, Unset):
            target_object_id = UNSET
        else:
            target_object_id = self.target_object_id

        target_type_id = self.target_type_id

        type_id: int | None | Unset
        if isinstance(self.type_id, Unset):
            type_id = UNSET
        else:
            type_id = self.type_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if send_reminder_mails is not UNSET:
            field_dict["sendReminderMails"] = send_reminder_mails
        if target_group_member_status_id is not UNSET:
            field_dict["targetGroupMemberStatusId"] = target_group_member_status_id
        if target_object_id is not UNSET:
            field_dict["targetObjectId"] = target_object_id
        if target_type_id is not UNSET:
            field_dict["targetTypeId"] = target_type_id
        if type_id is not UNSET:
            field_dict["typeId"] = type_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        send_reminder_mails = d.pop("sendReminderMails", UNSET)

        def _parse_target_group_member_status_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        target_group_member_status_id = _parse_target_group_member_status_id(
            d.pop("targetGroupMemberStatusId", UNSET)
        )

        def _parse_target_object_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        target_object_id = _parse_target_object_id(d.pop("targetObjectId", UNSET))

        target_type_id = d.pop("targetTypeId", UNSET)

        def _parse_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        type_id = _parse_type_id(d.pop("typeId", UNSET))

        get_groups_group_id_response_200_data_follow_up = cls(
            send_reminder_mails=send_reminder_mails,
            target_group_member_status_id=target_group_member_status_id,
            target_object_id=target_object_id,
            target_type_id=target_type_id,
            type_id=type_id,
        )

        get_groups_group_id_response_200_data_follow_up.additional_properties = d
        return get_groups_group_id_response_200_data_follow_up

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
