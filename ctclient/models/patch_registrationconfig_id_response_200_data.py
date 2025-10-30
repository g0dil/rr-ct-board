from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_registrationconfig_id_response_200_data_campuses_item import (
        PatchRegistrationconfigIdResponse200DataCampusesItem,
    )
    from ..models.patch_registrationconfig_id_response_200_data_fields_item import (
        PatchRegistrationconfigIdResponse200DataFieldsItem,
    )


T = TypeVar("T", bound="PatchRegistrationconfigIdResponse200Data")


@_attrs_define
class PatchRegistrationconfigIdResponse200Data:
    """
    Attributes:
        blacklist (list[str]):
        campuses (list[PatchRegistrationconfigIdResponse200DataCampusesItem]):
        department_ids (list[int]):
        fields (list[PatchRegistrationconfigIdResponse200DataFieldsItem]):
        id (int):
        is_active (bool):
        minimum_age (int):
        show_button (bool):
        status_id (int):
        tags_for_existing_persons (list[str]):
        tags_for_new_persons (list[str]):
    """

    blacklist: list[str]
    campuses: list[PatchRegistrationconfigIdResponse200DataCampusesItem]
    department_ids: list[int]
    fields: list[PatchRegistrationconfigIdResponse200DataFieldsItem]
    id: int
    is_active: bool
    minimum_age: int
    show_button: bool
    status_id: int
    tags_for_existing_persons: list[str]
    tags_for_new_persons: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blacklist = self.blacklist

        campuses = []
        for campuses_item_data in self.campuses:
            campuses_item = campuses_item_data.to_dict()
            campuses.append(campuses_item)

        department_ids = self.department_ids

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        id = self.id

        is_active = self.is_active

        minimum_age = self.minimum_age

        show_button = self.show_button

        status_id = self.status_id

        tags_for_existing_persons = self.tags_for_existing_persons

        tags_for_new_persons = self.tags_for_new_persons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blacklist": blacklist,
                "campuses": campuses,
                "departmentIds": department_ids,
                "fields": fields,
                "id": id,
                "isActive": is_active,
                "minimumAge": minimum_age,
                "showButton": show_button,
                "statusId": status_id,
                "tagsForExistingPersons": tags_for_existing_persons,
                "tagsForNewPersons": tags_for_new_persons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_registrationconfig_id_response_200_data_campuses_item import (
            PatchRegistrationconfigIdResponse200DataCampusesItem,
        )
        from ..models.patch_registrationconfig_id_response_200_data_fields_item import (
            PatchRegistrationconfigIdResponse200DataFieldsItem,
        )

        d = dict(src_dict)
        blacklist = cast(list[str], d.pop("blacklist"))

        campuses = []
        _campuses = d.pop("campuses")
        for campuses_item_data in _campuses:
            campuses_item = (
                PatchRegistrationconfigIdResponse200DataCampusesItem.from_dict(
                    campuses_item_data
                )
            )

            campuses.append(campuses_item)

        department_ids = cast(list[int], d.pop("departmentIds"))

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = PatchRegistrationconfigIdResponse200DataFieldsItem.from_dict(
                fields_item_data
            )

            fields.append(fields_item)

        id = d.pop("id")

        is_active = d.pop("isActive")

        minimum_age = d.pop("minimumAge")

        show_button = d.pop("showButton")

        status_id = d.pop("statusId")

        tags_for_existing_persons = cast(list[str], d.pop("tagsForExistingPersons"))

        tags_for_new_persons = cast(list[str], d.pop("tagsForNewPersons"))

        patch_registrationconfig_id_response_200_data = cls(
            blacklist=blacklist,
            campuses=campuses,
            department_ids=department_ids,
            fields=fields,
            id=id,
            is_active=is_active,
            minimum_age=minimum_age,
            show_button=show_button,
            status_id=status_id,
            tags_for_existing_persons=tags_for_existing_persons,
            tags_for_new_persons=tags_for_new_persons,
        )

        patch_registrationconfig_id_response_200_data.additional_properties = d
        return patch_registrationconfig_id_response_200_data

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
