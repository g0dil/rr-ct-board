from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_agenda_email_response_200_args import (
        SendAgendaEmailResponse200Args,
    )
    from ..models.send_agenda_email_response_200_errors_item import (
        SendAgendaEmailResponse200ErrorsItem,
    )


T = TypeVar("T", bound="SendAgendaEmailResponse200")


@_attrs_define
class SendAgendaEmailResponse200:
    """
    Attributes:
        args (SendAgendaEmailResponse200Args | Unset):
        errors (list[SendAgendaEmailResponse200ErrorsItem] | Unset): Array of DomainObjects with people, who have no
            eMail Addresses.
        message (str | Unset):  Example: 5 recipients have no eMail address. No eMail is sent to them..
        message_key (str | Unset):  Example: agenda.mail.missing.email.
        translated_message (str | Unset):  Example: 5 Empfänger haben keine E-Mail Adresse. Keine E-Mail wurde an sie
            geschickt..
    """

    args: SendAgendaEmailResponse200Args | Unset = UNSET
    errors: list[SendAgendaEmailResponse200ErrorsItem] | Unset = UNSET
    message: str | Unset = UNSET
    message_key: str | Unset = UNSET
    translated_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

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
        from ..models.send_agenda_email_response_200_args import (
            SendAgendaEmailResponse200Args,
        )
        from ..models.send_agenda_email_response_200_errors_item import (
            SendAgendaEmailResponse200ErrorsItem,
        )

        d = dict(src_dict)
        _args = d.pop("args", UNSET)
        args: SendAgendaEmailResponse200Args | Unset
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = SendAgendaEmailResponse200Args.from_dict(_args)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = SendAgendaEmailResponse200ErrorsItem.from_dict(
                errors_item_data
            )

            errors.append(errors_item)

        message = d.pop("message", UNSET)

        message_key = d.pop("messageKey", UNSET)

        translated_message = d.pop("translatedMessage", UNSET)

        send_agenda_email_response_200 = cls(
            args=args,
            errors=errors,
            message=message,
            message_key=message_key,
            translated_message=translated_message,
        )

        send_agenda_email_response_200.additional_properties = d
        return send_agenda_email_response_200

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
