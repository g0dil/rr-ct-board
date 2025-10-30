from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_member_export_config_version import GroupMemberExportConfigVersion

if TYPE_CHECKING:
    from ..models.group_member_export_config_pinned_item import (
        GroupMemberExportConfigPinnedItem,
    )
    from ..models.group_member_export_config_unpinned_item import (
        GroupMemberExportConfigUnpinnedItem,
    )


T = TypeVar("T", bound="GroupMemberExportConfig")


@_attrs_define
class GroupMemberExportConfig:
    """
    Example:
        {'pinned': [{'key': 'person.name'}], 'unpinned': [{'key': 'person.email'}], 'version': 10}

    Attributes:
        pinned (list[GroupMemberExportConfigPinnedItem]):
        unpinned (list[GroupMemberExportConfigUnpinnedItem]):
        version (GroupMemberExportConfigVersion):
    """

    pinned: list[GroupMemberExportConfigPinnedItem]
    unpinned: list[GroupMemberExportConfigUnpinnedItem]
    version: GroupMemberExportConfigVersion
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
        from ..models.group_member_export_config_pinned_item import (
            GroupMemberExportConfigPinnedItem,
        )
        from ..models.group_member_export_config_unpinned_item import (
            GroupMemberExportConfigUnpinnedItem,
        )

        d = dict(src_dict)
        pinned = []
        _pinned = d.pop("pinned")
        for pinned_item_data in _pinned:
            pinned_item = GroupMemberExportConfigPinnedItem.from_dict(pinned_item_data)

            pinned.append(pinned_item)

        unpinned = []
        _unpinned = d.pop("unpinned")
        for unpinned_item_data in _unpinned:
            unpinned_item = GroupMemberExportConfigUnpinnedItem.from_dict(
                unpinned_item_data
            )

            unpinned.append(unpinned_item)

        version = GroupMemberExportConfigVersion(d.pop("version"))

        group_member_export_config = cls(
            pinned=pinned,
            unpinned=unpinned,
            version=version,
        )

        group_member_export_config.additional_properties = d
        return group_member_export_config

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
