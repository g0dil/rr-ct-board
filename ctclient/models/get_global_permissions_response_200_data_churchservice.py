from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGlobalPermissionsResponse200DataChurchservice")


@_attrs_define
class GetGlobalPermissionsResponse200DataChurchservice:
    """
    Attributes:
        edit_agenda (list[float]):
        edit_agenda_templates (list[float]):
        edit_events (list[float]):
        edit_fact (list[float]):
        edit_masterdata (bool):
        edit_servicegroup (list[float]):
        edit_songcategory (list[float]):
        edit_template (bool):
        export_facts (bool):
        manage_absent (bool):
        use_ccli (bool):
        view (bool):
        view_agenda (list[float]):
        view_events (list[float]):
        view_fact (list[float]):
        view_history (bool):
        view_servicegroup (list[float]):
        view_song_statistics (bool):
        view_songcategory (list[float]):
    """

    edit_agenda: list[float]
    edit_agenda_templates: list[float]
    edit_events: list[float]
    edit_fact: list[float]
    edit_masterdata: bool
    edit_servicegroup: list[float]
    edit_songcategory: list[float]
    edit_template: bool
    export_facts: bool
    manage_absent: bool
    use_ccli: bool
    view: bool
    view_agenda: list[float]
    view_events: list[float]
    view_fact: list[float]
    view_history: bool
    view_servicegroup: list[float]
    view_song_statistics: bool
    view_songcategory: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edit_agenda = self.edit_agenda

        edit_agenda_templates = self.edit_agenda_templates

        edit_events = self.edit_events

        edit_fact = self.edit_fact

        edit_masterdata = self.edit_masterdata

        edit_servicegroup = self.edit_servicegroup

        edit_songcategory = self.edit_songcategory

        edit_template = self.edit_template

        export_facts = self.export_facts

        manage_absent = self.manage_absent

        use_ccli = self.use_ccli

        view = self.view

        view_agenda = self.view_agenda

        view_events = self.view_events

        view_fact = self.view_fact

        view_history = self.view_history

        view_servicegroup = self.view_servicegroup

        view_song_statistics = self.view_song_statistics

        view_songcategory = self.view_songcategory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edit agenda": edit_agenda,
                "edit agenda templates": edit_agenda_templates,
                "edit events": edit_events,
                "edit fact": edit_fact,
                "edit masterdata": edit_masterdata,
                "edit servicegroup": edit_servicegroup,
                "edit songcategory": edit_songcategory,
                "edit template": edit_template,
                "export facts": export_facts,
                "manage absent": manage_absent,
                "use ccli": use_ccli,
                "view": view,
                "view agenda": view_agenda,
                "view events": view_events,
                "view fact": view_fact,
                "view history": view_history,
                "view servicegroup": view_servicegroup,
                "view song statistics": view_song_statistics,
                "view songcategory": view_songcategory,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        edit_agenda = cast(list[float], d.pop("edit agenda"))

        edit_agenda_templates = cast(list[float], d.pop("edit agenda templates"))

        edit_events = cast(list[float], d.pop("edit events"))

        edit_fact = cast(list[float], d.pop("edit fact"))

        edit_masterdata = d.pop("edit masterdata")

        edit_servicegroup = cast(list[float], d.pop("edit servicegroup"))

        edit_songcategory = cast(list[float], d.pop("edit songcategory"))

        edit_template = d.pop("edit template")

        export_facts = d.pop("export facts")

        manage_absent = d.pop("manage absent")

        use_ccli = d.pop("use ccli")

        view = d.pop("view")

        view_agenda = cast(list[float], d.pop("view agenda"))

        view_events = cast(list[float], d.pop("view events"))

        view_fact = cast(list[float], d.pop("view fact"))

        view_history = d.pop("view history")

        view_servicegroup = cast(list[float], d.pop("view servicegroup"))

        view_song_statistics = d.pop("view song statistics")

        view_songcategory = cast(list[float], d.pop("view songcategory"))

        get_global_permissions_response_200_data_churchservice = cls(
            edit_agenda=edit_agenda,
            edit_agenda_templates=edit_agenda_templates,
            edit_events=edit_events,
            edit_fact=edit_fact,
            edit_masterdata=edit_masterdata,
            edit_servicegroup=edit_servicegroup,
            edit_songcategory=edit_songcategory,
            edit_template=edit_template,
            export_facts=export_facts,
            manage_absent=manage_absent,
            use_ccli=use_ccli,
            view=view,
            view_agenda=view_agenda,
            view_events=view_events,
            view_fact=view_fact,
            view_history=view_history,
            view_servicegroup=view_servicegroup,
            view_song_statistics=view_song_statistics,
            view_songcategory=view_songcategory,
        )

        get_global_permissions_response_200_data_churchservice.additional_properties = d
        return get_global_permissions_response_200_data_churchservice

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
