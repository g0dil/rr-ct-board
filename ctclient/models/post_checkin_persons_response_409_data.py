from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostCheckinPersonsResponse409Data")


@_attrs_define
class PostCheckinPersonsResponse409Data:
    """
    Attributes:
        args (list[Any]):
        errors (list[Any]):
        message (str):
        message_key (str):
        translated_message (str):
    """

    args: list[Any]
    errors: list[Any]
    message: str
    message_key: str
    translated_message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args = self.args

        errors = self.errors

        message = self.message

        message_key = self.message_key

        translated_message = self.translated_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "args": args,
                "errors": errors,
                "message": message,
                "messageKey": message_key,
                "translatedMessage": translated_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        args = cast(list[Any], d.pop("args"))

        errors = cast(list[Any], d.pop("errors"))

        message = d.pop("message")

        message_key = d.pop("messageKey")

        translated_message = d.pop("translatedMessage")

        post_checkin_persons_response_409_data = cls(
            args=args,
            errors=errors,
            message=message,
            message_key=message_key,
            translated_message=translated_message,
        )

        post_checkin_persons_response_409_data.additional_properties = d
        return post_checkin_persons_response_409_data

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
