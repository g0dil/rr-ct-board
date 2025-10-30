from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_member_field_group_field_type_code import (
    GroupMemberFieldGroupFieldTypeCode,
)

if TYPE_CHECKING:
    from ..models.group_member_field_group_options_item import (
        GroupMemberFieldGroupOptionsItem,
    )


T = TypeVar("T", bound="GroupMemberFieldGroup")


@_attrs_define
class GroupMemberFieldGroup:
    """
    Attributes:
        default_value (str):
        field_name (str):
        field_type_code (GroupMemberFieldGroupFieldTypeCode): The intern code of the field type the field belongs to.
            This is used to define the type of the field.
        field_type_id (int):
        max_length (int):
        name (str):
        name_in_signup_form (None | str):
        note (None | str):
        note_in_signup_form (None | str):
        options (list[GroupMemberFieldGroupOptionsItem]):
        reference_name (str):
        required_in_registration_form (bool):
        security_level (int):
        sort_key (int):
        use_in_registration_form (bool):
        group_id (int):
        id (int):
    """

    default_value: str
    field_name: str
    field_type_code: GroupMemberFieldGroupFieldTypeCode
    field_type_id: int
    max_length: int
    name: str
    name_in_signup_form: None | str
    note: None | str
    note_in_signup_form: None | str
    options: list[GroupMemberFieldGroupOptionsItem]
    reference_name: str
    required_in_registration_form: bool
    security_level: int
    sort_key: int
    use_in_registration_form: bool
    group_id: int
    id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_value = self.default_value

        field_name = self.field_name

        field_type_code = self.field_type_code.value

        field_type_id = self.field_type_id

        max_length = self.max_length

        name = self.name

        name_in_signup_form: None | str
        name_in_signup_form = self.name_in_signup_form

        note: None | str
        note = self.note

        note_in_signup_form: None | str
        note_in_signup_form = self.note_in_signup_form

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        reference_name = self.reference_name

        required_in_registration_form = self.required_in_registration_form

        security_level = self.security_level

        sort_key = self.sort_key

        use_in_registration_form = self.use_in_registration_form

        group_id = self.group_id

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "defaultValue": default_value,
                "fieldName": field_name,
                "fieldTypeCode": field_type_code,
                "fieldTypeId": field_type_id,
                "maxLength": max_length,
                "name": name,
                "nameInSignupForm": name_in_signup_form,
                "note": note,
                "noteInSignupForm": note_in_signup_form,
                "options": options,
                "referenceName": reference_name,
                "requiredInRegistrationForm": required_in_registration_form,
                "securityLevel": security_level,
                "sortKey": sort_key,
                "useInRegistrationForm": use_in_registration_form,
                "groupId": group_id,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_member_field_group_options_item import (
            GroupMemberFieldGroupOptionsItem,
        )

        d = dict(src_dict)
        default_value = d.pop("defaultValue")

        field_name = d.pop("fieldName")

        field_type_code = GroupMemberFieldGroupFieldTypeCode(d.pop("fieldTypeCode"))

        field_type_id = d.pop("fieldTypeId")

        max_length = d.pop("maxLength")

        name = d.pop("name")

        def _parse_name_in_signup_form(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name_in_signup_form = _parse_name_in_signup_form(d.pop("nameInSignupForm"))

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        def _parse_note_in_signup_form(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note_in_signup_form = _parse_note_in_signup_form(d.pop("noteInSignupForm"))

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = GroupMemberFieldGroupOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        reference_name = d.pop("referenceName")

        required_in_registration_form = d.pop("requiredInRegistrationForm")

        security_level = d.pop("securityLevel")

        sort_key = d.pop("sortKey")

        use_in_registration_form = d.pop("useInRegistrationForm")

        group_id = d.pop("groupId")

        id = d.pop("id")

        group_member_field_group = cls(
            default_value=default_value,
            field_name=field_name,
            field_type_code=field_type_code,
            field_type_id=field_type_id,
            max_length=max_length,
            name=name,
            name_in_signup_form=name_in_signup_form,
            note=note,
            note_in_signup_form=note_in_signup_form,
            options=options,
            reference_name=reference_name,
            required_in_registration_form=required_in_registration_form,
            security_level=security_level,
            sort_key=sort_key,
            use_in_registration_form=use_in_registration_form,
            group_id=group_id,
            id=id,
        )

        group_member_field_group.additional_properties = d
        return group_member_field_group

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
