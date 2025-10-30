from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_subscriptions_person_id_response_200_data_item_type_1_meta_type_0_created_person import (
        GetSubscriptionsPersonIdResponse200DataItemType1MetaType0CreatedPerson,
    )
    from ..models.get_subscriptions_person_id_response_200_data_item_type_1_meta_type_0_modified_person import (
        GetSubscriptionsPersonIdResponse200DataItemType1MetaType0ModifiedPerson,
    )


T = TypeVar("T", bound="GetSubscriptionsPersonIdResponse200DataItemType1MetaType0")


@_attrs_define
class GetSubscriptionsPersonIdResponse200DataItemType1MetaType0:
    """
    Attributes:
        created_date (datetime.datetime | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        created_person (GetSubscriptionsPersonIdResponse200DataItemType1MetaType0CreatedPerson | Unset):
        modified_date (datetime.datetime | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        modified_person (GetSubscriptionsPersonIdResponse200DataItemType1MetaType0ModifiedPerson | Unset):
    """

    created_date: datetime.datetime | Unset = UNSET
    created_person: (
        GetSubscriptionsPersonIdResponse200DataItemType1MetaType0CreatedPerson | Unset
    ) = UNSET
    modified_date: datetime.datetime | Unset = UNSET
    modified_person: (
        GetSubscriptionsPersonIdResponse200DataItemType1MetaType0ModifiedPerson | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_date: str | Unset = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        created_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_person, Unset):
            created_person = self.created_person.to_dict()

        modified_date: str | Unset = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat()

        modified_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modified_person, Unset):
            modified_person = self.modified_person.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if created_person is not UNSET:
            field_dict["createdPerson"] = created_person
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if modified_person is not UNSET:
            field_dict["modifiedPerson"] = modified_person

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_subscriptions_person_id_response_200_data_item_type_1_meta_type_0_created_person import (
            GetSubscriptionsPersonIdResponse200DataItemType1MetaType0CreatedPerson,
        )
        from ..models.get_subscriptions_person_id_response_200_data_item_type_1_meta_type_0_modified_person import (
            GetSubscriptionsPersonIdResponse200DataItemType1MetaType0ModifiedPerson,
        )

        d = dict(src_dict)
        _created_date = d.pop("createdDate", UNSET)
        created_date: datetime.datetime | Unset
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        _created_person = d.pop("createdPerson", UNSET)
        created_person: (
            GetSubscriptionsPersonIdResponse200DataItemType1MetaType0CreatedPerson
            | Unset
        )
        if isinstance(_created_person, Unset):
            created_person = UNSET
        else:
            created_person = GetSubscriptionsPersonIdResponse200DataItemType1MetaType0CreatedPerson.from_dict(
                _created_person
            )

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: datetime.datetime | Unset
        if isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = isoparse(_modified_date)

        _modified_person = d.pop("modifiedPerson", UNSET)
        modified_person: (
            GetSubscriptionsPersonIdResponse200DataItemType1MetaType0ModifiedPerson
            | Unset
        )
        if isinstance(_modified_person, Unset):
            modified_person = UNSET
        else:
            modified_person = GetSubscriptionsPersonIdResponse200DataItemType1MetaType0ModifiedPerson.from_dict(
                _modified_person
            )

        get_subscriptions_person_id_response_200_data_item_type_1_meta_type_0 = cls(
            created_date=created_date,
            created_person=created_person,
            modified_date=modified_date,
            modified_person=modified_person,
        )

        get_subscriptions_person_id_response_200_data_item_type_1_meta_type_0.additional_properties = d
        return get_subscriptions_person_id_response_200_data_item_type_1_meta_type_0

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
