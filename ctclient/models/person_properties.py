from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_properties_invitation_status import (
    PersonPropertiesInvitationStatus,
)

T = TypeVar("T", bound="PersonProperties")


@_attrs_define
class PersonProperties:
    """
    Attributes:
        can_chat (bool):
        has_email (bool):
        image_url (None | str):
        invitation_status (PersonPropertiesInvitationStatus):
        is_archived (bool):
        is_dead (bool):
        is_saml_user (bool):
    """

    can_chat: bool
    has_email: bool
    image_url: None | str
    invitation_status: PersonPropertiesInvitationStatus
    is_archived: bool
    is_dead: bool
    is_saml_user: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_chat = self.can_chat

        has_email = self.has_email

        image_url: None | str
        image_url = self.image_url

        invitation_status = self.invitation_status.value

        is_archived = self.is_archived

        is_dead = self.is_dead

        is_saml_user = self.is_saml_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canChat": can_chat,
                "hasEmail": has_email,
                "imageUrl": image_url,
                "invitationStatus": invitation_status,
                "isArchived": is_archived,
                "isDead": is_dead,
                "isSamlUser": is_saml_user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_chat = d.pop("canChat")

        has_email = d.pop("hasEmail")

        def _parse_image_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url = _parse_image_url(d.pop("imageUrl"))

        invitation_status = PersonPropertiesInvitationStatus(d.pop("invitationStatus"))

        is_archived = d.pop("isArchived")

        is_dead = d.pop("isDead")

        is_saml_user = d.pop("isSamlUser")

        person_properties = cls(
            can_chat=can_chat,
            has_email=has_email,
            image_url=image_url,
            invitation_status=invitation_status,
            is_archived=is_archived,
            is_dead=is_dead,
            is_saml_user=is_saml_user,
        )

        person_properties.additional_properties = d
        return person_properties

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
