from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.website_data_calendar_domain_type import WebsiteDataCalendarDomainType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.website_data_calendar_domain_data import WebsiteDataCalendarDomainData


T = TypeVar("T", bound="WebsiteDataCalendar")


@_attrs_define
class WebsiteDataCalendar:
    """
    Attributes:
        domain_id (int):
        id (int):
        additional_id (int):
        domain_type (WebsiteDataCalendarDomainType):
        domain_data (WebsiteDataCalendarDomainData | Unset):
    """

    domain_id: int
    id: int
    additional_id: int
    domain_type: WebsiteDataCalendarDomainType
    domain_data: WebsiteDataCalendarDomainData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_id = self.domain_id

        id = self.id

        additional_id = self.additional_id

        domain_type = self.domain_type.value

        domain_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain_data, Unset):
            domain_data = self.domain_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainId": domain_id,
                "id": id,
                "additionalId": additional_id,
                "domainType": domain_type,
            }
        )
        if domain_data is not UNSET:
            field_dict["domainData"] = domain_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.website_data_calendar_domain_data import (
            WebsiteDataCalendarDomainData,
        )

        d = dict(src_dict)
        domain_id = d.pop("domainId")

        id = d.pop("id")

        additional_id = d.pop("additionalId")

        domain_type = WebsiteDataCalendarDomainType(d.pop("domainType"))

        _domain_data = d.pop("domainData", UNSET)
        domain_data: WebsiteDataCalendarDomainData | Unset
        if isinstance(_domain_data, Unset):
            domain_data = UNSET
        else:
            domain_data = WebsiteDataCalendarDomainData.from_dict(_domain_data)

        website_data_calendar = cls(
            domain_id=domain_id,
            id=id,
            additional_id=additional_id,
            domain_type=domain_type,
            domain_data=domain_data,
        )

        website_data_calendar.additional_properties = d
        return website_data_calendar

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
