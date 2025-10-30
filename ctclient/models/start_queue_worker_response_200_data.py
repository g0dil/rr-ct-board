from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartQueueWorkerResponse200Data")


@_attrs_define
class StartQueueWorkerResponse200Data:
    """
    Attributes:
        messages (list[str] | Unset): Messages from Worker
        queue (str | Unset): Name of Queue Example: default.
    """

    messages: list[str] | Unset = UNSET
    queue: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        messages: list[str] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages

        queue = self.queue

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if messages is not UNSET:
            field_dict["messages"] = messages
        if queue is not UNSET:
            field_dict["queue"] = queue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        messages = cast(list[str], d.pop("messages", UNSET))

        queue = d.pop("queue", UNSET)

        start_queue_worker_response_200_data = cls(
            messages=messages,
            queue=queue,
        )

        start_queue_worker_response_200_data.additional_properties = d
        return start_queue_worker_response_200_data

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
