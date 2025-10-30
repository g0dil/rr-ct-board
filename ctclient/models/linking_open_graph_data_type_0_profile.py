from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkingOpenGraphDataType0Profile")


@_attrs_define
class LinkingOpenGraphDataType0Profile:
    """
    Example:
        {'firstName': 'John', 'gender': 'male', 'lastName': 'Doe', 'username': 'johndoe'}

    Attributes:
        first_name (str | Unset): The first name of the individual.
        gender (str | Unset): The gender of the individual.
        last_name (str | Unset): The last name of the individual.
        username (str | Unset): The username of the individual on the platform.
    """

    first_name: str | Unset = UNSET
    gender: str | Unset = UNSET
    last_name: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        gender = self.gender

        last_name = self.last_name

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("firstName", UNSET)

        gender = d.pop("gender", UNSET)

        last_name = d.pop("lastName", UNSET)

        username = d.pop("username", UNSET)

        linking_open_graph_data_type_0_profile = cls(
            first_name=first_name,
            gender=gender,
            last_name=last_name,
            username=username,
        )

        linking_open_graph_data_type_0_profile.additional_properties = d
        return linking_open_graph_data_type_0_profile

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
