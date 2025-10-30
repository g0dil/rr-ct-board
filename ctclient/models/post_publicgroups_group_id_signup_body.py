from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_publicgroups_group_id_signup_body_forms_item import (
        PostPublicgroupsGroupIdSignupBodyFormsItem,
    )


T = TypeVar("T", bound="PostPublicgroupsGroupIdSignupBody")


@_attrs_define
class PostPublicgroupsGroupIdSignupBody:
    """
    Attributes:
        forms (list[PostPublicgroupsGroupIdSignupBodyFormsItem]): A list of form data containing a form object for each
            person that should be signed up.
        token (str): The sign up token.
        sign_out_url_template (str | Unset): Url used in the mail sent to the user. Example:
            https://homepage.de/$groupId/$token.
    """

    forms: list[PostPublicgroupsGroupIdSignupBodyFormsItem]
    token: str
    sign_out_url_template: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        forms = []
        for forms_item_data in self.forms:
            forms_item = forms_item_data.to_dict()
            forms.append(forms_item)

        token = self.token

        sign_out_url_template = self.sign_out_url_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "forms": forms,
                "token": token,
            }
        )
        if sign_out_url_template is not UNSET:
            field_dict["signOutUrlTemplate"] = sign_out_url_template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_publicgroups_group_id_signup_body_forms_item import (
            PostPublicgroupsGroupIdSignupBodyFormsItem,
        )

        d = dict(src_dict)
        forms = []
        _forms = d.pop("forms")
        for forms_item_data in _forms:
            forms_item = PostPublicgroupsGroupIdSignupBodyFormsItem.from_dict(
                forms_item_data
            )

            forms.append(forms_item)

        token = d.pop("token")

        sign_out_url_template = d.pop("signOutUrlTemplate", UNSET)

        post_publicgroups_group_id_signup_body = cls(
            forms=forms,
            token=token,
            sign_out_url_template=sign_out_url_template,
        )

        post_publicgroups_group_id_signup_body.additional_properties = d
        return post_publicgroups_group_id_signup_body

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
