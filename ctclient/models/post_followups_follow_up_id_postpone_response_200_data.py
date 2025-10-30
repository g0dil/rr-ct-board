from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.post_followups_follow_up_id_postpone_response_200_data_color import (
    PostFollowupsFollowUpIdPostponeResponse200DataColor,
)
from ..models.post_followups_follow_up_id_postpone_response_200_data_origin import (
    PostFollowupsFollowUpIdPostponeResponse200DataOrigin,
)
from ..models.post_followups_follow_up_id_postpone_response_200_data_success_group_member_status_type_0 import (
    PostFollowupsFollowUpIdPostponeResponse200DataSuccessGroupMemberStatusType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_followups_follow_up_id_postpone_response_200_data_meta import (
        PostFollowupsFollowUpIdPostponeResponse200DataMeta,
    )


T = TypeVar("T", bound="PostFollowupsFollowUpIdPostponeResponse200Data")


@_attrs_define
class PostFollowupsFollowUpIdPostponeResponse200Data:
    """
    Attributes:
        title (str):  Example: Call Peter.
        done_date (datetime.date | None): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
        effective_due_date (datetime.date | None): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
        group_id (int | None):
        id (int):  Example: 5.
        membership_id (int | None):
        meta (PostFollowupsFollowUpIdPostponeResponse200DataMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z',
            'createdPerson': {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        origin (PostFollowupsFollowUpIdPostponeResponse200DataOrigin):
        person_id (int):
        color (PostFollowupsFollowUpIdPostponeResponse200DataColor | Unset): A color in ChurchTools
        description (None | str | Unset):  Example: Ask Peter to participate in next Sunday's service.
        due_date (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
        icon (str | Unset):  Example: phone.
        owner_id (int | None | Unset):
        success_group_id (int | None | Unset):
        success_group_member_status (None | PostFollowupsFollowUpIdPostponeResponse200DataSuccessGroupMemberStatusType0
            | Unset):
        success_group_of_group_type_id (int | None | Unset):
        success_role_id (int | None | Unset):
    """

    title: str
    done_date: datetime.date | None
    effective_due_date: datetime.date | None
    group_id: int | None
    id: int
    membership_id: int | None
    meta: PostFollowupsFollowUpIdPostponeResponse200DataMeta
    origin: PostFollowupsFollowUpIdPostponeResponse200DataOrigin
    person_id: int
    color: PostFollowupsFollowUpIdPostponeResponse200DataColor | Unset = UNSET
    description: None | str | Unset = UNSET
    due_date: datetime.date | None | Unset = UNSET
    icon: str | Unset = UNSET
    owner_id: int | None | Unset = UNSET
    success_group_id: int | None | Unset = UNSET
    success_group_member_status: (
        None
        | PostFollowupsFollowUpIdPostponeResponse200DataSuccessGroupMemberStatusType0
        | Unset
    ) = UNSET
    success_group_of_group_type_id: int | None | Unset = UNSET
    success_role_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        done_date: None | str
        if isinstance(self.done_date, datetime.date):
            done_date = self.done_date.isoformat()
        else:
            done_date = self.done_date

        effective_due_date: None | str
        if isinstance(self.effective_due_date, datetime.date):
            effective_due_date = self.effective_due_date.isoformat()
        else:
            effective_due_date = self.effective_due_date

        group_id: int | None
        group_id = self.group_id

        id = self.id

        membership_id: int | None
        membership_id = self.membership_id

        meta = self.meta.to_dict()

        origin = self.origin.value

        person_id = self.person_id

        color: str | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        icon = self.icon

        owner_id: int | None | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        success_group_id: int | None | Unset
        if isinstance(self.success_group_id, Unset):
            success_group_id = UNSET
        else:
            success_group_id = self.success_group_id

        success_group_member_status: None | str | Unset
        if isinstance(self.success_group_member_status, Unset):
            success_group_member_status = UNSET
        elif isinstance(
            self.success_group_member_status,
            PostFollowupsFollowUpIdPostponeResponse200DataSuccessGroupMemberStatusType0,
        ):
            success_group_member_status = self.success_group_member_status.value
        else:
            success_group_member_status = self.success_group_member_status

        success_group_of_group_type_id: int | None | Unset
        if isinstance(self.success_group_of_group_type_id, Unset):
            success_group_of_group_type_id = UNSET
        else:
            success_group_of_group_type_id = self.success_group_of_group_type_id

        success_role_id: int | None | Unset
        if isinstance(self.success_role_id, Unset):
            success_role_id = UNSET
        else:
            success_role_id = self.success_role_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "doneDate": done_date,
                "effectiveDueDate": effective_due_date,
                "groupId": group_id,
                "id": id,
                "membershipId": membership_id,
                "meta": meta,
                "origin": origin,
                "personId": person_id,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if icon is not UNSET:
            field_dict["icon"] = icon
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if success_group_id is not UNSET:
            field_dict["successGroupId"] = success_group_id
        if success_group_member_status is not UNSET:
            field_dict["successGroupMemberStatus"] = success_group_member_status
        if success_group_of_group_type_id is not UNSET:
            field_dict["successGroupOfGroupTypeId"] = success_group_of_group_type_id
        if success_role_id is not UNSET:
            field_dict["successRoleId"] = success_role_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_followups_follow_up_id_postpone_response_200_data_meta import (
            PostFollowupsFollowUpIdPostponeResponse200DataMeta,
        )

        d = dict(src_dict)
        title = d.pop("title")

        def _parse_done_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                done_date_type_0 = isoparse(data).date()

                return done_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None, data)

        done_date = _parse_done_date(d.pop("doneDate"))

        def _parse_effective_due_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_due_date_type_0 = isoparse(data).date()

                return effective_due_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None, data)

        effective_due_date = _parse_effective_due_date(d.pop("effectiveDueDate"))

        def _parse_group_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        group_id = _parse_group_id(d.pop("groupId"))

        id = d.pop("id")

        def _parse_membership_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        membership_id = _parse_membership_id(d.pop("membershipId"))

        meta = PostFollowupsFollowUpIdPostponeResponse200DataMeta.from_dict(
            d.pop("meta")
        )

        origin = PostFollowupsFollowUpIdPostponeResponse200DataOrigin(d.pop("origin"))

        person_id = d.pop("personId")

        _color = d.pop("color", UNSET)
        color: PostFollowupsFollowUpIdPostponeResponse200DataColor | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = PostFollowupsFollowUpIdPostponeResponse200DataColor(_color)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_due_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = isoparse(data).date()

                return due_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        due_date = _parse_due_date(d.pop("dueDate", UNSET))

        icon = d.pop("icon", UNSET)

        def _parse_owner_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner_id = _parse_owner_id(d.pop("ownerId", UNSET))

        def _parse_success_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        success_group_id = _parse_success_group_id(d.pop("successGroupId", UNSET))

        def _parse_success_group_member_status(
            data: object,
        ) -> (
            None
            | PostFollowupsFollowUpIdPostponeResponse200DataSuccessGroupMemberStatusType0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                success_group_member_status_type_0 = PostFollowupsFollowUpIdPostponeResponse200DataSuccessGroupMemberStatusType0(
                    data
                )

                return success_group_member_status_type_0
            except:  # noqa: E722
                pass
            return cast(
                None
                | PostFollowupsFollowUpIdPostponeResponse200DataSuccessGroupMemberStatusType0
                | Unset,
                data,
            )

        success_group_member_status = _parse_success_group_member_status(
            d.pop("successGroupMemberStatus", UNSET)
        )

        def _parse_success_group_of_group_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        success_group_of_group_type_id = _parse_success_group_of_group_type_id(
            d.pop("successGroupOfGroupTypeId", UNSET)
        )

        def _parse_success_role_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        success_role_id = _parse_success_role_id(d.pop("successRoleId", UNSET))

        post_followups_follow_up_id_postpone_response_200_data = cls(
            title=title,
            done_date=done_date,
            effective_due_date=effective_due_date,
            group_id=group_id,
            id=id,
            membership_id=membership_id,
            meta=meta,
            origin=origin,
            person_id=person_id,
            color=color,
            description=description,
            due_date=due_date,
            icon=icon,
            owner_id=owner_id,
            success_group_id=success_group_id,
            success_group_member_status=success_group_member_status,
            success_group_of_group_type_id=success_group_of_group_type_id,
            success_role_id=success_role_id,
        )

        post_followups_follow_up_id_postpone_response_200_data.additional_properties = d
        return post_followups_follow_up_id_postpone_response_200_data

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
