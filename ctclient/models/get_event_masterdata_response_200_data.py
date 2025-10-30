from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_event_masterdata_response_200_data_absence_reasons_item import (
        GetEventMasterdataResponse200DataAbsenceReasonsItem,
    )
    from ..models.get_event_masterdata_response_200_data_facts_item import (
        GetEventMasterdataResponse200DataFactsItem,
    )
    from ..models.get_event_masterdata_response_200_data_service_groups_item import (
        GetEventMasterdataResponse200DataServiceGroupsItem,
    )
    from ..models.get_event_masterdata_response_200_data_services_item import (
        GetEventMasterdataResponse200DataServicesItem,
    )
    from ..models.get_event_masterdata_response_200_data_song_category import (
        GetEventMasterdataResponse200DataSongCategory,
    )
    from ..models.get_event_masterdata_response_200_data_song_source import (
        GetEventMasterdataResponse200DataSongSource,
    )


T = TypeVar("T", bound="GetEventMasterdataResponse200Data")


@_attrs_define
class GetEventMasterdataResponse200Data:
    """
    Attributes:
        absence_reasons (list[GetEventMasterdataResponse200DataAbsenceReasonsItem] | Unset):
        facts (list[GetEventMasterdataResponse200DataFactsItem] | Unset):
        service_groups (list[GetEventMasterdataResponse200DataServiceGroupsItem] | Unset):
        services (list[GetEventMasterdataResponse200DataServicesItem] | Unset):
        song_categories (list[GetEventMasterdataResponse200DataSongCategory] | Unset):
        song_sources (list[GetEventMasterdataResponse200DataSongSource] | Unset):
    """

    absence_reasons: (
        list[GetEventMasterdataResponse200DataAbsenceReasonsItem] | Unset
    ) = UNSET
    facts: list[GetEventMasterdataResponse200DataFactsItem] | Unset = UNSET
    service_groups: list[GetEventMasterdataResponse200DataServiceGroupsItem] | Unset = (
        UNSET
    )
    services: list[GetEventMasterdataResponse200DataServicesItem] | Unset = UNSET
    song_categories: list[GetEventMasterdataResponse200DataSongCategory] | Unset = UNSET
    song_sources: list[GetEventMasterdataResponse200DataSongSource] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        absence_reasons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.absence_reasons, Unset):
            absence_reasons = []
            for absence_reasons_item_data in self.absence_reasons:
                absence_reasons_item = absence_reasons_item_data.to_dict()
                absence_reasons.append(absence_reasons_item)

        facts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.facts, Unset):
            facts = []
            for facts_item_data in self.facts:
                facts_item = facts_item_data.to_dict()
                facts.append(facts_item)

        service_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service_groups, Unset):
            service_groups = []
            for service_groups_item_data in self.service_groups:
                service_groups_item = service_groups_item_data.to_dict()
                service_groups.append(service_groups_item)

        services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        song_categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.song_categories, Unset):
            song_categories = []
            for song_categories_item_data in self.song_categories:
                song_categories_item = song_categories_item_data.to_dict()
                song_categories.append(song_categories_item)

        song_sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.song_sources, Unset):
            song_sources = []
            for song_sources_item_data in self.song_sources:
                song_sources_item = song_sources_item_data.to_dict()
                song_sources.append(song_sources_item)

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
        from ..models.get_event_masterdata_response_200_data_absence_reasons_item import (
            GetEventMasterdataResponse200DataAbsenceReasonsItem,
        )
        from ..models.get_event_masterdata_response_200_data_facts_item import (
            GetEventMasterdataResponse200DataFactsItem,
        )
        from ..models.get_event_masterdata_response_200_data_service_groups_item import (
            GetEventMasterdataResponse200DataServiceGroupsItem,
        )
        from ..models.get_event_masterdata_response_200_data_services_item import (
            GetEventMasterdataResponse200DataServicesItem,
        )
        from ..models.get_event_masterdata_response_200_data_song_category import (
            GetEventMasterdataResponse200DataSongCategory,
        )
        from ..models.get_event_masterdata_response_200_data_song_source import (
            GetEventMasterdataResponse200DataSongSource,
        )

        d = dict(src_dict)
        absence_reasons = []
        _absence_reasons = d.pop("absenceReasons", UNSET)
        for absence_reasons_item_data in _absence_reasons or []:
            absence_reasons_item = (
                GetEventMasterdataResponse200DataAbsenceReasonsItem.from_dict(
                    absence_reasons_item_data
                )
            )

            absence_reasons.append(absence_reasons_item)

        facts = []
        _facts = d.pop("facts", UNSET)
        for facts_item_data in _facts or []:
            facts_item = GetEventMasterdataResponse200DataFactsItem.from_dict(
                facts_item_data
            )

            facts.append(facts_item)

        service_groups = []
        _service_groups = d.pop("serviceGroups", UNSET)
        for service_groups_item_data in _service_groups or []:
            service_groups_item = (
                GetEventMasterdataResponse200DataServiceGroupsItem.from_dict(
                    service_groups_item_data
                )
            )

            service_groups.append(service_groups_item)

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = GetEventMasterdataResponse200DataServicesItem.from_dict(
                services_item_data
            )

            services.append(services_item)

        song_categories = []
        _song_categories = d.pop("songCategories", UNSET)
        for song_categories_item_data in _song_categories or []:
            song_categories_item = (
                GetEventMasterdataResponse200DataSongCategory.from_dict(
                    song_categories_item_data
                )
            )

            song_categories.append(song_categories_item)

        song_sources = []
        _song_sources = d.pop("songSources", UNSET)
        for song_sources_item_data in _song_sources or []:
            song_sources_item = GetEventMasterdataResponse200DataSongSource.from_dict(
                song_sources_item_data
            )

            song_sources.append(song_sources_item)

        get_event_masterdata_response_200_data = cls(
            absence_reasons=absence_reasons,
            facts=facts,
            service_groups=service_groups,
            services=services,
            song_categories=song_categories,
            song_sources=song_sources,
        )

        get_event_masterdata_response_200_data.additional_properties = d
        return get_event_masterdata_response_200_data

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
