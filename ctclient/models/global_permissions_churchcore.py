from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalPermissionsChurchcore")


@_attrs_define
class GlobalPermissionsChurchcore:
    """
    Attributes:
        administer_church_html_templates (bool):
        administer_persons (bool):
        administer_settings (bool):
        edit_languages (list[float]):
        edit_public_profiles (bool):
        edit_translations_masterdata (bool):
        edit_website_releases (bool):
        edit_website_staff (bool):
        invite_persons (bool):
        login_to_external_system (list[float]):
        simulate_persons (bool):
        use_church_html_templates (list[float]):
        view_logfile (bool):
        view_website (bool):
        administer_custom_modules (bool | Unset):
        use_churchquery (bool | Unset):
    """

    administer_church_html_templates: bool
    administer_persons: bool
    administer_settings: bool
    edit_languages: list[float]
    edit_public_profiles: bool
    edit_translations_masterdata: bool
    edit_website_releases: bool
    edit_website_staff: bool
    invite_persons: bool
    login_to_external_system: list[float]
    simulate_persons: bool
    use_church_html_templates: list[float]
    view_logfile: bool
    view_website: bool
    administer_custom_modules: bool | Unset = UNSET
    use_churchquery: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        administer_church_html_templates = self.administer_church_html_templates

        administer_persons = self.administer_persons

        administer_settings = self.administer_settings

        edit_languages = self.edit_languages

        edit_public_profiles = self.edit_public_profiles

        edit_translations_masterdata = self.edit_translations_masterdata

        edit_website_releases = self.edit_website_releases

        edit_website_staff = self.edit_website_staff

        invite_persons = self.invite_persons

        login_to_external_system = self.login_to_external_system

        simulate_persons = self.simulate_persons

        use_church_html_templates = self.use_church_html_templates

        view_logfile = self.view_logfile

        view_website = self.view_website

        administer_custom_modules = self.administer_custom_modules

        use_churchquery = self.use_churchquery

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "administer church html templates": administer_church_html_templates,
                "administer persons": administer_persons,
                "administer settings": administer_settings,
                "edit languages": edit_languages,
                "edit public profiles": edit_public_profiles,
                "edit translations masterdata": edit_translations_masterdata,
                "edit website releases": edit_website_releases,
                "edit website staff": edit_website_staff,
                "invite persons": invite_persons,
                "login to external system": login_to_external_system,
                "simulate persons": simulate_persons,
                "use church html templates": use_church_html_templates,
                "view logfile": view_logfile,
                "view website": view_website,
            }
        )
        if administer_custom_modules is not UNSET:
            field_dict["administer custom modules"] = administer_custom_modules
        if use_churchquery is not UNSET:
            field_dict["use churchquery"] = use_churchquery

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        administer_church_html_templates = d.pop("administer church html templates")

        administer_persons = d.pop("administer persons")

        administer_settings = d.pop("administer settings")

        edit_languages = cast(list[float], d.pop("edit languages"))

        edit_public_profiles = d.pop("edit public profiles")

        edit_translations_masterdata = d.pop("edit translations masterdata")

        edit_website_releases = d.pop("edit website releases")

        edit_website_staff = d.pop("edit website staff")

        invite_persons = d.pop("invite persons")

        login_to_external_system = cast(list[float], d.pop("login to external system"))

        simulate_persons = d.pop("simulate persons")

        use_church_html_templates = cast(
            list[float], d.pop("use church html templates")
        )

        view_logfile = d.pop("view logfile")

        view_website = d.pop("view website")

        administer_custom_modules = d.pop("administer custom modules", UNSET)

        use_churchquery = d.pop("use churchquery", UNSET)

        global_permissions_churchcore = cls(
            administer_church_html_templates=administer_church_html_templates,
            administer_persons=administer_persons,
            administer_settings=administer_settings,
            edit_languages=edit_languages,
            edit_public_profiles=edit_public_profiles,
            edit_translations_masterdata=edit_translations_masterdata,
            edit_website_releases=edit_website_releases,
            edit_website_staff=edit_website_staff,
            invite_persons=invite_persons,
            login_to_external_system=login_to_external_system,
            simulate_persons=simulate_persons,
            use_church_html_templates=use_church_html_templates,
            view_logfile=view_logfile,
            view_website=view_website,
            administer_custom_modules=administer_custom_modules,
            use_churchquery=use_churchquery,
        )

        global_permissions_churchcore.additional_properties = d
        return global_permissions_churchcore

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
