from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutAutomaticEmailBody")


@_attrs_define
class PutAutomaticEmailBody:
    """
    Attributes:
        body (str):
        is_active (bool):
        sender_id (int | None): SenderID = PersonID of one leader in that group
        subject (str):
    """

    body: str
    is_active: bool
    sender_id: int | None
    subject: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        is_active = self.is_active

        sender_id: int | None
        sender_id = self.sender_id

        subject = self.subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "isActive": is_active,
                "senderId": sender_id,
                "subject": subject,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        is_active = d.pop("isActive")

        def _parse_sender_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sender_id = _parse_sender_id(d.pop("senderId"))

        subject = d.pop("subject")

        put_automatic_email_body = cls(
            body=body,
            is_active=is_active,
            sender_id=sender_id,
            subject=subject,
        )

        put_automatic_email_body.additional_properties = d
        return put_automatic_email_body

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
