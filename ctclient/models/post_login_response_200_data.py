from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostLoginResponse200Data")


@_attrs_define
class PostLoginResponse200Data:
    """
    Attributes:
        location (str):
        message (str):
        person_id (int):
        status (str):
    """

    location: str
    message: str
    person_id: int
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location

        message = self.message

        person_id = self.person_id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
                "message": message,
                "personId": person_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location = d.pop("location")

        message = d.pop("message")

        person_id = d.pop("personId")

        status = d.pop("status")

        post_login_response_200_data = cls(
            location=location,
            message=message,
            person_id=person_id,
            status=status,
        )

        post_login_response_200_data.additional_properties = d
        return post_login_response_200_data

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
