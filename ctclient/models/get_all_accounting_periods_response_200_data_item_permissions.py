from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAllAccountingPeriodsResponse200DataItemPermissions")


@_attrs_define
class GetAllAccountingPeriodsResponse200DataItemPermissions:
    """
    Attributes:
        can_use_expert_mode (bool): Flag if current user can make changes in this accounting periods, like filing new
            transactions and expert mode is enabled.
        edit_accounting_period (bool): Flag if current user can edit this accounting period, like changing the name.
    """

    can_use_expert_mode: bool
    edit_accounting_period: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_use_expert_mode = self.can_use_expert_mode

        edit_accounting_period = self.edit_accounting_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canUseExpertMode": can_use_expert_mode,
                "edit accounting period": edit_accounting_period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_use_expert_mode = d.pop("canUseExpertMode")

        edit_accounting_period = d.pop("edit accounting period")

        get_all_accounting_periods_response_200_data_item_permissions = cls(
            can_use_expert_mode=can_use_expert_mode,
            edit_accounting_period=edit_accounting_period,
        )

        get_all_accounting_periods_response_200_data_item_permissions.additional_properties = d
        return get_all_accounting_periods_response_200_data_item_permissions

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
