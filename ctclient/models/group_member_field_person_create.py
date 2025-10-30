from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.group_member_field_person_create_db_field import (
        GroupMemberFieldPersonCreateDbField,
    )


T = TypeVar("T", bound="GroupMemberFieldPersonCreate")


@_attrs_define
class GroupMemberFieldPersonCreate:
    """
    Attributes:
        db_field (GroupMemberFieldPersonCreateDbField):
        required_in_registration_form (bool):
        sort_key (int):
    """

    db_field: GroupMemberFieldPersonCreateDbField
    required_in_registration_form: bool
    sort_key: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        db_field = self.db_field.to_dict()

        required_in_registration_form = self.required_in_registration_form

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dbField": db_field,
                "requiredInRegistrationForm": required_in_registration_form,
                "sortKey": sort_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_member_field_person_create_db_field import (
            GroupMemberFieldPersonCreateDbField,
        )

        d = dict(src_dict)
        db_field = GroupMemberFieldPersonCreateDbField.from_dict(d.pop("dbField"))

        required_in_registration_form = d.pop("requiredInRegistrationForm")

        sort_key = d.pop("sortKey")

        group_member_field_person_create = cls(
            db_field=db_field,
            required_in_registration_form=required_in_registration_form,
            sort_key=sort_key,
        )

        group_member_field_person_create.additional_properties = d
        return group_member_field_person_create

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
