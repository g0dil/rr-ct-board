from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchPersonResponse400")


@_attrs_define
class PatchPersonResponse400:
    """
    Attributes:
        args (list[str] | Unset):
        errors (list[str] | Unset):
        message (str | Unset):  Example: There are validation errors.
        message_key (str | Unset):  Example: validation.error.
        translated_message (str | Unset):  Example: Die eingegebenen Daten waren nicht korrekt..
    """

    args: list[str] | Unset = UNSET
    errors: list[str] | Unset = UNSET
    message: str | Unset = UNSET
    message_key: str | Unset = UNSET
    translated_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        message = self.message

        message_key = self.message_key

        translated_message = self.translated_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if args is not UNSET:
            field_dict["args"] = args
        if errors is not UNSET:
            field_dict["errors"] = errors
        if message is not UNSET:
            field_dict["message"] = message
        if message_key is not UNSET:
            field_dict["messageKey"] = message_key
        if translated_message is not UNSET:
            field_dict["translatedMessage"] = translated_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        args = cast(list[str], d.pop("args", UNSET))

        errors = cast(list[str], d.pop("errors", UNSET))

        message = d.pop("message", UNSET)

        message_key = d.pop("messageKey", UNSET)

        translated_message = d.pop("translatedMessage", UNSET)

        patch_person_response_400 = cls(
            args=args,
            errors=errors,
            message=message,
            message_key=message_key,
            translated_message=translated_message,
        )

        patch_person_response_400.additional_properties = d
        return patch_person_response_400

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
