from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_groups_group_id_memberfields_response_200_data_item_type_0_field_db_field import (
        GetGroupsGroupIdMemberfieldsResponse200DataItemType0FieldDbField,
    )


T = TypeVar("T", bound="GetGroupsGroupIdMemberfieldsResponse200DataItemType0Field")


@_attrs_define
class GetGroupsGroupIdMemberfieldsResponse200DataItemType0Field:
    """
    Attributes:
        db_field (GetGroupsGroupIdMemberfieldsResponse200DataItemType0FieldDbField):
        required_in_registration_form (bool):
        sort_key (int):
        group_id (int):
        id (int):
    """

    db_field: GetGroupsGroupIdMemberfieldsResponse200DataItemType0FieldDbField
    required_in_registration_form: bool
    sort_key: int
    group_id: int
    id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        db_field = self.db_field.to_dict()

        required_in_registration_form = self.required_in_registration_form

        sort_key = self.sort_key

        group_id = self.group_id

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dbField": db_field,
                "requiredInRegistrationForm": required_in_registration_form,
                "sortKey": sort_key,
                "groupId": group_id,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_groups_group_id_memberfields_response_200_data_item_type_0_field_db_field import (
            GetGroupsGroupIdMemberfieldsResponse200DataItemType0FieldDbField,
        )

        d = dict(src_dict)
        db_field = (
            GetGroupsGroupIdMemberfieldsResponse200DataItemType0FieldDbField.from_dict(
                d.pop("dbField")
            )
        )

        required_in_registration_form = d.pop("requiredInRegistrationForm")

        sort_key = d.pop("sortKey")

        group_id = d.pop("groupId")

        id = d.pop("id")

        get_groups_group_id_memberfields_response_200_data_item_type_0_field = cls(
            db_field=db_field,
            required_in_registration_form=required_in_registration_form,
            sort_key=sort_key,
            group_id=group_id,
            id=id,
        )

        get_groups_group_id_memberfields_response_200_data_item_type_0_field.additional_properties = d
        return get_groups_group_id_memberfields_response_200_data_item_type_0_field

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
