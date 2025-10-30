from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.registration_config_campuses_item_campus_meta_created_person import (
        RegistrationConfigCampusesItemCampusMetaCreatedPerson,
    )
    from ..models.registration_config_campuses_item_campus_meta_modified_person import (
        RegistrationConfigCampusesItemCampusMetaModifiedPerson,
    )


T = TypeVar("T", bound="RegistrationConfigCampusesItemCampusMeta")


@_attrs_define
class RegistrationConfigCampusesItemCampusMeta:
    """
    Example:
        {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson': {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z',
            'modifiedPerson': {'id': 1}}

    Attributes:
        created_date (datetime.datetime): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        created_person (RegistrationConfigCampusesItemCampusMetaCreatedPerson):
        modified_date (datetime.datetime | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        modified_person (RegistrationConfigCampusesItemCampusMetaModifiedPerson | Unset):
    """

    created_date: datetime.datetime
    created_person: RegistrationConfigCampusesItemCampusMetaCreatedPerson
    modified_date: datetime.datetime | Unset = UNSET
    modified_person: RegistrationConfigCampusesItemCampusMetaModifiedPerson | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_date = self.created_date.isoformat()

        created_person = self.created_person.to_dict()

        modified_date: str | Unset = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat()

        modified_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modified_person, Unset):
            modified_person = self.modified_person.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdDate": created_date,
                "createdPerson": created_person,
            }
        )
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if modified_person is not UNSET:
            field_dict["modifiedPerson"] = modified_person

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registration_config_campuses_item_campus_meta_created_person import (
            RegistrationConfigCampusesItemCampusMetaCreatedPerson,
        )
        from ..models.registration_config_campuses_item_campus_meta_modified_person import (
            RegistrationConfigCampusesItemCampusMetaModifiedPerson,
        )

        d = dict(src_dict)
        created_date = isoparse(d.pop("createdDate"))

        created_person = (
            RegistrationConfigCampusesItemCampusMetaCreatedPerson.from_dict(
                d.pop("createdPerson")
            )
        )

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: datetime.datetime | Unset
        if isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        _modified_person = d.pop("modifiedPerson", UNSET)
        modified_person: RegistrationConfigCampusesItemCampusMetaModifiedPerson | Unset
        if isinstance(_modified_person, Unset):
            modified_person = UNSET
        else:
            modified_person = (
                RegistrationConfigCampusesItemCampusMetaModifiedPerson.from_dict(
                    _modified_person
                )
            )

        registration_config_campuses_item_campus_meta = cls(
            created_date=created_date,
            created_person=created_person,
            modified_date=modified_date,
            modified_person=modified_person,
        )

        registration_config_campuses_item_campus_meta.additional_properties = d
        return registration_config_campuses_item_campus_meta

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
