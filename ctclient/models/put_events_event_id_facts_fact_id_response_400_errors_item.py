from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_events_event_id_facts_fact_id_response_400_errors_item_args import (
        PutEventsEventIdFactsFactIdResponse400ErrorsItemArgs,
    )


T = TypeVar("T", bound="PutEventsEventIdFactsFactIdResponse400ErrorsItem")


@_attrs_define
class PutEventsEventIdFactsFactIdResponse400ErrorsItem:
    """
    Attributes:
        args (PutEventsEventIdFactsFactIdResponse400ErrorsItemArgs | Unset):
        field_id (str | Unset):
        message (str | Unset):
        message_key (str | Unset):
    """

    args: PutEventsEventIdFactsFactIdResponse400ErrorsItemArgs | Unset = UNSET
    field_id: str | Unset = UNSET
    message: str | Unset = UNSET
    message_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        field_id = self.field_id

        message = self.message

        message_key = self.message_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if args is not UNSET:
            field_dict["args"] = args
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if message is not UNSET:
            field_dict["message"] = message
        if message_key is not UNSET:
            field_dict["messageKey"] = message_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_events_event_id_facts_fact_id_response_400_errors_item_args import (
            PutEventsEventIdFactsFactIdResponse400ErrorsItemArgs,
        )

        d = dict(src_dict)
        _args = d.pop("args", UNSET)
        args: PutEventsEventIdFactsFactIdResponse400ErrorsItemArgs | Unset
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = PutEventsEventIdFactsFactIdResponse400ErrorsItemArgs.from_dict(_args)

        field_id = d.pop("fieldId", UNSET)

        message = d.pop("message", UNSET)

        message_key = d.pop("messageKey", UNSET)

        put_events_event_id_facts_fact_id_response_400_errors_item = cls(
            args=args,
            field_id=field_id,
            message=message,
            message_key=message_key,
        )

        put_events_event_id_facts_fact_id_response_400_errors_item.additional_properties = d
        return put_events_event_id_facts_fact_id_response_400_errors_item

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
