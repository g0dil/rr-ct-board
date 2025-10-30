from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetEventMasterdataResponse200Meta")


@_attrs_define
class GetEventMasterdataResponse200Meta:
    """
    Attributes:
        absence_reasons (int | Unset):
        facts (int | Unset):
        service_groups (int | Unset):
        services (int | Unset):
        song_categories (int | Unset):
        song_sources (int | Unset):
    """

    absence_reasons: int | Unset = UNSET
    facts: int | Unset = UNSET
    service_groups: int | Unset = UNSET
    services: int | Unset = UNSET
    song_categories: int | Unset = UNSET
    song_sources: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        absence_reasons = self.absence_reasons

        facts = self.facts

        service_groups = self.service_groups

        services = self.services

        song_categories = self.song_categories

        song_sources = self.song_sources

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if absence_reasons is not UNSET:
            field_dict["absenceReasons"] = absence_reasons
        if facts is not UNSET:
            field_dict["facts"] = facts
        if service_groups is not UNSET:
            field_dict["serviceGroups"] = service_groups
        if services is not UNSET:
            field_dict["services"] = services
        if song_categories is not UNSET:
            field_dict["songCategories"] = song_categories
        if song_sources is not UNSET:
            field_dict["songSources"] = song_sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        absence_reasons = d.pop("absenceReasons", UNSET)

        facts = d.pop("facts", UNSET)

        service_groups = d.pop("serviceGroups", UNSET)

        services = d.pop("services", UNSET)

        song_categories = d.pop("songCategories", UNSET)

        song_sources = d.pop("songSources", UNSET)

        get_event_masterdata_response_200_meta = cls(
            absence_reasons=absence_reasons,
            facts=facts,
            service_groups=service_groups,
            services=services,
            song_categories=song_categories,
            song_sources=song_sources,
        )

        get_event_masterdata_response_200_meta.additional_properties = d
        return get_event_masterdata_response_200_meta

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
