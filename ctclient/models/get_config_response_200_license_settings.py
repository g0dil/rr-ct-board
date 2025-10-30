from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_config_response_200_license_settings_hide_licensetab import (
    GetConfigResponse200LicenseSettingsHideLicensetab,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetConfigResponse200LicenseSettings")


@_attrs_define
class GetConfigResponse200LicenseSettings:
    """
    Attributes:
        hide_licensetab (GetConfigResponse200LicenseSettingsHideLicensetab | Unset):
    """

    hide_licensetab: GetConfigResponse200LicenseSettingsHideLicensetab | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hide_licensetab: str | Unset = UNSET
        if not isinstance(self.hide_licensetab, Unset):
            hide_licensetab = self.hide_licensetab.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hide_licensetab is not UNSET:
            field_dict["hide_licensetab"] = hide_licensetab

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _hide_licensetab = d.pop("hide_licensetab", UNSET)
        hide_licensetab: GetConfigResponse200LicenseSettingsHideLicensetab | Unset
        if isinstance(_hide_licensetab, Unset):
            hide_licensetab = UNSET
        else:
            hide_licensetab = GetConfigResponse200LicenseSettingsHideLicensetab(
                _hide_licensetab
            )

        get_config_response_200_license_settings = cls(
            hide_licensetab=hide_licensetab,
        )

        get_config_response_200_license_settings.additional_properties = d
        return get_config_response_200_license_settings

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
