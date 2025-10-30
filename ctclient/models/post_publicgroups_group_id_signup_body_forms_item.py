from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_publicgroups_group_id_signup_body_forms_item_form_item import (
        PostPublicgroupsGroupIdSignupBodyFormsItemFormItem,
    )


T = TypeVar("T", bound="PostPublicgroupsGroupIdSignupBodyFormsItem")


@_attrs_define
class PostPublicgroupsGroupIdSignupBodyFormsItem:
    """
    Attributes:
        form (list[PostPublicgroupsGroupIdSignupBodyFormsItemFormItem]): The form data for the current person.
        person_id (int | Unset): The person ID the current form applies to. Can be empty if a single new user is about
            to sign up.
    """

    form: list[PostPublicgroupsGroupIdSignupBodyFormsItemFormItem]
    person_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form = []
        for form_item_data in self.form:
            form_item = form_item_data.to_dict()
            form.append(form_item)

        person_id = self.person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "form": form,
            }
        )
        if person_id is not UNSET:
            field_dict["personId"] = person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_publicgroups_group_id_signup_body_forms_item_form_item import (
            PostPublicgroupsGroupIdSignupBodyFormsItemFormItem,
        )

        d = dict(src_dict)
        form = []
        _form = d.pop("form")
        for form_item_data in _form:
            form_item = PostPublicgroupsGroupIdSignupBodyFormsItemFormItem.from_dict(
                form_item_data
            )

            form.append(form_item)

        person_id = d.pop("personId", UNSET)

        post_publicgroups_group_id_signup_body_forms_item = cls(
            form=form,
            person_id=person_id,
        )

        post_publicgroups_group_id_signup_body_forms_item.additional_properties = d
        return post_publicgroups_group_id_signup_body_forms_item

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
