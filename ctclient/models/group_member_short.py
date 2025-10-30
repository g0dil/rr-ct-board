from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupMemberShort")


@_attrs_define
class GroupMemberShort:
    """
    Attributes:
        group_id (int | Unset):
        group_member_status (str | Unset):
        group_type_role_id (int | Unset):
        last_change (datetime.date | Unset):
        person_id (int | Unset):
    """

    group_id: int | Unset = UNSET
    group_member_status: str | Unset = UNSET
    group_type_role_id: int | Unset = UNSET
    last_change: datetime.date | Unset = UNSET
    person_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        group_member_status = self.group_member_status

        group_type_role_id = self.group_type_role_id

        last_change: str | Unset = UNSET
        if not isinstance(self.last_change, Unset):
            last_change = self.last_change.isoformat()

        person_id = self.person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if group_member_status is not UNSET:
            field_dict["groupMemberStatus"] = group_member_status
        if group_type_role_id is not UNSET:
            field_dict["groupTypeRoleId"] = group_type_role_id
        if last_change is not UNSET:
            field_dict["lastChange"] = last_change
        if person_id is not UNSET:
            field_dict["personId"] = person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = d.pop("groupId", UNSET)

        group_member_status = d.pop("groupMemberStatus", UNSET)

        group_type_role_id = d.pop("groupTypeRoleId", UNSET)

        _last_change = d.pop("lastChange", UNSET)
        last_change: datetime.date | Unset
        if isinstance(_last_change, Unset):
            last_change = UNSET
        else:
            last_change = isoparse(_last_change).date()

        person_id = d.pop("personId", UNSET)

        group_member_short = cls(
            group_id=group_id,
            group_member_status=group_member_status,
            group_type_role_id=group_type_role_id,
            last_change=last_change,
            person_id=person_id,
        )

        group_member_short.additional_properties = d
        return group_member_short

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
