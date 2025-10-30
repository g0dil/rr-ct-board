from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchPersonsPersonidMergeDuplicateidBodyPersonEmail")


@_attrs_define
class PatchPersonsPersonidMergeDuplicateidBodyPersonEmail:
    """
    Attributes:
        contact_label_id (int | Unset):  Example: 1.
        email (str | Unset):  Example: pastor@church.com.
        is_default (bool | Unset): Marks the default eMail address. Example: True.
    """

    contact_label_id: int | Unset = UNSET
    email: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_label_id = self.contact_label_id

        email = self.email

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact_label_id is not UNSET:
            field_dict["contactLabelId"] = contact_label_id
        if email is not UNSET:
            field_dict["email"] = email
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contact_label_id = d.pop("contactLabelId", UNSET)

        email = d.pop("email", UNSET)

        is_default = d.pop("isDefault", UNSET)

        patch_persons_personid_merge_duplicateid_body_person_email = cls(
            contact_label_id=contact_label_id,
            email=email,
            is_default=is_default,
        )

        patch_persons_personid_merge_duplicateid_body_person_email.additional_properties = d
        return patch_persons_personid_merge_duplicateid_body_person_email

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
