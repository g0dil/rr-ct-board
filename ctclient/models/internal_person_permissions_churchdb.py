from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPersonPermissionsChurchdb")


@_attrs_define
class InternalPersonPermissionsChurchdb:
    """
    Attributes:
        do_followup (bool | Unset):
        edit_person_field_of_group_members (float | Unset):
        edit_persons (bool | Unset):
        invite_person (bool | Unset):
        see_persons (float | Unset):
        see_tags (bool | Unset):
    """

    do_followup: bool | Unset = UNSET
    edit_person_field_of_group_members: float | Unset = UNSET
    edit_persons: bool | Unset = UNSET
    invite_person: bool | Unset = UNSET
    see_persons: float | Unset = UNSET
    see_tags: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        do_followup = self.do_followup

        edit_person_field_of_group_members = self.edit_person_field_of_group_members

        edit_persons = self.edit_persons

        invite_person = self.invite_person

        see_persons = self.see_persons

        see_tags = self.see_tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if do_followup is not UNSET:
            field_dict["+do followup"] = do_followup
        if edit_person_field_of_group_members is not UNSET:
            field_dict["+edit person field of group members"] = (
                edit_person_field_of_group_members
            )
        if edit_persons is not UNSET:
            field_dict["+edit persons"] = edit_persons
        if invite_person is not UNSET:
            field_dict["+invite person"] = invite_person
        if see_persons is not UNSET:
            field_dict["+see persons"] = see_persons
        if see_tags is not UNSET:
            field_dict["+see tags"] = see_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        do_followup = d.pop("+do followup", UNSET)

        edit_person_field_of_group_members = d.pop(
            "+edit person field of group members", UNSET
        )

        edit_persons = d.pop("+edit persons", UNSET)

        invite_person = d.pop("+invite person", UNSET)

        see_persons = d.pop("+see persons", UNSET)

        see_tags = d.pop("+see tags", UNSET)

        internal_person_permissions_churchdb = cls(
            do_followup=do_followup,
            edit_person_field_of_group_members=edit_person_field_of_group_members,
            edit_persons=edit_persons,
            invite_person=invite_person,
            see_persons=see_persons,
            see_tags=see_tags,
        )

        internal_person_permissions_churchdb.additional_properties = d
        return internal_person_permissions_churchdb

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
