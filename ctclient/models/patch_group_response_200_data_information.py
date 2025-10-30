from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_group_response_200_data_information_chat_status import (
    PatchGroupResponse200DataInformationChatStatus,
)
from ..models.patch_group_response_200_data_information_color import (
    PatchGroupResponse200DataInformationColor,
)

if TYPE_CHECKING:
    from ..models.patch_group_response_200_data_information_date_of_foundation import (
        PatchGroupResponse200DataInformationDateOfFoundation,
    )
    from ..models.patch_group_response_200_data_information_end_date import (
        PatchGroupResponse200DataInformationEndDate,
    )


T = TypeVar("T", bound="PatchGroupResponse200DataInformation")


@_attrs_define
class PatchGroupResponse200DataInformation:
    """
    Attributes:
        age_group_ids (list[int]):  Example: [1, 2].
        campus_id (int | None):
        chat_status (PatchGroupResponse200DataInformationChatStatus): status of chat room Example: STARTED.
        color (PatchGroupResponse200DataInformationColor): A color in ChurchTools
        date_of_foundation (PatchGroupResponse200DataInformationDateOfFoundation):
        end_date (PatchGroupResponse200DataInformationEndDate):
        group_category_id (int | None):
        group_homepage_url (None | str):
        group_status_id (int):
        group_type_id (int):
        image_url (None | str):
        max_members (int | None): Allowed maximal members
        meeting_time (None | str):
        note (str):
        sign_up_override_role_id (int | None):
        target_group_id (int | None):
        weekday (int | None): The number of the weekday. Starting with 0 = Sunday, 1 = Monday, ...
    """

    age_group_ids: list[int]
    campus_id: int | None
    chat_status: PatchGroupResponse200DataInformationChatStatus
    color: PatchGroupResponse200DataInformationColor
    date_of_foundation: PatchGroupResponse200DataInformationDateOfFoundation
    end_date: PatchGroupResponse200DataInformationEndDate
    group_category_id: int | None
    group_homepage_url: None | str
    group_status_id: int
    group_type_id: int
    image_url: None | str
    max_members: int | None
    meeting_time: None | str
    note: str
    sign_up_override_role_id: int | None
    target_group_id: int | None
    weekday: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        age_group_ids = self.age_group_ids

        campus_id: int | None
        campus_id = self.campus_id

        chat_status = self.chat_status.value

        color = self.color.value

        date_of_foundation = self.date_of_foundation.to_dict()

        end_date = self.end_date.to_dict()

        group_category_id: int | None
        group_category_id = self.group_category_id

        group_homepage_url: None | str
        group_homepage_url = self.group_homepage_url

        group_status_id = self.group_status_id

        group_type_id = self.group_type_id

        image_url: None | str
        image_url = self.image_url

        max_members: int | None
        max_members = self.max_members

        meeting_time: None | str
        meeting_time = self.meeting_time

        note = self.note

        sign_up_override_role_id: int | None
        sign_up_override_role_id = self.sign_up_override_role_id

        target_group_id: int | None
        target_group_id = self.target_group_id

        weekday: int | None
        weekday = self.weekday

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ageGroupIds": age_group_ids,
                "campusId": campus_id,
                "chatStatus": chat_status,
                "color": color,
                "dateOfFoundation": date_of_foundation,
                "endDate": end_date,
                "groupCategoryId": group_category_id,
                "groupHomepageUrl": group_homepage_url,
                "groupStatusId": group_status_id,
                "groupTypeId": group_type_id,
                "imageUrl": image_url,
                "maxMembers": max_members,
                "meetingTime": meeting_time,
                "note": note,
                "signUpOverrideRoleId": sign_up_override_role_id,
                "targetGroupId": target_group_id,
                "weekday": weekday,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_group_response_200_data_information_date_of_foundation import (
            PatchGroupResponse200DataInformationDateOfFoundation,
        )
        from ..models.patch_group_response_200_data_information_end_date import (
            PatchGroupResponse200DataInformationEndDate,
        )

        d = dict(src_dict)
        age_group_ids = cast(list[int], d.pop("ageGroupIds"))

        def _parse_campus_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        campus_id = _parse_campus_id(d.pop("campusId"))

        chat_status = PatchGroupResponse200DataInformationChatStatus(
            d.pop("chatStatus")
        )

        color = PatchGroupResponse200DataInformationColor(d.pop("color"))

        date_of_foundation = (
            PatchGroupResponse200DataInformationDateOfFoundation.from_dict(
                d.pop("dateOfFoundation")
            )
        )

        end_date = PatchGroupResponse200DataInformationEndDate.from_dict(
            d.pop("endDate")
        )

        def _parse_group_category_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        group_category_id = _parse_group_category_id(d.pop("groupCategoryId"))

        def _parse_group_homepage_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        group_homepage_url = _parse_group_homepage_url(d.pop("groupHomepageUrl"))

        group_status_id = d.pop("groupStatusId")

        group_type_id = d.pop("groupTypeId")

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("imageUrl"))

        def _parse_max_members(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_members = _parse_max_members(d.pop("maxMembers"))

        def _parse_meeting_time(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        meeting_time = _parse_meeting_time(d.pop("meetingTime"))

        note = d.pop("note")

        def _parse_sign_up_override_role_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sign_up_override_role_id = _parse_sign_up_override_role_id(
            d.pop("signUpOverrideRoleId")
        )

        def _parse_target_group_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        target_group_id = _parse_target_group_id(d.pop("targetGroupId"))

        def _parse_weekday(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        weekday = _parse_weekday(d.pop("weekday"))

        patch_group_response_200_data_information = cls(
            age_group_ids=age_group_ids,
            campus_id=campus_id,
            chat_status=chat_status,
            color=color,
            date_of_foundation=date_of_foundation,
            end_date=end_date,
            group_category_id=group_category_id,
            group_homepage_url=group_homepage_url,
            group_status_id=group_status_id,
            group_type_id=group_type_id,
            image_url=image_url,
            max_members=max_members,
            meeting_time=meeting_time,
            note=note,
            sign_up_override_role_id=sign_up_override_role_id,
            target_group_id=target_group_id,
            weekday=weekday,
        )

        patch_group_response_200_data_information.additional_properties = d
        return patch_group_response_200_data_information

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
