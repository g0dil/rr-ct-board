from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueSignUpTokenBody")


@_attrs_define
class IssueSignUpTokenBody:
    """
    Attributes:
        clicked (list[Any] | Unset): Array of person ids, which are clicked on group detail page. Those persons, will be
            also checked on the form site.
            The `clicked` field will be saved only in combination with `personId`.
        email (str | Unset): eMail address of not logged in user or new user.
        group_homepage_hash (str | Unset): The hash of the group homepage. If specified, the user can return to the
            group homepage after the sign up was successful.
        person_id (int | Unset): Person Id, which issues the token.
        sign_up_url_template (str | Unset): Url used in the mail sent to the user. Example:
            https://homepage.de/$groupId/$token.
    """

    clicked: list[Any] | Unset = UNSET
    email: str | Unset = UNSET
    group_homepage_hash: str | Unset = UNSET
    person_id: int | Unset = UNSET
    sign_up_url_template: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clicked: list[Any] | Unset = UNSET
        if not isinstance(self.clicked, Unset):
            clicked = self.clicked

        email = self.email

        group_homepage_hash = self.group_homepage_hash

        person_id = self.person_id

        sign_up_url_template = self.sign_up_url_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clicked is not UNSET:
            field_dict["clicked"] = clicked
        if email is not UNSET:
            field_dict["email"] = email
        if group_homepage_hash is not UNSET:
            field_dict["groupHomepageHash"] = group_homepage_hash
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if sign_up_url_template is not UNSET:
            field_dict["signUpUrlTemplate"] = sign_up_url_template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        clicked = cast(list[Any], d.pop("clicked", UNSET))

        email = d.pop("email", UNSET)

        group_homepage_hash = d.pop("groupHomepageHash", UNSET)

        person_id = d.pop("personId", UNSET)

        sign_up_url_template = d.pop("signUpUrlTemplate", UNSET)

        issue_sign_up_token_body = cls(
            clicked=clicked,
            email=email,
            group_homepage_hash=group_homepage_hash,
            person_id=person_id,
            sign_up_url_template=sign_up_url_template,
        )

        issue_sign_up_token_body.additional_properties = d
        return issue_sign_up_token_body

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
