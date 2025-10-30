from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_login_totp_response_200_data_status import (
    PostLoginTotpResponse200DataStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostLoginTotpResponse200Data")


@_attrs_define
class PostLoginTotpResponse200Data:
    """
    Attributes:
        status (PostLoginTotpResponse200DataStatus):
        redirect_to (str | Unset):
    """

    status: PostLoginTotpResponse200DataStatus
    redirect_to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        redirect_to = self.redirect_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if redirect_to is not UNSET:
            field_dict["redirectTo"] = redirect_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = PostLoginTotpResponse200DataStatus(d.pop("status"))

        redirect_to = d.pop("redirectTo", UNSET)

        post_login_totp_response_200_data = cls(
            status=status,
            redirect_to=redirect_to,
        )

        post_login_totp_response_200_data.additional_properties = d
        return post_login_totp_response_200_data

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
