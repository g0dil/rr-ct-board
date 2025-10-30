from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meta_data_modified_id_modified_person import (
        MetaDataModifiedIdModifiedPerson,
    )


T = TypeVar("T", bound="MetaDataModifiedId")


@_attrs_define
class MetaDataModifiedId:
    """
    Attributes:
        modified_date (datetime.datetime | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        modified_person (MetaDataModifiedIdModifiedPerson | Unset):
    """

    modified_date: datetime.datetime | Unset = UNSET
    modified_person: MetaDataModifiedIdModifiedPerson | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modified_date: str | Unset = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat()

        modified_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modified_person, Unset):
            modified_person = self.modified_person.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if modified_person is not UNSET:
            field_dict["modifiedPerson"] = modified_person

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta_data_modified_id_modified_person import (
            MetaDataModifiedIdModifiedPerson,
        )

        d = dict(src_dict)
        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: datetime.datetime | Unset
        if isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        _modified_person = d.pop("modifiedPerson", UNSET)
        modified_person: MetaDataModifiedIdModifiedPerson | Unset
        if isinstance(_modified_person, Unset):
            modified_person = UNSET
        else:
            modified_person = MetaDataModifiedIdModifiedPerson.from_dict(
                _modified_person
            )

        meta_data_modified_id = cls(
            modified_date=modified_date,
            modified_person=modified_person,
        )

        meta_data_modified_id.additional_properties = d
        return meta_data_modified_id

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
