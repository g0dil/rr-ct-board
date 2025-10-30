from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonPrivacyPolicyOwner")


@_attrs_define
class PersonPrivacyPolicyOwner:
    """
    Attributes:
        accepted (bool):
        accepted_type (str):
        age (int):
        allowed_to_accept (bool):
        edit_birthday (bool):
        first_name (str):
        id (int):
        image_url (str):
        last_name (str):
        accepted_date (datetime.datetime | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        accepted_who (int | Unset):
    """

    accepted: bool
    accepted_type: str
    age: int
    allowed_to_accept: bool
    edit_birthday: bool
    first_name: str
    id: int
    image_url: str
    last_name: str
    accepted_date: datetime.datetime | Unset = UNSET
    accepted_who: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        accepted_type = self.accepted_type

        age = self.age

        allowed_to_accept = self.allowed_to_accept

        edit_birthday = self.edit_birthday

        first_name = self.first_name

        id = self.id

        image_url = self.image_url

        last_name = self.last_name

        accepted_date: str | Unset = UNSET
        if not isinstance(self.accepted_date, Unset):
            accepted_date = self.accepted_date.isoformat()

        accepted_who = self.accepted_who

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted": accepted,
                "acceptedType": accepted_type,
                "age": age,
                "allowedToAccept": allowed_to_accept,
                "editBirthday": edit_birthday,
                "firstName": first_name,
                "id": id,
                "imageUrl": image_url,
                "lastName": last_name,
            }
        )
        if accepted_date is not UNSET:
            field_dict["acceptedDate"] = accepted_date
        if accepted_who is not UNSET:
            field_dict["acceptedWho"] = accepted_who

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted = d.pop("accepted")

        accepted_type = d.pop("acceptedType")

        age = d.pop("age")

        allowed_to_accept = d.pop("allowedToAccept")

        edit_birthday = d.pop("editBirthday")

        first_name = d.pop("firstName")

        id = d.pop("id")

        image_url = d.pop("imageUrl")

        last_name = d.pop("lastName")

        _accepted_date = d.pop("acceptedDate", UNSET)
        accepted_date: datetime.datetime | Unset
        if isinstance(_accepted_date, Unset):
            accepted_date = UNSET
        else:
            accepted_date = isoparse(_accepted_date)

        accepted_who = d.pop("acceptedWho", UNSET)

        person_privacy_policy_owner = cls(
            accepted=accepted,
            accepted_type=accepted_type,
            age=age,
            allowed_to_accept=allowed_to_accept,
            edit_birthday=edit_birthday,
            first_name=first_name,
            id=id,
            image_url=image_url,
            last_name=last_name,
            accepted_date=accepted_date,
            accepted_who=accepted_who,
        )

        person_privacy_policy_owner.additional_properties = d
        return person_privacy_policy_owner

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
