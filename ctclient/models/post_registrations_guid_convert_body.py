from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_registrations_guid_convert_body_form_data_item import (
        PostRegistrationsGuidConvertBodyFormDataItem,
    )


T = TypeVar("T", bound="PostRegistrationsGuidConvertBody")


@_attrs_define
class PostRegistrationsGuidConvertBody:
    """
    Attributes:
        form_data (list[PostRegistrationsGuidConvertBodyFormDataItem]):
        person_id (int | Unset): If specified, this indicates with existing person the new account should be linked to.
    """

    form_data: list[PostRegistrationsGuidConvertBodyFormDataItem]
    person_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form_data = []
        for form_data_item_data in self.form_data:
            form_data_item = form_data_item_data.to_dict()
            form_data.append(form_data_item)

        person_id = self.person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formData": form_data,
            }
        )
        if person_id is not UNSET:
            field_dict["personId"] = person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_registrations_guid_convert_body_form_data_item import (
            PostRegistrationsGuidConvertBodyFormDataItem,
        )

        d = dict(src_dict)
        form_data = []
        _form_data = d.pop("formData")
        for form_data_item_data in _form_data:
            form_data_item = PostRegistrationsGuidConvertBodyFormDataItem.from_dict(
                form_data_item_data
            )

            form_data.append(form_data_item)

        person_id = d.pop("personId", UNSET)

        post_registrations_guid_convert_body = cls(
            form_data=form_data,
            person_id=person_id,
        )

        post_registrations_guid_convert_body.additional_properties = d
        return post_registrations_guid_convert_body

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
