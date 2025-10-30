from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateNewClientBody")


@_attrs_define
class CreateNewClientBody:
    """
    Example:
        {'name': 'Ein ganz neuer Mandant', 'sortKey': 5}

    Attributes:
        name (str):
        sort_key (int):
        city (str | Unset):
        email (str | Unset):
        phone (str | Unset):
        postal_code (str | Unset):
        street (str | Unset):
        treasurer_id (int | Unset):
    """

    name: str
    sort_key: int
    city: str | Unset = UNSET
    email: str | Unset = UNSET
    phone: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    street: str | Unset = UNSET
    treasurer_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        sort_key = self.sort_key

        city = self.city

        email = self.email

        phone = self.phone

        postal_code = self.postal_code

        street = self.street

        treasurer_id = self.treasurer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "sortKey": sort_key,
            }
        )
        if city is not UNSET:
            field_dict["city"] = city
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if street is not UNSET:
            field_dict["street"] = street
        if treasurer_id is not UNSET:
            field_dict["treasurerId"] = treasurer_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        sort_key = d.pop("sortKey")

        city = d.pop("city", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        street = d.pop("street", UNSET)

        treasurer_id = d.pop("treasurerId", UNSET)

        create_new_client_body = cls(
            name=name,
            sort_key=sort_key,
            city=city,
            email=email,
            phone=phone,
            postal_code=postal_code,
            street=street,
            treasurer_id=treasurer_id,
        )

        create_new_client_body.additional_properties = d
        return create_new_client_body

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
