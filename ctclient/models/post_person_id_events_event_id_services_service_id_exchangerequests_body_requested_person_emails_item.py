from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="PostPersonIdEventsEventIdServicesServiceIdExchangerequestsBodyRequestedPersonEmailsItem",
)


@_attrs_define
class PostPersonIdEventsEventIdServicesServiceIdExchangerequestsBodyRequestedPersonEmailsItem:
    """
    Attributes:
        contact_label_id (int):
        email (str):
        is_default (bool):
    """

    contact_label_id: int
    email: str
    is_default: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_label_id = self.contact_label_id

        email = self.email

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contactLabelId": contact_label_id,
                "email": email,
                "isDefault": is_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contact_label_id = d.pop("contactLabelId")

        email = d.pop("email")

        is_default = d.pop("isDefault")

        post_person_id_events_event_id_services_service_id_exchangerequests_body_requested_person_emails_item = cls(
            contact_label_id=contact_label_id,
            email=email,
            is_default=is_default,
        )

        post_person_id_events_event_id_services_service_id_exchangerequests_body_requested_person_emails_item.additional_properties = d
        return post_person_id_events_event_id_services_service_id_exchangerequests_body_requested_person_emails_item

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
