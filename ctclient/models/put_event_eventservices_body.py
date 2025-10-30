from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_event_eventservices_body_services_item import (
        PutEventEventservicesBodyServicesItem,
    )


T = TypeVar("T", bound="PutEventEventservicesBody")


@_attrs_define
class PutEventEventservicesBody:
    """
    Attributes:
        event_id (int):
        services (list[PutEventEventservicesBodyServicesItem]):
    """

    event_id: int
    services: list[PutEventEventservicesBodyServicesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        services = []
        for services_item_data in self.services:
            services_item = services_item_data.to_dict()
            services.append(services_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventId": event_id,
                "services": services,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_event_eventservices_body_services_item import (
            PutEventEventservicesBodyServicesItem,
        )

        d = dict(src_dict)
        event_id = d.pop("eventId")

        services = []
        _services = d.pop("services")
        for services_item_data in _services:
            services_item = PutEventEventservicesBodyServicesItem.from_dict(
                services_item_data
            )

            services.append(services_item)

        put_event_eventservices_body = cls(
            event_id=event_id,
            services=services,
        )

        put_event_eventservices_body.additional_properties = d
        return put_event_eventservices_body

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
