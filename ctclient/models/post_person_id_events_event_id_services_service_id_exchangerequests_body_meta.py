from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="PostPersonIdEventsEventIdServicesServiceIdExchangerequestsBodyMeta"
)


@_attrs_define
class PostPersonIdEventsEventIdServicesServiceIdExchangerequestsBodyMeta:
    """
    Attributes:
        modified_date (str | Unset):
    """

    modified_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modified_date = self.modified_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        modified_date = d.pop("modifiedDate", UNSET)

        post_person_id_events_event_id_services_service_id_exchangerequests_body_meta = cls(
            modified_date=modified_date,
        )

        post_person_id_events_event_id_services_service_id_exchangerequests_body_meta.additional_properties = d
        return post_person_id_events_event_id_services_service_id_exchangerequests_body_meta

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
