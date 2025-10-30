from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_resource_masterdata_response_200_data_resource_types_item import (
        GetResourceMasterdataResponse200DataResourceTypesItem,
    )
    from ..models.get_resource_masterdata_response_200_data_resources_item import (
        GetResourceMasterdataResponse200DataResourcesItem,
    )


T = TypeVar("T", bound="GetResourceMasterdataResponse200Data")


@_attrs_define
class GetResourceMasterdataResponse200Data:
    """
    Attributes:
        resource_types (list[GetResourceMasterdataResponse200DataResourceTypesItem] | Unset):
        resources (list[GetResourceMasterdataResponse200DataResourcesItem] | Unset):
    """

    resource_types: (
        list[GetResourceMasterdataResponse200DataResourceTypesItem] | Unset
    ) = UNSET
    resources: list[GetResourceMasterdataResponse200DataResourcesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resource_types, Unset):
            resource_types = []
            for resource_types_item_data in self.resource_types:
                resource_types_item = resource_types_item_data.to_dict()
                resource_types.append(resource_types_item)

        resources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()
                resources.append(resources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_types is not UNSET:
            field_dict["resourceTypes"] = resource_types
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_resource_masterdata_response_200_data_resource_types_item import (
            GetResourceMasterdataResponse200DataResourceTypesItem,
        )
        from ..models.get_resource_masterdata_response_200_data_resources_item import (
            GetResourceMasterdataResponse200DataResourcesItem,
        )

        d = dict(src_dict)
        resource_types = []
        _resource_types = d.pop("resourceTypes", UNSET)
        for resource_types_item_data in _resource_types or []:
            resource_types_item = (
                GetResourceMasterdataResponse200DataResourceTypesItem.from_dict(
                    resource_types_item_data
                )
            )

            resource_types.append(resource_types_item)

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = (
                GetResourceMasterdataResponse200DataResourcesItem.from_dict(
                    resources_item_data
                )
            )

            resources.append(resources_item)

        get_resource_masterdata_response_200_data = cls(
            resource_types=resource_types,
            resources=resources,
        )

        get_resource_masterdata_response_200_data.additional_properties = d
        return get_resource_masterdata_response_200_data

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
