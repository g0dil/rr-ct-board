from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventMasterDataServicesItem")


@_attrs_define
class EventMasterDataServicesItem:
    """
    Attributes:
        allow_chat (bool | Unset):
        allow_comment_on_confirmation (bool | Unset):
        allow_control_live_agenda (bool | Unset):
        allow_decline (bool | Unset):
        allow_exchange (bool | Unset):
        cal_text_template (str | Unset):
        comment (str | Unset):
        comment_on_confirmation (bool | Unset):
        group_ids (list[int] | Unset):
        hide_person_name (bool | Unset):
        id (int | Unset):
        name (str | Unset):
        only_assign_from_groups (bool | Unset):
        send_reminder_mails (bool | Unset):
        send_service_request_emails (bool | Unset):
        service_group_id (int | Unset):
        sort_key (int | Unset):
        standard (bool | Unset):
        tag_ids (list[int] | Unset):
    """

    allow_chat: bool | Unset = UNSET
    allow_comment_on_confirmation: bool | Unset = UNSET
    allow_control_live_agenda: bool | Unset = UNSET
    allow_decline: bool | Unset = UNSET
    allow_exchange: bool | Unset = UNSET
    cal_text_template: str | Unset = UNSET
    comment: str | Unset = UNSET
    comment_on_confirmation: bool | Unset = UNSET
    group_ids: list[int] | Unset = UNSET
    hide_person_name: bool | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    only_assign_from_groups: bool | Unset = UNSET
    send_reminder_mails: bool | Unset = UNSET
    send_service_request_emails: bool | Unset = UNSET
    service_group_id: int | Unset = UNSET
    sort_key: int | Unset = UNSET
    standard: bool | Unset = UNSET
    tag_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_chat = self.allow_chat

        allow_comment_on_confirmation = self.allow_comment_on_confirmation

        allow_control_live_agenda = self.allow_control_live_agenda

        allow_decline = self.allow_decline

        allow_exchange = self.allow_exchange

        cal_text_template = self.cal_text_template

        comment = self.comment

        comment_on_confirmation = self.comment_on_confirmation

        group_ids: list[int] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        hide_person_name = self.hide_person_name

        id = self.id

        name = self.name

        only_assign_from_groups = self.only_assign_from_groups

        send_reminder_mails = self.send_reminder_mails

        send_service_request_emails = self.send_service_request_emails

        service_group_id = self.service_group_id

        sort_key = self.sort_key

        standard = self.standard

        tag_ids: list[int] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_chat is not UNSET:
            field_dict["allowChat"] = allow_chat
        if allow_comment_on_confirmation is not UNSET:
            field_dict["allowCommentOnConfirmation"] = allow_comment_on_confirmation
        if allow_control_live_agenda is not UNSET:
            field_dict["allowControlLiveAgenda"] = allow_control_live_agenda
        if allow_decline is not UNSET:
            field_dict["allowDecline"] = allow_decline
        if allow_exchange is not UNSET:
            field_dict["allowExchange"] = allow_exchange
        if cal_text_template is not UNSET:
            field_dict["calTextTemplate"] = cal_text_template
        if comment is not UNSET:
            field_dict["comment"] = comment
        if comment_on_confirmation is not UNSET:
            field_dict["commentOnConfirmation"] = comment_on_confirmation
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if hide_person_name is not UNSET:
            field_dict["hidePersonName"] = hide_person_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if only_assign_from_groups is not UNSET:
            field_dict["onlyAssignFromGroups"] = only_assign_from_groups
        if send_reminder_mails is not UNSET:
            field_dict["sendReminderMails"] = send_reminder_mails
        if send_service_request_emails is not UNSET:
            field_dict["sendServiceRequestEmails"] = send_service_request_emails
        if service_group_id is not UNSET:
            field_dict["serviceGroupId"] = service_group_id
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key
        if standard is not UNSET:
            field_dict["standard"] = standard
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_chat = d.pop("allowChat", UNSET)

        allow_comment_on_confirmation = d.pop("allowCommentOnConfirmation", UNSET)

        allow_control_live_agenda = d.pop("allowControlLiveAgenda", UNSET)

        allow_decline = d.pop("allowDecline", UNSET)

        allow_exchange = d.pop("allowExchange", UNSET)

        cal_text_template = d.pop("calTextTemplate", UNSET)

        comment = d.pop("comment", UNSET)

        comment_on_confirmation = d.pop("commentOnConfirmation", UNSET)

        group_ids = cast(list[int], d.pop("groupIds", UNSET))

        hide_person_name = d.pop("hidePersonName", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        only_assign_from_groups = d.pop("onlyAssignFromGroups", UNSET)

        send_reminder_mails = d.pop("sendReminderMails", UNSET)

        send_service_request_emails = d.pop("sendServiceRequestEmails", UNSET)

        service_group_id = d.pop("serviceGroupId", UNSET)

        sort_key = d.pop("sortKey", UNSET)

        standard = d.pop("standard", UNSET)

        tag_ids = cast(list[int], d.pop("tagIds", UNSET))

        event_master_data_services_item = cls(
            allow_chat=allow_chat,
            allow_comment_on_confirmation=allow_comment_on_confirmation,
            allow_control_live_agenda=allow_control_live_agenda,
            allow_decline=allow_decline,
            allow_exchange=allow_exchange,
            cal_text_template=cal_text_template,
            comment=comment,
            comment_on_confirmation=comment_on_confirmation,
            group_ids=group_ids,
            hide_person_name=hide_person_name,
            id=id,
            name=name,
            only_assign_from_groups=only_assign_from_groups,
            send_reminder_mails=send_reminder_mails,
            send_service_request_emails=send_service_request_emails,
            service_group_id=service_group_id,
            sort_key=sort_key,
            standard=standard,
            tag_ids=tag_ids,
        )

        event_master_data_services_item.additional_properties = d
        return event_master_data_services_item

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
