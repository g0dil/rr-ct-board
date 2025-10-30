from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_events_event_id_facts_fact_id_response_400_args_item import (
        PutEventsEventIdFactsFactIdResponse400ArgsItem,
    )
    from ..models.put_events_event_id_facts_fact_id_response_400_errors_item import (
        PutEventsEventIdFactsFactIdResponse400ErrorsItem,
    )


T = TypeVar("T", bound="PutEventsEventIdFactsFactIdResponse400")


@_attrs_define
class PutEventsEventIdFactsFactIdResponse400:
    """
    Attributes:
        args (list[PutEventsEventIdFactsFactIdResponse400ArgsItem] | Unset):
        errors (list[PutEventsEventIdFactsFactIdResponse400ErrorsItem] | Unset):
        message (str | Unset):
        message_key (str | Unset):
        translated_message (str | Unset):
    """

    args: list[PutEventsEventIdFactsFactIdResponse400ArgsItem] | Unset = UNSET
    errors: list[PutEventsEventIdFactsFactIdResponse400ErrorsItem] | Unset = UNSET
    message: str | Unset = UNSET
    message_key: str | Unset = UNSET
    translated_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = []
            for args_item_data in self.args:
                args_item = args_item_data.to_dict()
                args.append(args_item)

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
        from ..models.put_events_event_id_facts_fact_id_response_400_args_item import (
            PutEventsEventIdFactsFactIdResponse400ArgsItem,
        )
        from ..models.put_events_event_id_facts_fact_id_response_400_errors_item import (
            PutEventsEventIdFactsFactIdResponse400ErrorsItem,
        )

        d = dict(src_dict)
        args = []
        _args = d.pop("args", UNSET)
        for args_item_data in _args or []:
            args_item = PutEventsEventIdFactsFactIdResponse400ArgsItem.from_dict(
                args_item_data
            )

            args.append(args_item)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = PutEventsEventIdFactsFactIdResponse400ErrorsItem.from_dict(
                errors_item_data
            )

            errors.append(errors_item)

        message = d.pop("message", UNSET)

        message_key = d.pop("messageKey", UNSET)

        translated_message = d.pop("translatedMessage", UNSET)

        put_events_event_id_facts_fact_id_response_400 = cls(
            args=args,
            errors=errors,
            message=message,
            message_key=message_key,
            translated_message=translated_message,
        )

        put_events_event_id_facts_fact_id_response_400.additional_properties = d
        return put_events_event_id_facts_fact_id_response_400

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
