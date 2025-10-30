from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGlobalPermissionsResponse200DataChurchreport")


@_attrs_define
class GetGlobalPermissionsResponse200DataChurchreport:
    """
    Attributes:
        edit_masterdata (bool):
        view (bool):
        view_query (list[float]):
    """

    edit_masterdata: bool
    view: bool
    view_query: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edit_masterdata = self.edit_masterdata

        view = self.view

        view_query = self.view_query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edit masterdata": edit_masterdata,
                "view": view,
                "view query": view_query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        edit_masterdata = d.pop("edit masterdata")

        view = d.pop("view")

        view_query = cast(list[float], d.pop("view query"))

        get_global_permissions_response_200_data_churchreport = cls(
            edit_masterdata=edit_masterdata,
            view=view,
            view_query=view_query,
        )

        get_global_permissions_response_200_data_churchreport.additional_properties = d
        return get_global_permissions_response_200_data_churchreport

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
