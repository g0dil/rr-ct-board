from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_persons_birthdays_response_200_data_item_person_domain_attributes import (
        GetPersonsBirthdaysResponse200DataItemPersonDomainAttributes,
    )


T = TypeVar("T", bound="GetPersonsBirthdaysResponse200DataItemPerson")


@_attrs_define
class GetPersonsBirthdaysResponse200DataItemPerson:
    """
    Attributes:
        api_url (str):
        domain_attributes (GetPersonsBirthdaysResponse200DataItemPersonDomainAttributes):
        domain_identifier (str):
        domain_type (str):
        frontend_url (str):
        image_url (str):
        title (str):
    """

    api_url: str
    domain_attributes: GetPersonsBirthdaysResponse200DataItemPersonDomainAttributes
    domain_identifier: str
    domain_type: str
    frontend_url: str
    image_url: str
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_url = self.api_url

        domain_attributes = self.domain_attributes.to_dict()

        domain_identifier = self.domain_identifier

        domain_type = self.domain_type

        frontend_url = self.frontend_url

        image_url = self.image_url

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiUrl": api_url,
                "domainAttributes": domain_attributes,
                "domainIdentifier": domain_identifier,
                "domainType": domain_type,
                "frontendUrl": frontend_url,
                "imageUrl": image_url,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_persons_birthdays_response_200_data_item_person_domain_attributes import (
            GetPersonsBirthdaysResponse200DataItemPersonDomainAttributes,
        )

        d = dict(src_dict)
        api_url = d.pop("apiUrl")

        domain_attributes = (
            GetPersonsBirthdaysResponse200DataItemPersonDomainAttributes.from_dict(
                d.pop("domainAttributes")
            )
        )

        domain_identifier = d.pop("domainIdentifier")

        domain_type = d.pop("domainType")

        frontend_url = d.pop("frontendUrl")

        image_url = d.pop("imageUrl")

        title = d.pop("title")

        get_persons_birthdays_response_200_data_item_person = cls(
            api_url=api_url,
            domain_attributes=domain_attributes,
            domain_identifier=domain_identifier,
            domain_type=domain_type,
            frontend_url=frontend_url,
            image_url=image_url,
            title=title,
        )

        get_persons_birthdays_response_200_data_item_person.additional_properties = d
        return get_persons_birthdays_response_200_data_item_person

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
