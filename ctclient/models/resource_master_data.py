from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_master_data_resource_types_item import (
        ResourceMasterDataResourceTypesItem,
    )
    from ..models.resource_master_data_resources_item import (
        ResourceMasterDataResourcesItem,
    )


T = TypeVar("T", bound="ResourceMasterData")


@_attrs_define
class ResourceMasterData:
    """
    Attributes:
        resource_types (list[ResourceMasterDataResourceTypesItem] | Unset):
        resources (list[ResourceMasterDataResourcesItem] | Unset):
    """

    resource_types: list[ResourceMasterDataResourceTypesItem] | Unset = UNSET
    resources: list[ResourceMasterDataResourcesItem] | Unset = UNSET
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
        from ..models.resource_master_data_resource_types_item import (
            ResourceMasterDataResourceTypesItem,
        )
        from ..models.resource_master_data_resources_item import (
            ResourceMasterDataResourcesItem,
        )

        d = dict(src_dict)
        resource_types = []
        _resource_types = d.pop("resourceTypes", UNSET)
        for resource_types_item_data in _resource_types or []:
            resource_types_item = ResourceMasterDataResourceTypesItem.from_dict(
                resource_types_item_data
            )

            resource_types.append(resource_types_item)

        resources = []
        _resources = d.pop("resources", UNSET)
        for resources_item_data in _resources or []:
            resources_item = ResourceMasterDataResourcesItem.from_dict(
                resources_item_data
            )

            resources.append(resources_item)

        resource_master_data = cls(
            resource_types=resource_types,
            resources=resources,
        )

        resource_master_data.additional_properties = d
        return resource_master_data

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
