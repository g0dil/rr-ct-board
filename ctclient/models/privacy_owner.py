from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="PrivacyOwner")


@_attrs_define
class PrivacyOwner:
    """
    Attributes:
        accepted (bool):
        accepted_date (datetime.date | None): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
        accepted_type (None | str):
        accepted_who (int | None):
        age (int):
        allowed_to_accept (bool):
        edit_birthday (bool):
        first_name (str):
        id (int):
        image (str):
        last_name (str):
    """

    accepted: bool
    accepted_date: datetime.date | None
    accepted_type: None | str
    accepted_who: int | None
    age: int
    allowed_to_accept: bool
    edit_birthday: bool
    first_name: str
    id: int
    image: str
    last_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        accepted_date: None | str
        if isinstance(self.accepted_date, datetime.date):
            accepted_date = self.accepted_date.isoformat()
        else:
            accepted_date = self.accepted_date

        accepted_type: None | str
        accepted_type = self.accepted_type

        accepted_who: int | None
        accepted_who = self.accepted_who

        age = self.age

        allowed_to_accept = self.allowed_to_accept

        edit_birthday = self.edit_birthday

        first_name = self.first_name

        id = self.id

        image = self.image

        last_name = self.last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted": accepted,
                "acceptedDate": accepted_date,
                "acceptedType": accepted_type,
                "acceptedWho": accepted_who,
                "age": age,
                "allowedToAccept": allowed_to_accept,
                "editBirthday": edit_birthday,
                "firstName": first_name,
                "id": id,
                "image": image,
                "lastName": last_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted = d.pop("accepted")

        def _parse_accepted_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_date_type_0 = isoparse(data).date()

                return accepted_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None, data)

        accepted_date = _parse_accepted_date(d.pop("acceptedDate"))

        def _parse_accepted_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        accepted_type = _parse_accepted_type(d.pop("acceptedType"))

        def _parse_accepted_who(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        accepted_who = _parse_accepted_who(d.pop("acceptedWho"))

        age = d.pop("age")

        allowed_to_accept = d.pop("allowedToAccept")

        edit_birthday = d.pop("editBirthday")

        first_name = d.pop("firstName")

        id = d.pop("id")

        image = d.pop("image")

        last_name = d.pop("lastName")

        privacy_owner = cls(
            accepted=accepted,
            accepted_date=accepted_date,
            accepted_type=accepted_type,
            accepted_who=accepted_who,
            age=age,
            allowed_to_accept=allowed_to_accept,
            edit_birthday=edit_birthday,
            first_name=first_name,
            id=id,
            image=image,
            last_name=last_name,
        )

        privacy_owner.additional_properties = d
        return privacy_owner

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
