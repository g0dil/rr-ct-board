from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSsoLoginsResponse200DataItem")


@_attrs_define
class GetSsoLoginsResponse200DataItem:
    """
    Attributes:
        id (int):
        login_link (str):
        name (str):
        type_ (str):
    """

    id: int
    login_link: str
    name: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        login_link = self.login_link

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "loginLink": login_link,
                "name": name,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        login_link = d.pop("loginLink")

        name = d.pop("name")

        type_ = d.pop("type")

        get_sso_logins_response_200_data_item = cls(
            id=id,
            login_link=login_link,
            name=name,
            type_=type_,
        )

        get_sso_logins_response_200_data_item.additional_properties = d
        return get_sso_logins_response_200_data_item

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
