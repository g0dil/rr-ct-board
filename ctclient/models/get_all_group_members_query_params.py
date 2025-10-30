from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_all_group_members_query_params_group_member_statuses_item import (
    GetAllGroupMembersQueryParamsGroupMemberStatusesItem,
)
from ..models.get_all_group_members_query_params_include_item import (
    GetAllGroupMembersQueryParamsIncludeItem,
)
from ..models.get_all_group_members_query_params_order_directions_item import (
    GetAllGroupMembersQueryParamsOrderDirectionsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAllGroupMembersQueryParams")


@_attrs_define
class GetAllGroupMembersQueryParams:
    """
    Attributes:
        allowed_chat_users_only (bool | Unset):
        allowed_chat_writers_only (bool | Unset):
        comment (str | Unset):
        group_member_statuses (list[GetAllGroupMembersQueryParamsGroupMemberStatusesItem] | Unset):
        include (list[GetAllGroupMembersQueryParamsIncludeItem] | Unset):
        limit (int | Unset):  Default: 10. Example: 10.
        member_start_date_after (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        member_start_date_before (datetime.date | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
            2022-10-19.
        order_directions (list[GetAllGroupMembersQueryParamsOrderDirectionsItem] | Unset):
        order_fields (list[str] | Unset):
        page (int | Unset):  Default: 1. Example: 1.
        person_fields (list[str] | Unset):
        person_id (list[int] | Unset):
        query (str | Unset):  Example: Peter Maier.
        role_ids (list[int] | Unset):
    """

    allowed_chat_users_only: bool | Unset = UNSET
    allowed_chat_writers_only: bool | Unset = UNSET
    comment: str | Unset = UNSET
    group_member_statuses: (
        list[GetAllGroupMembersQueryParamsGroupMemberStatusesItem] | Unset
    ) = UNSET
    include: list[GetAllGroupMembersQueryParamsIncludeItem] | Unset = UNSET
    limit: int | Unset = 10
    member_start_date_after: datetime.date | Unset = UNSET
    member_start_date_before: datetime.date | Unset = UNSET
    order_directions: list[GetAllGroupMembersQueryParamsOrderDirectionsItem] | Unset = (
        UNSET
    )
    order_fields: list[str] | Unset = UNSET
    page: int | Unset = 1
    person_fields: list[str] | Unset = UNSET
    person_id: list[int] | Unset = UNSET
    query: str | Unset = UNSET
    role_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_chat_users_only = self.allowed_chat_users_only

        allowed_chat_writers_only = self.allowed_chat_writers_only

        comment = self.comment

        group_member_statuses: list[str] | Unset = UNSET
        if not isinstance(self.group_member_statuses, Unset):
            group_member_statuses = []
            for group_member_statuses_item_data in self.group_member_statuses:
                group_member_statuses_item = group_member_statuses_item_data.value
                group_member_statuses.append(group_member_statuses_item)

        include: list[str] | Unset = UNSET
        if not isinstance(self.include, Unset):
            include = []
            for include_item_data in self.include:
                include_item = include_item_data.value
                include.append(include_item)

        limit = self.limit

        member_start_date_after: str | Unset = UNSET
        if not isinstance(self.member_start_date_after, Unset):
            member_start_date_after = self.member_start_date_after.isoformat()

        member_start_date_before: str | Unset = UNSET
        if not isinstance(self.member_start_date_before, Unset):
            member_start_date_before = self.member_start_date_before.isoformat()

        order_directions: list[str] | Unset = UNSET
        if not isinstance(self.order_directions, Unset):
            order_directions = []
            for order_directions_item_data in self.order_directions:
                order_directions_item = order_directions_item_data.value
                order_directions.append(order_directions_item)

        order_fields: list[str] | Unset = UNSET
        if not isinstance(self.order_fields, Unset):
            order_fields = self.order_fields

        page = self.page

        person_fields: list[str] | Unset = UNSET
        if not isinstance(self.person_fields, Unset):
            person_fields = self.person_fields

        person_id: list[int] | Unset = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = self.person_id

        query = self.query

        role_ids: list[int] | Unset = UNSET
        if not isinstance(self.role_ids, Unset):
            role_ids = self.role_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_chat_users_only is not UNSET:
            field_dict["allowed_chat_users_only"] = allowed_chat_users_only
        if allowed_chat_writers_only is not UNSET:
            field_dict["allowed_chat_writers_only"] = allowed_chat_writers_only
        if comment is not UNSET:
            field_dict["comment"] = comment
        if group_member_statuses is not UNSET:
            field_dict["group_member_statuses"] = group_member_statuses
        if include is not UNSET:
            field_dict["include"] = include
        if limit is not UNSET:
            field_dict["limit"] = limit
        if member_start_date_after is not UNSET:
            field_dict["member_start_date_after"] = member_start_date_after
        if member_start_date_before is not UNSET:
            field_dict["member_start_date_before"] = member_start_date_before
        if order_directions is not UNSET:
            field_dict["orderDirections"] = order_directions
        if order_fields is not UNSET:
            field_dict["orderFields"] = order_fields
        if page is not UNSET:
            field_dict["page"] = page
        if person_fields is not UNSET:
            field_dict["personFields"] = person_fields
        if person_id is not UNSET:
            field_dict["person_id"] = person_id
        if query is not UNSET:
            field_dict["query"] = query
        if role_ids is not UNSET:
            field_dict["role_ids"] = role_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_chat_users_only = d.pop("allowed_chat_users_only", UNSET)

        allowed_chat_writers_only = d.pop("allowed_chat_writers_only", UNSET)

        comment = d.pop("comment", UNSET)

        group_member_statuses = []
        _group_member_statuses = d.pop("group_member_statuses", UNSET)
        for group_member_statuses_item_data in _group_member_statuses or []:
            group_member_statuses_item = (
                GetAllGroupMembersQueryParamsGroupMemberStatusesItem(
                    group_member_statuses_item_data
                )
            )

            group_member_statuses.append(group_member_statuses_item)

        include = []
        _include = d.pop("include", UNSET)
        for include_item_data in _include or []:
            include_item = GetAllGroupMembersQueryParamsIncludeItem(include_item_data)

            include.append(include_item)

        limit = d.pop("limit", UNSET)

        _member_start_date_after = d.pop("member_start_date_after", UNSET)
        member_start_date_after: datetime.date | Unset
        if isinstance(_member_start_date_after, Unset):
            member_start_date_after = UNSET
        else:
            member_start_date_after = isoparse(_member_start_date_after).date()

        _member_start_date_before = d.pop("member_start_date_before", UNSET)
        member_start_date_before: datetime.date | Unset
        if isinstance(_member_start_date_before, Unset):
            member_start_date_before = UNSET
        else:
            member_start_date_before = isoparse(_member_start_date_before).date()

        order_directions = []
        _order_directions = d.pop("orderDirections", UNSET)
        for order_directions_item_data in _order_directions or []:
            order_directions_item = GetAllGroupMembersQueryParamsOrderDirectionsItem(
                order_directions_item_data
            )

            order_directions.append(order_directions_item)

        order_fields = cast(list[str], d.pop("orderFields", UNSET))

        page = d.pop("page", UNSET)

        person_fields = cast(list[str], d.pop("personFields", UNSET))

        person_id = cast(list[int], d.pop("person_id", UNSET))

        query = d.pop("query", UNSET)

        role_ids = cast(list[int], d.pop("role_ids", UNSET))

        get_all_group_members_query_params = cls(
            allowed_chat_users_only=allowed_chat_users_only,
            allowed_chat_writers_only=allowed_chat_writers_only,
            comment=comment,
            group_member_statuses=group_member_statuses,
            include=include,
            limit=limit,
            member_start_date_after=member_start_date_after,
            member_start_date_before=member_start_date_before,
            order_directions=order_directions,
            order_fields=order_fields,
            page=page,
            person_fields=person_fields,
            person_id=person_id,
            query=query,
            role_ids=role_ids,
        )

        get_all_group_members_query_params.additional_properties = d
        return get_all_group_members_query_params

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
