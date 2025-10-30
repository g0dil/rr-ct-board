from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGlobalPermissionsResponse200DataFinance")


@_attrs_define
class GetGlobalPermissionsResponse200DataFinance:
    """
    Attributes:
        edit_accounting_period (list[float]):
        edit_masterdata (bool):
        view (bool):
        view_accounting_period (list[float]):
    """

    edit_accounting_period: list[float]
    edit_masterdata: bool
    view: bool
    view_accounting_period: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edit_accounting_period = self.edit_accounting_period

        edit_masterdata = self.edit_masterdata

        view = self.view

        view_accounting_period = self.view_accounting_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edit accounting period": edit_accounting_period,
                "edit masterdata": edit_masterdata,
                "view": view,
                "view accounting period": view_accounting_period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        edit_accounting_period = cast(list[float], d.pop("edit accounting period"))

        edit_masterdata = d.pop("edit masterdata")

        view = d.pop("view")

        view_accounting_period = cast(list[float], d.pop("view accounting period"))

        get_global_permissions_response_200_data_finance = cls(
            edit_accounting_period=edit_accounting_period,
            edit_masterdata=edit_masterdata,
            view=view,
            view_accounting_period=view_accounting_period,
        )

        get_global_permissions_response_200_data_finance.additional_properties = d
        return get_global_permissions_response_200_data_finance

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
