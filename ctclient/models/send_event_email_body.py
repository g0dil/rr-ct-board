from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendEventEmailBody")


@_attrs_define
class SendEventEmailBody:
    """
    Example:
        {'appendAgendaButton': False, 'body': 'I have a updated the agenda for the upcoming service. Please review the
            changes.', 'eventIds': [31, 32], 'files': [0], 'recipients': [40, 41, 116], 'sendCopyToMe': True, 'subject':
            'Agenda Updated'}

    Attributes:
        append_agenda_button (bool): If an agenda exists for the event, a button with a link to that agenda is added to
            the mail body. Example: True.
        body (str): E-Mail body.
        event_ids (list[int]): Array of event IDs. Multiple event IDs MUST be integrated events, i.e. all events share
            the same agenda.
        files (list[int]): List of file Ids. If the file is attached to the event it is added to the mail body.
        recipients (list[int]): Array of person IDs.
        subject (str): E-Mail subject.
        send_copy_to_me (bool | Unset): Flag if a mail should be send to the user sending the request. Default: False.
    """

    append_agenda_button: bool
    body: str
    event_ids: list[int]
    files: list[int]
    recipients: list[int]
    subject: str
    send_copy_to_me: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        append_agenda_button = self.append_agenda_button

        body = self.body

        event_ids = self.event_ids

        files = self.files

        recipients = self.recipients

        subject = self.subject

        send_copy_to_me = self.send_copy_to_me

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appendAgendaButton": append_agenda_button,
                "body": body,
                "eventIds": event_ids,
                "files": files,
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
        append_agenda_button = d.pop("appendAgendaButton")

        body = d.pop("body")

        event_ids = cast(list[int], d.pop("eventIds"))

        files = cast(list[int], d.pop("files"))

        recipients = cast(list[int], d.pop("recipients"))

        subject = d.pop("subject")

        send_copy_to_me = d.pop("sendCopyToMe", UNSET)

        send_event_email_body = cls(
            append_agenda_button=append_agenda_button,
            body=body,
            event_ids=event_ids,
            files=files,
            recipients=recipients,
            subject=subject,
            send_copy_to_me=send_copy_to_me,
        )

        send_event_email_body.additional_properties = d
        return send_event_email_body

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
