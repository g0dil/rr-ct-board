from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendAgendaEmailBody")


@_attrs_define
class SendAgendaEmailBody:
    """
    Example:
        {'body': 'I have updated the agenda for the upcoming service. Please review the changes.', 'eventIds': [31, 32],
            'recipients': [40, 41, 116], 'sendCopyToMe': True, 'subject': 'Agenda Updated'}

    Attributes:
        body (str): E-Mail body.
        event_ids (list[int]): Array of event IDs. Multiple event IDs MUST be integrated events, i.e. all events share
            the same agenda.
        recipients (list[int]): Array of person IDs.
        subject (str): E-Mail subject.
        send_copy_to_me (bool | Unset): Flag if a mail should be send to the user sending the request. Default: False.
    """

    body: str
    event_ids: list[int]
    recipients: list[int]
    subject: str
    send_copy_to_me: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        event_ids = self.event_ids

        recipients = self.recipients

        subject = self.subject

        send_copy_to_me = self.send_copy_to_me

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "eventIds": event_ids,
                "recipients": recipients,
                "subject": subject,
            }
        )
        if send_copy_to_me is not UNSET:
            field_dict["sendCopyToMe"] = send_copy_to_me

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        event_ids = cast(list[int], d.pop("eventIds"))

        recipients = cast(list[int], d.pop("recipients"))

        subject = d.pop("subject")

        send_copy_to_me = d.pop("sendCopyToMe", UNSET)

        send_agenda_email_body = cls(
            body=body,
            event_ids=event_ids,
            recipients=recipients,
            subject=subject,
            send_copy_to_me=send_copy_to_me,
        )

        send_agenda_email_body.additional_properties = d
        return send_agenda_email_body

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
