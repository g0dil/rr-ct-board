from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGroupsGroupIdResponse200DataSettingsNewMember")


@_attrs_define
class GetGroupsGroupIdResponse200DataSettingsNewMember:
    """Campus, status, and department for newly created persons.

    Attributes:
        campus_id (int | None):
        department_id (int | None):
        status_id (int | None):
    """

    campus_id: int | None
    department_id: int | None
    status_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campus_id: int | None
        campus_id = self.campus_id

        department_id: int | None
        department_id = self.department_id

        status_id: int | None
        status_id = self.status_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campusId": campus_id,
                "departmentId": department_id,
                "statusId": status_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_campus_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        campus_id = _parse_campus_id(d.pop("campusId"))

        def _parse_department_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        department_id = _parse_department_id(d.pop("departmentId"))

        def _parse_status_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        status_id = _parse_status_id(d.pop("statusId"))

        get_groups_group_id_response_200_data_settings_new_member = cls(
            campus_id=campus_id,
            department_id=department_id,
            status_id=status_id,
        )

        get_groups_group_id_response_200_data_settings_new_member.additional_properties = d
        return get_groups_group_id_response_200_data_settings_new_member

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
