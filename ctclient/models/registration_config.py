from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.registration_config_campuses_item import (
        RegistrationConfigCampusesItem,
    )
    from ..models.registration_config_fields_item import RegistrationConfigFieldsItem
    from ..models.registration_config_meta import RegistrationConfigMeta


T = TypeVar("T", bound="RegistrationConfig")


@_attrs_define
class RegistrationConfig:
    """
    Attributes:
        blacklist (list[str]):
        campuses (list[RegistrationConfigCampusesItem]):
        department_ids (list[int]):
        fields (list[RegistrationConfigFieldsItem]):
        guid (str):
        id (int):
        is_active (bool):
        is_complete (bool): Indiciates if the registration configuration has all required data and is complete.
        minimum_age (int):
        show_button (bool):
        status_id (int):
        tags_for_existing_persons (list[str]):
        tags_for_new_persons (list[str]):
        meta (RegistrationConfigMeta | Unset):  Example: {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson': {'id':
            1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
    """

    blacklist: list[str]
    campuses: list[RegistrationConfigCampusesItem]
    department_ids: list[int]
    fields: list[RegistrationConfigFieldsItem]
    guid: str
    id: int
    is_active: bool
    is_complete: bool
    minimum_age: int
    show_button: bool
    status_id: int
    tags_for_existing_persons: list[str]
    tags_for_new_persons: list[str]
    meta: RegistrationConfigMeta | Unset = UNSET
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

        guid = self.guid

        id = self.id

        is_active = self.is_active

        is_complete = self.is_complete

        minimum_age = self.minimum_age

        show_button = self.show_button

        status_id = self.status_id

        tags_for_existing_persons = self.tags_for_existing_persons

        tags_for_new_persons = self.tags_for_new_persons

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blacklist": blacklist,
                "campuses": campuses,
                "departmentIds": department_ids,
                "fields": fields,
                "guid": guid,
                "id": id,
                "isActive": is_active,
                "isComplete": is_complete,
                "minimumAge": minimum_age,
                "showButton": show_button,
                "statusId": status_id,
                "tagsForExistingPersons": tags_for_existing_persons,
                "tagsForNewPersons": tags_for_new_persons,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registration_config_campuses_item import (
            RegistrationConfigCampusesItem,
        )
        from ..models.registration_config_fields_item import (
            RegistrationConfigFieldsItem,
        )
        from ..models.registration_config_meta import RegistrationConfigMeta

        d = dict(src_dict)
        blacklist = cast(list[str], d.pop("blacklist"))

        campuses = []
        _campuses = d.pop("campuses")
        for campuses_item_data in _campuses:
            campuses_item = RegistrationConfigCampusesItem.from_dict(campuses_item_data)

            campuses.append(campuses_item)

        department_ids = cast(list[int], d.pop("departmentIds"))

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = RegistrationConfigFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        guid = d.pop("guid")

        id = d.pop("id")

        is_active = d.pop("isActive")

        is_complete = d.pop("isComplete")

        minimum_age = d.pop("minimumAge")

        show_button = d.pop("showButton")

        status_id = d.pop("statusId")

        tags_for_existing_persons = cast(list[str], d.pop("tagsForExistingPersons"))

        tags_for_new_persons = cast(list[str], d.pop("tagsForNewPersons"))

        _meta = d.pop("meta", UNSET)
        meta: RegistrationConfigMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = RegistrationConfigMeta.from_dict(_meta)

        registration_config = cls(
            blacklist=blacklist,
            campuses=campuses,
            department_ids=department_ids,
            fields=fields,
            guid=guid,
            id=id,
            is_active=is_active,
            is_complete=is_complete,
            minimum_age=minimum_age,
            show_button=show_button,
            status_id=status_id,
            tags_for_existing_persons=tags_for_existing_persons,
            tags_for_new_persons=tags_for_new_persons,
            meta=meta,
        )

        registration_config.additional_properties = d
        return registration_config

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
