from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_person_properties_response_200_data_additional_property import (
        GetPersonPropertiesResponse200DataAdditionalProperty,
    )


T = TypeVar("T", bound="GetPersonPropertiesResponse200Data")


@_attrs_define
class GetPersonPropertiesResponse200Data:
    """ """

    additional_properties: dict[
        str, GetPersonPropertiesResponse200DataAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_person_properties_response_200_data_additional_property import (
            GetPersonPropertiesResponse200DataAdditionalProperty,
        )

        d = dict(src_dict)
        get_person_properties_response_200_data = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                GetPersonPropertiesResponse200DataAdditionalProperty.from_dict(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        get_person_properties_response_200_data.additional_properties = (
            additional_properties
        )
        return get_person_properties_response_200_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> GetPersonPropertiesResponse200DataAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: GetPersonPropertiesResponse200DataAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
