from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_groups_group_id_members_history_response_200_data_item_previous_membership_status import (
    GetGroupsGroupIdMembersHistoryResponse200DataItemPreviousMembershipStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_groups_group_id_members_history_response_200_data_item_previous_fields import (
        GetGroupsGroupIdMembersHistoryResponse200DataItemPreviousFields,
    )


T = TypeVar("T", bound="GetGroupsGroupIdMembersHistoryResponse200DataItemPrevious")


@_attrs_define
class GetGroupsGroupIdMembersHistoryResponse200DataItemPrevious:
    """
    Attributes:
        member_role_id (int):
        comment (str | Unset):
        end_date (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
        fields (GetGroupsGroupIdMembersHistoryResponse200DataItemPreviousFields | Unset):
        membership_status (GetGroupsGroupIdMembersHistoryResponse200DataItemPreviousMembershipStatus | Unset):
        start_date (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
    """

    member_role_id: int
    comment: str | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    fields: GetGroupsGroupIdMembersHistoryResponse200DataItemPreviousFields | Unset = (
        UNSET
    )
    membership_status: (
        GetGroupsGroupIdMembersHistoryResponse200DataItemPreviousMembershipStatus
        | Unset
    ) = UNSET
    start_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_role_id = self.member_role_id

        comment = self.comment

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        membership_status: str | Unset = UNSET
        if not isinstance(self.membership_status, Unset):
            membership_status = self.membership_status.value

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "memberRoleId": member_role_id,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if fields is not UNSET:
            field_dict["fields"] = fields
        if membership_status is not UNSET:
            field_dict["membershipStatus"] = membership_status
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_groups_group_id_members_history_response_200_data_item_previous_fields import (
            GetGroupsGroupIdMembersHistoryResponse200DataItemPreviousFields,
        )

        d = dict(src_dict)
        member_role_id = d.pop("memberRoleId")

        comment = d.pop("comment", UNSET)

        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        _fields = d.pop("fields", UNSET)
        fields: GetGroupsGroupIdMembersHistoryResponse200DataItemPreviousFields | Unset
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = GetGroupsGroupIdMembersHistoryResponse200DataItemPreviousFields.from_dict(
                _fields
            )

        _membership_status = d.pop("membershipStatus", UNSET)
        membership_status: (
            GetGroupsGroupIdMembersHistoryResponse200DataItemPreviousMembershipStatus
            | Unset
        )
        if isinstance(_membership_status, Unset):
            membership_status = UNSET
        else:
            membership_status = GetGroupsGroupIdMembersHistoryResponse200DataItemPreviousMembershipStatus(
                _membership_status
            )

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        get_groups_group_id_members_history_response_200_data_item_previous = cls(
            member_role_id=member_role_id,
            comment=comment,
            end_date=end_date,
            fields=fields,
            membership_status=membership_status,
            start_date=start_date,
        )

        get_groups_group_id_members_history_response_200_data_item_previous.additional_properties = d
        return get_groups_group_id_members_history_response_200_data_item_previous

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
