from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.membership_update_group_member_status import (
    MembershipUpdateGroupMemberStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.membership_update_fields_type_0 import MembershipUpdateFieldsType0
    from ..models.membership_update_member_start_date import (
        MembershipUpdateMemberStartDate,
    )


T = TypeVar("T", bound="MembershipUpdate")


@_attrs_define
class MembershipUpdate:
    """
    Attributes:
        comment (None | str | Unset):
        fields (MembershipUpdateFieldsType0 | None | Unset): Group member fields as key value pairs, where the key is
            the ID of the field to be set. Example: {'12': True, '14': 'Text', '17': None}.
        group_member_status (MembershipUpdateGroupMemberStatus | Unset):
        group_type_role_id (int | Unset):
        inform_leader (bool | Unset):
        member_end_date (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        member_start_date (MembershipUpdateMemberStartDate | Unset):
        waitinglist_position (int | None | Unset):
    """

    comment: None | str | Unset = UNSET
    fields: MembershipUpdateFieldsType0 | None | Unset = UNSET
    group_member_status: MembershipUpdateGroupMemberStatus | Unset = UNSET
    group_type_role_id: int | Unset = UNSET
    inform_leader: bool | Unset = UNSET
    member_end_date: datetime.date | None | Unset = UNSET
    member_start_date: MembershipUpdateMemberStartDate | Unset = UNSET
    waitinglist_position: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.membership_update_fields_type_0 import MembershipUpdateFieldsType0

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        fields: dict[str, Any] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, MembershipUpdateFieldsType0):
            fields = self.fields.to_dict()
        else:
            fields = self.fields

        group_member_status: str | Unset = UNSET
        if not isinstance(self.group_member_status, Unset):
            group_member_status = self.group_member_status.value

        group_type_role_id: int | Unset
        if isinstance(self.group_type_role_id, Unset):
            group_type_role_id = UNSET
        else:
            group_type_role_id = self.group_type_role_id

        inform_leader: bool | Unset
        if isinstance(self.inform_leader, Unset):
            inform_leader = UNSET
        else:
            inform_leader = self.inform_leader

        member_end_date: None | str | Unset
        if isinstance(self.member_end_date, Unset):
            member_end_date = UNSET
        elif isinstance(self.member_end_date, datetime.date):
            member_end_date = self.member_end_date.isoformat()
        else:
            member_end_date = self.member_end_date

        member_start_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.member_start_date, Unset):
            member_start_date = self.member_start_date.to_dict()

        waitinglist_position: int | None | Unset
        if isinstance(self.waitinglist_position, Unset):
            waitinglist_position = UNSET
        else:
            waitinglist_position = self.waitinglist_position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if fields is not UNSET:
            field_dict["fields"] = fields
        if group_member_status is not UNSET:
            field_dict["groupMemberStatus"] = group_member_status
        if group_type_role_id is not UNSET:
            field_dict["groupTypeRoleId"] = group_type_role_id
        if inform_leader is not UNSET:
            field_dict["informLeader"] = inform_leader
        if member_end_date is not UNSET:
            field_dict["memberEndDate"] = member_end_date
        if member_start_date is not UNSET:
            field_dict["memberStartDate"] = member_start_date
        if waitinglist_position is not UNSET:
            field_dict["waitinglistPosition"] = waitinglist_position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.membership_update_fields_type_0 import MembershipUpdateFieldsType0
        from ..models.membership_update_member_start_date import (
            MembershipUpdateMemberStartDate,
        )

        d = dict(src_dict)

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_fields(data: object) -> MembershipUpdateFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fields_type_0 = MembershipUpdateFieldsType0.from_dict(data)

                return fields_type_0
            except:  # noqa: E722
                pass
            return cast(MembershipUpdateFieldsType0 | None | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))

        _group_member_status = d.pop("groupMemberStatus", UNSET)
        group_member_status: MembershipUpdateGroupMemberStatus | Unset
        if isinstance(_group_member_status, Unset):
            group_member_status = UNSET
        else:
            group_member_status = MembershipUpdateGroupMemberStatus(
                _group_member_status
            )

        def _parse_group_type_role_id(data: object) -> int | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | Unset, data)

        group_type_role_id = _parse_group_type_role_id(d.pop("groupTypeRoleId", UNSET))

        def _parse_inform_leader(data: object) -> bool | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset, data)

        inform_leader = _parse_inform_leader(d.pop("informLeader", UNSET))

        def _parse_member_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                member_end_date_type_0 = isoparse(data).date()

                return member_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        member_end_date = _parse_member_end_date(d.pop("memberEndDate", UNSET))

        _member_start_date = d.pop("memberStartDate", UNSET)
        member_start_date: MembershipUpdateMemberStartDate | Unset
        if isinstance(_member_start_date, Unset):
            member_start_date = UNSET
        else:
            member_start_date = MembershipUpdateMemberStartDate.from_dict(
                _member_start_date
            )

        def _parse_waitinglist_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        waitinglist_position = _parse_waitinglist_position(
            d.pop("waitinglistPosition", UNSET)
        )

        membership_update = cls(
            comment=comment,
            fields=fields,
            group_member_status=group_member_status,
            group_type_role_id=group_type_role_id,
            inform_leader=inform_leader,
            member_end_date=member_end_date,
            member_start_date=member_start_date,
            waitinglist_position=waitinglist_position,
        )

        membership_update.additional_properties = d
        return membership_update

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
