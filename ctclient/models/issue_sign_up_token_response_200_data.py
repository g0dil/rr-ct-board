from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_sign_up_token_response_200_data_group import (
        IssueSignUpTokenResponse200DataGroup,
    )


T = TypeVar("T", bound="IssueSignUpTokenResponse200Data")


@_attrs_define
class IssueSignUpTokenResponse200Data:
    """
    Attributes:
        email (None | str | Unset): Provide eMail
        group (IssueSignUpTokenResponse200DataGroup | Unset): Basic Group Information
        requester_id (int | None | Unset): Provided PersonId
        token (str | Unset): Sign Up Token
        url (str | Unset): Link To Sign Up Form
    """

    email: None | str | Unset = UNSET
    group: IssueSignUpTokenResponse200DataGroup | Unset = UNSET
    requester_id: int | None | Unset = UNSET
    token: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        requester_id: int | None | Unset
        if isinstance(self.requester_id, Unset):
            requester_id = UNSET
        else:
            requester_id = self.requester_id

        token = self.token

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if group is not UNSET:
            field_dict["group"] = group
        if requester_id is not UNSET:
            field_dict["requesterId"] = requester_id
        if token is not UNSET:
            field_dict["token"] = token
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_sign_up_token_response_200_data_group import (
            IssueSignUpTokenResponse200DataGroup,
        )

        d = dict(src_dict)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        _group = d.pop("group", UNSET)
        group: IssueSignUpTokenResponse200DataGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = IssueSignUpTokenResponse200DataGroup.from_dict(_group)

        def _parse_requester_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        requester_id = _parse_requester_id(d.pop("requesterId", UNSET))

        token = d.pop("token", UNSET)

        url = d.pop("url", UNSET)

        issue_sign_up_token_response_200_data = cls(
            email=email,
            group=group,
            requester_id=requester_id,
            token=token,
            url=url,
        )

        issue_sign_up_token_response_200_data.additional_properties = d
        return issue_sign_up_token_response_200_data

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
