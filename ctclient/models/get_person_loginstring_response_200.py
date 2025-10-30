from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPersonLoginstringResponse200")


@_attrs_define
class GetPersonLoginstringResponse200:
    """
    Attributes:
        login_string (str | Unset):
        person_id (str | Unset):
    """

    login_string: str | Unset = UNSET
    person_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        login_string = self.login_string

        person_id = self.person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if login_string is not UNSET:
            field_dict["loginString"] = login_string
        if person_id is not UNSET:
            field_dict["personId"] = person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login_string = d.pop("loginString", UNSET)

        person_id = d.pop("personId", UNSET)

        get_person_loginstring_response_200 = cls(
            login_string=login_string,
            person_id=person_id,
        )

        get_person_loginstring_response_200.additional_properties = d
        return get_person_loginstring_response_200

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
