from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.post_persons_person_id_followups_body_color import (
    PostPersonsPersonIdFollowupsBodyColor,
)
from ..models.post_persons_person_id_followups_body_success_group_member_status_type_0 import (
    PostPersonsPersonIdFollowupsBodySuccessGroupMemberStatusType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostPersonsPersonIdFollowupsBody")


@_attrs_define
class PostPersonsPersonIdFollowupsBody:
    """
    Attributes:
        title (str):  Example: Call Peter.
        color (PostPersonsPersonIdFollowupsBodyColor | Unset): A color in ChurchTools
        description (None | str | Unset):  Example: Ask Peter to participate in next Sunday's service.
        due_date (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
        icon (str | Unset):  Example: phone.
        owner_id (int | None | Unset):
        success_group_id (int | None | Unset):
        success_group_member_status (None | PostPersonsPersonIdFollowupsBodySuccessGroupMemberStatusType0 | Unset):
        success_group_of_group_type_id (int | None | Unset):
        success_role_id (int | None | Unset):
    """

    title: str
    color: PostPersonsPersonIdFollowupsBodyColor | Unset = UNSET
    description: None | str | Unset = UNSET
    due_date: datetime.date | None | Unset = UNSET
    icon: str | Unset = UNSET
    owner_id: int | None | Unset = UNSET
    success_group_id: int | None | Unset = UNSET
    success_group_member_status: (
        None | PostPersonsPersonIdFollowupsBodySuccessGroupMemberStatusType0 | Unset
    ) = UNSET
    success_group_of_group_type_id: int | None | Unset = UNSET
    success_role_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

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
            PostPersonsPersonIdFollowupsBodySuccessGroupMemberStatusType0,
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
        d = dict(src_dict)
        title = d.pop("title")

        _color = d.pop("color", UNSET)
        color: PostPersonsPersonIdFollowupsBodyColor | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = PostPersonsPersonIdFollowupsBodyColor(_color)

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
            None | PostPersonsPersonIdFollowupsBodySuccessGroupMemberStatusType0 | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                success_group_member_status_type_0 = (
                    PostPersonsPersonIdFollowupsBodySuccessGroupMemberStatusType0(data)
                )

                return success_group_member_status_type_0
            except:  # noqa: E722
                pass
            return cast(
                None
                | PostPersonsPersonIdFollowupsBodySuccessGroupMemberStatusType0
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

        post_persons_person_id_followups_body = cls(
            title=title,
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

        post_persons_person_id_followups_body.additional_properties = d
        return post_persons_person_id_followups_body

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
