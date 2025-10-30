from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_groups_group_id_members_export_config_body_config_version import (
    GetGroupsGroupIdMembersExportConfigBodyConfigVersion,
)

if TYPE_CHECKING:
    from ..models.get_groups_group_id_members_export_config_body_config_pinned_item import (
        GetGroupsGroupIdMembersExportConfigBodyConfigPinnedItem,
    )
    from ..models.get_groups_group_id_members_export_config_body_config_unpinned_item import (
        GetGroupsGroupIdMembersExportConfigBodyConfigUnpinnedItem,
    )


T = TypeVar("T", bound="GetGroupsGroupIdMembersExportConfigBodyConfig")


@_attrs_define
class GetGroupsGroupIdMembersExportConfigBodyConfig:
    """
    Example:
        {'pinned': [{'key': 'person.name'}], 'unpinned': [{'key': 'person.email'}], 'version': 10}

    Attributes:
        pinned (list[GetGroupsGroupIdMembersExportConfigBodyConfigPinnedItem]):
        unpinned (list[GetGroupsGroupIdMembersExportConfigBodyConfigUnpinnedItem]):
        version (GetGroupsGroupIdMembersExportConfigBodyConfigVersion):
    """

    pinned: list[GetGroupsGroupIdMembersExportConfigBodyConfigPinnedItem]
    unpinned: list[GetGroupsGroupIdMembersExportConfigBodyConfigUnpinnedItem]
    version: GetGroupsGroupIdMembersExportConfigBodyConfigVersion
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pinned = []
        for pinned_item_data in self.pinned:
            pinned_item = pinned_item_data.to_dict()
            pinned.append(pinned_item)

        unpinned = []
        for unpinned_item_data in self.unpinned:
            unpinned_item = unpinned_item_data.to_dict()
            unpinned.append(unpinned_item)

        version = self.version.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pinned": pinned,
                "unpinned": unpinned,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_groups_group_id_members_export_config_body_config_pinned_item import (
            GetGroupsGroupIdMembersExportConfigBodyConfigPinnedItem,
        )
        from ..models.get_groups_group_id_members_export_config_body_config_unpinned_item import (
            GetGroupsGroupIdMembersExportConfigBodyConfigUnpinnedItem,
        )

        d = dict(src_dict)
        pinned = []
        _pinned = d.pop("pinned")
        for pinned_item_data in _pinned:
            pinned_item = (
                GetGroupsGroupIdMembersExportConfigBodyConfigPinnedItem.from_dict(
                    pinned_item_data
                )
            )

            pinned.append(pinned_item)

        unpinned = []
        _unpinned = d.pop("unpinned")
        for unpinned_item_data in _unpinned:
            unpinned_item = (
                GetGroupsGroupIdMembersExportConfigBodyConfigUnpinnedItem.from_dict(
                    unpinned_item_data
                )
            )

            unpinned.append(unpinned_item)

        version = GetGroupsGroupIdMembersExportConfigBodyConfigVersion(d.pop("version"))

        get_groups_group_id_members_export_config_body_config = cls(
            pinned=pinned,
            unpinned=unpinned,
            version=version,
        )

        get_groups_group_id_members_export_config_body_config.additional_properties = d
        return get_groups_group_id_members_export_config_body_config

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
