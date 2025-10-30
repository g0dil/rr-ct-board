from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.put_groups_group_id_members_person_id_body_group_member_status import (
    PutGroupsGroupIdMembersPersonIdBodyGroupMemberStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_groups_group_id_members_person_id_body_fields_type_0 import (
        PutGroupsGroupIdMembersPersonIdBodyFieldsType0,
    )
    from ..models.put_groups_group_id_members_person_id_body_member_start_date import (
        PutGroupsGroupIdMembersPersonIdBodyMemberStartDate,
    )


T = TypeVar("T", bound="PutGroupsGroupIdMembersPersonIdBody")


@_attrs_define
class PutGroupsGroupIdMembersPersonIdBody:
    """
    Attributes:
        comment (None | str | Unset):
        fields (None | PutGroupsGroupIdMembersPersonIdBodyFieldsType0 | Unset): Group member fields as key value pairs,
            where the key is the ID of the field to be set. Example: {'12': True, '14': 'Text', '17': None}.
        group_member_status (PutGroupsGroupIdMembersPersonIdBodyGroupMemberStatus | Unset):  Default:
            PutGroupsGroupIdMembersPersonIdBodyGroupMemberStatus.ACTIVE.
        group_type_role_id (int | None | Unset):
        ignore_group_full (bool | None | Unset):
        inform_leader (bool | None | Unset):
        member_end_date (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        member_start_date (PutGroupsGroupIdMembersPersonIdBodyMemberStartDate | Unset):
        only_add (bool | None | Unset):
        waitinglist_position (int | None | Unset):
    """

    comment: None | str | Unset = UNSET
    fields: None | PutGroupsGroupIdMembersPersonIdBodyFieldsType0 | Unset = UNSET
    group_member_status: (
        PutGroupsGroupIdMembersPersonIdBodyGroupMemberStatus | Unset
    ) = PutGroupsGroupIdMembersPersonIdBodyGroupMemberStatus.ACTIVE
    group_type_role_id: int | None | Unset = UNSET
    ignore_group_full: bool | None | Unset = UNSET
    inform_leader: bool | None | Unset = UNSET
    member_end_date: datetime.date | None | Unset = UNSET
    member_start_date: PutGroupsGroupIdMembersPersonIdBodyMemberStartDate | Unset = (
        UNSET
    )
    only_add: bool | None | Unset = UNSET
    waitinglist_position: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.put_groups_group_id_members_person_id_body_fields_type_0 import (
            PutGroupsGroupIdMembersPersonIdBodyFieldsType0,
        )

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        fields: dict[str, Any] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, PutGroupsGroupIdMembersPersonIdBodyFieldsType0):
            fields = self.fields.to_dict()
        else:
            fields = self.fields

        group_member_status: str | Unset = UNSET
        if not isinstance(self.group_member_status, Unset):
            group_member_status = self.group_member_status.value

        group_type_role_id: int | None | Unset
        if isinstance(self.group_type_role_id, Unset):
            group_type_role_id = UNSET
        else:
            group_type_role_id = self.group_type_role_id

        ignore_group_full: bool | None | Unset
        if isinstance(self.ignore_group_full, Unset):
            ignore_group_full = UNSET
        else:
            ignore_group_full = self.ignore_group_full

        inform_leader: bool | None | Unset
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

        only_add: bool | None | Unset
        if isinstance(self.only_add, Unset):
            only_add = UNSET
        else:
            only_add = self.only_add

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
        if ignore_group_full is not UNSET:
            field_dict["ignoreGroupFull"] = ignore_group_full
        if inform_leader is not UNSET:
            field_dict["informLeader"] = inform_leader
        if member_end_date is not UNSET:
            field_dict["memberEndDate"] = member_end_date
        if member_start_date is not UNSET:
            field_dict["memberStartDate"] = member_start_date
        if only_add is not UNSET:
            field_dict["only_add"] = only_add
        if waitinglist_position is not UNSET:
            field_dict["waitinglistPosition"] = waitinglist_position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_groups_group_id_members_person_id_body_fields_type_0 import (
            PutGroupsGroupIdMembersPersonIdBodyFieldsType0,
        )
        from ..models.put_groups_group_id_members_person_id_body_member_start_date import (
            PutGroupsGroupIdMembersPersonIdBodyMemberStartDate,
        )

        d = dict(src_dict)

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_fields(
            data: object,
        ) -> None | PutGroupsGroupIdMembersPersonIdBodyFieldsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fields_type_0 = (
                    PutGroupsGroupIdMembersPersonIdBodyFieldsType0.from_dict(data)
                )

                return fields_type_0
            except:  # noqa: E722
                pass
            return cast(
                None | PutGroupsGroupIdMembersPersonIdBodyFieldsType0 | Unset, data
            )

        fields = _parse_fields(d.pop("fields", UNSET))

        _group_member_status = d.pop("groupMemberStatus", UNSET)
        group_member_status: (
            PutGroupsGroupIdMembersPersonIdBodyGroupMemberStatus | Unset
        )
        if isinstance(_group_member_status, Unset):
            group_member_status = UNSET
        else:
            group_member_status = PutGroupsGroupIdMembersPersonIdBodyGroupMemberStatus(
                _group_member_status
            )

        def _parse_group_type_role_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_type_role_id = _parse_group_type_role_id(d.pop("groupTypeRoleId", UNSET))

        def _parse_ignore_group_full(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ignore_group_full = _parse_ignore_group_full(d.pop("ignoreGroupFull", UNSET))

        def _parse_inform_leader(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

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
        member_start_date: PutGroupsGroupIdMembersPersonIdBodyMemberStartDate | Unset
        if isinstance(_member_start_date, Unset):
            member_start_date = UNSET
        else:
            member_start_date = (
                PutGroupsGroupIdMembersPersonIdBodyMemberStartDate.from_dict(
                    _member_start_date
                )
            )

        def _parse_only_add(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        only_add = _parse_only_add(d.pop("only_add", UNSET))

        def _parse_waitinglist_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        waitinglist_position = _parse_waitinglist_position(
            d.pop("waitinglistPosition", UNSET)
        )

        put_groups_group_id_members_person_id_body = cls(
            comment=comment,
            fields=fields,
            group_member_status=group_member_status,
            group_type_role_id=group_type_role_id,
            ignore_group_full=ignore_group_full,
            inform_leader=inform_leader,
            member_end_date=member_end_date,
            member_start_date=member_start_date,
            only_add=only_add,
            waitinglist_position=waitinglist_position,
        )

        put_groups_group_id_members_person_id_body.additional_properties = d
        return put_groups_group_id_members_person_id_body

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
