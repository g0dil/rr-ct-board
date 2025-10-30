from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAccountByIdResponse200DataPermissions")


@_attrs_define
class GetAccountByIdResponse200DataPermissions:
    """
    Attributes:
        allow_posting (bool): Flag, if user can use this account to post a transaction.
    """

    allow_posting: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_posting = self.allow_posting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowPosting": allow_posting,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_posting = d.pop("allowPosting")

        get_account_by_id_response_200_data_permissions = cls(
            allow_posting=allow_posting,
        )

        get_account_by_id_response_200_data_permissions.additional_properties = d
        return get_account_by_id_response_200_data_permissions

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
