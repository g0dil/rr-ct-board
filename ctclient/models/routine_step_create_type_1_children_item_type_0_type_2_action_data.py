from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoutineStepCreateType1ChildrenItemType0Type2ActionData")


@_attrs_define
class RoutineStepCreateType1ChildrenItemType0Type2ActionData:
    """
    Attributes:
        group_id (int):
        comment (str | Unset):
        inform_leader (bool | Unset):
        member_end_date (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        member_start_date (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        role_id (int | Unset):
        waitinglist_position (int | Unset):
    """

    group_id: int
    comment: str | Unset = UNSET
    inform_leader: bool | Unset = UNSET
    member_end_date: datetime.date | None | Unset = UNSET
    member_start_date: datetime.date | None | Unset = UNSET
    role_id: int | Unset = UNSET
    waitinglist_position: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        comment = self.comment

        inform_leader = self.inform_leader

        member_end_date: None | str | Unset
        if isinstance(self.member_end_date, Unset):
            member_end_date = UNSET
        elif isinstance(self.member_end_date, datetime.date):
            member_end_date = self.member_end_date.isoformat()
        else:
            member_end_date = self.member_end_date

        member_start_date: None | str | Unset
        if isinstance(self.member_start_date, Unset):
            member_start_date = UNSET
        elif isinstance(self.member_start_date, datetime.date):
            member_start_date = self.member_start_date.isoformat()
        else:
            member_start_date = self.member_start_date

        role_id = self.role_id

        waitinglist_position = self.waitinglist_position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groupId": group_id,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if inform_leader is not UNSET:
            field_dict["informLeader"] = inform_leader
        if member_end_date is not UNSET:
            field_dict["memberEndDate"] = member_end_date
        if member_start_date is not UNSET:
            field_dict["memberStartDate"] = member_start_date
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if waitinglist_position is not UNSET:
            field_dict["waitinglistPosition"] = waitinglist_position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = d.pop("groupId")

        comment = d.pop("comment", UNSET)

        inform_leader = d.pop("informLeader", UNSET)

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

        def _parse_member_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                member_start_date_type_0 = isoparse(data).date()

                return member_start_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        member_start_date = _parse_member_start_date(d.pop("memberStartDate", UNSET))

        role_id = d.pop("roleId", UNSET)

        waitinglist_position = d.pop("waitinglistPosition", UNSET)

        routine_step_create_type_1_children_item_type_0_type_2_action_data = cls(
            group_id=group_id,
            comment=comment,
            inform_leader=inform_leader,
            member_end_date=member_end_date,
            member_start_date=member_start_date,
            role_id=role_id,
            waitinglist_position=waitinglist_position,
        )

        routine_step_create_type_1_children_item_type_0_type_2_action_data.additional_properties = d
        return routine_step_create_type_1_children_item_type_0_type_2_action_data

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
