from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.meta_data_created_id_created_person import (
        MetaDataCreatedIdCreatedPerson,
    )


T = TypeVar("T", bound="MetaDataCreatedId")


@_attrs_define
class MetaDataCreatedId:
    """
    Attributes:
        created_date (datetime.datetime): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        created_person (MetaDataCreatedIdCreatedPerson):
    """

    created_date: datetime.datetime
    created_person: MetaDataCreatedIdCreatedPerson
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_date = self.created_date.isoformat()

        created_person = self.created_person.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdDate": created_date,
                "createdPerson": created_person,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta_data_created_id_created_person import (
            MetaDataCreatedIdCreatedPerson,
        )

        d = dict(src_dict)
        created_date = isoparse(d.pop("createdDate"))

        created_person = MetaDataCreatedIdCreatedPerson.from_dict(
            d.pop("createdPerson")
        )

        meta_data_created_id = cls(
            created_date=created_date,
            created_person=created_person,
        )

        meta_data_created_id.additional_properties = d
        return meta_data_created_id

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
