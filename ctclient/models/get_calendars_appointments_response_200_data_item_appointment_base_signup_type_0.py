from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T", bound="GetCalendarsAppointmentsResponse200DataItemAppointmentBaseSignupType0"
)


@_attrs_define
class GetCalendarsAppointmentsResponse200DataItemAppointmentBaseSignupType0:
    """
    Attributes:
        signup_days_archive_group_no (int | None):
        signup_group_type_id (int | None):
        signup_set_completion_date (bool):
        signup_template_group_id (int | None):
        singup_days_forward_no (int | None):
    """

    signup_days_archive_group_no: int | None
    signup_group_type_id: int | None
    signup_set_completion_date: bool
    signup_template_group_id: int | None
    singup_days_forward_no: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signup_days_archive_group_no: int | None
        signup_days_archive_group_no = self.signup_days_archive_group_no

        signup_group_type_id: int | None
        signup_group_type_id = self.signup_group_type_id

        signup_set_completion_date = self.signup_set_completion_date

        signup_template_group_id: int | None
        signup_template_group_id = self.signup_template_group_id

        singup_days_forward_no: int | None
        singup_days_forward_no = self.singup_days_forward_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signupDaysArchiveGroupNo": signup_days_archive_group_no,
                "signupGroupTypeId": signup_group_type_id,
                "signupSetCompletionDate": signup_set_completion_date,
                "signupTemplateGroupId": signup_template_group_id,
                "singupDaysForwardNo": singup_days_forward_no,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_signup_days_archive_group_no(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        signup_days_archive_group_no = _parse_signup_days_archive_group_no(
            d.pop("signupDaysArchiveGroupNo")
        )

        def _parse_signup_group_type_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        signup_group_type_id = _parse_signup_group_type_id(d.pop("signupGroupTypeId"))

        signup_set_completion_date = d.pop("signupSetCompletionDate")

        def _parse_signup_template_group_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        signup_template_group_id = _parse_signup_template_group_id(
            d.pop("signupTemplateGroupId")
        )

        def _parse_singup_days_forward_no(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        singup_days_forward_no = _parse_singup_days_forward_no(
            d.pop("singupDaysForwardNo")
        )

        get_calendars_appointments_response_200_data_item_appointment_base_signup_type_0 = cls(
            signup_days_archive_group_no=signup_days_archive_group_no,
            signup_group_type_id=signup_group_type_id,
            signup_set_completion_date=signup_set_completion_date,
            signup_template_group_id=signup_template_group_id,
            singup_days_forward_no=singup_days_forward_no,
        )

        get_calendars_appointments_response_200_data_item_appointment_base_signup_type_0.additional_properties = d
        return get_calendars_appointments_response_200_data_item_appointment_base_signup_type_0

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
