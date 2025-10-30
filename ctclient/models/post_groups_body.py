from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_groups_body_visibility import PostGroupsBodyVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostGroupsBody")


@_attrs_define
class PostGroupsBody:
    """
    Attributes:
        group_status_id (int): ID of group status
        group_type_id (int): Id of group type
        name (str): Group name
        campus_id (int | Unset): Campus Id if group is connected to a campus
        force (bool | Unset): Need to be true, if another group with that name already exists
        group_category_id (int | Unset): ID of group category
        parent_group_id (int | Unset): Group ID of parent group
        role_id (int | Unset): put yourself in this role
        visibility (PostGroupsBodyVisibility | Unset): The visibility of a group.
    """

    group_status_id: int
    group_type_id: int
    name: str
    campus_id: int | Unset = UNSET
    force: bool | Unset = UNSET
    group_category_id: int | Unset = UNSET
    parent_group_id: int | Unset = UNSET
    role_id: int | Unset = UNSET
    visibility: PostGroupsBodyVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_status_id = self.group_status_id

        group_type_id = self.group_type_id

        name = self.name

        campus_id = self.campus_id

        force = self.force

        group_category_id = self.group_category_id

        parent_group_id = self.parent_group_id

        role_id = self.role_id

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groupStatusId": group_status_id,
                "groupTypeId": group_type_id,
                "name": name,
            }
        )
        if campus_id is not UNSET:
            field_dict["campusId"] = campus_id
        if force is not UNSET:
            field_dict["force"] = force
        if group_category_id is not UNSET:
            field_dict["groupCategoryId"] = group_category_id
        if parent_group_id is not UNSET:
            field_dict["parentGroupId"] = parent_group_id
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_status_id = d.pop("groupStatusId")

        group_type_id = d.pop("groupTypeId")

        name = d.pop("name")

        campus_id = d.pop("campusId", UNSET)

        force = d.pop("force", UNSET)

        group_category_id = d.pop("groupCategoryId", UNSET)

        parent_group_id = d.pop("parentGroupId", UNSET)

        role_id = d.pop("roleId", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: PostGroupsBodyVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = PostGroupsBodyVisibility(_visibility)

        post_groups_body = cls(
            group_status_id=group_status_id,
            group_type_id=group_type_id,
            name=name,
            campus_id=campus_id,
            force=force,
            group_category_id=group_category_id,
            parent_group_id=parent_group_id,
            role_id=role_id,
            visibility=visibility,
        )

        post_groups_body.additional_properties = d
        return post_groups_body

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
