from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_groups_group_id_groupstatus_body_role_mapping import (
        PostGroupsGroupIdGroupstatusBodyRoleMapping,
    )


T = TypeVar("T", bound="PostGroupsGroupIdGroupstatusBody")


@_attrs_define
class PostGroupsGroupIdGroupstatusBody:
    """
    Attributes:
        group_type_id (int | Unset):
        role_mapping (PostGroupsGroupIdGroupstatusBodyRoleMapping | Unset):
    """

    group_type_id: int | Unset = UNSET
    role_mapping: PostGroupsGroupIdGroupstatusBodyRoleMapping | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_type_id = self.group_type_id

        role_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role_mapping, Unset):
            role_mapping = self.role_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_type_id is not UNSET:
            field_dict["groupTypeId"] = group_type_id
        if role_mapping is not UNSET:
            field_dict["roleMapping"] = role_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_groups_group_id_groupstatus_body_role_mapping import (
            PostGroupsGroupIdGroupstatusBodyRoleMapping,
        )

        d = dict(src_dict)
        group_type_id = d.pop("groupTypeId", UNSET)

        _role_mapping = d.pop("roleMapping", UNSET)
        role_mapping: PostGroupsGroupIdGroupstatusBodyRoleMapping | Unset
        if isinstance(_role_mapping, Unset):
            role_mapping = UNSET
        else:
            role_mapping = PostGroupsGroupIdGroupstatusBodyRoleMapping.from_dict(
                _role_mapping
            )

        post_groups_group_id_groupstatus_body = cls(
            group_type_id=group_type_id,
            role_mapping=role_mapping,
        )

        post_groups_group_id_groupstatus_body.additional_properties = d
        return post_groups_group_id_groupstatus_body

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
