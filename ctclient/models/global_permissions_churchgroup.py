from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GlobalPermissionsChurchgroup")


@_attrs_define
class GlobalPermissionsChurchgroup:
    """
    Attributes:
        administer_global_views (bool):
        administer_groups (bool):
        create_groups_of_grouptype (list[float]):
        delete_group (list[float]):
        delete_groups_of_grouptype (list[float]):
        edit_group (list[float]):
        edit_group_memberships_of_group (list[float]):
        edit_group_memberships_of_grouptype (list[float]):
        edit_groups_of_grouptype (list[float]):
        edit_masterdata (bool):
        security_level_group (list[float]):
        view (bool):
        view_group (list[float]):
        view_group_history (bool):
        view_group_tags (bool):
        view_groups_of_grouptype (list[float]):
    """

    administer_global_views: bool
    administer_groups: bool
    create_groups_of_grouptype: list[float]
    delete_group: list[float]
    delete_groups_of_grouptype: list[float]
    edit_group: list[float]
    edit_group_memberships_of_group: list[float]
    edit_group_memberships_of_grouptype: list[float]
    edit_groups_of_grouptype: list[float]
    edit_masterdata: bool
    security_level_group: list[float]
    view: bool
    view_group: list[float]
    view_group_history: bool
    view_group_tags: bool
    view_groups_of_grouptype: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        administer_global_views = self.administer_global_views

        administer_groups = self.administer_groups

        create_groups_of_grouptype = self.create_groups_of_grouptype

        delete_group = self.delete_group

        delete_groups_of_grouptype = self.delete_groups_of_grouptype

        edit_group = self.edit_group

        edit_group_memberships_of_group = self.edit_group_memberships_of_group

        edit_group_memberships_of_grouptype = self.edit_group_memberships_of_grouptype

        edit_groups_of_grouptype = self.edit_groups_of_grouptype

        edit_masterdata = self.edit_masterdata

        security_level_group = self.security_level_group

        view = self.view

        view_group = self.view_group

        view_group_history = self.view_group_history

        view_group_tags = self.view_group_tags

        view_groups_of_grouptype = self.view_groups_of_grouptype

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "administer global views": administer_global_views,
                "administer groups": administer_groups,
                "create groups of grouptype": create_groups_of_grouptype,
                "delete group": delete_group,
                "delete groups of grouptype": delete_groups_of_grouptype,
                "edit group": edit_group,
                "edit group memberships of group": edit_group_memberships_of_group,
                "edit group memberships of grouptype": edit_group_memberships_of_grouptype,
                "edit groups of grouptype": edit_groups_of_grouptype,
                "edit masterdata": edit_masterdata,
                "security level group": security_level_group,
                "view": view,
                "view group": view_group,
                "view group history": view_group_history,
                "view group tags": view_group_tags,
                "view groups of grouptype": view_groups_of_grouptype,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        administer_global_views = d.pop("administer global views")

        administer_groups = d.pop("administer groups")

        create_groups_of_grouptype = cast(
            list[float], d.pop("create groups of grouptype")
        )

        delete_group = cast(list[float], d.pop("delete group"))

        delete_groups_of_grouptype = cast(
            list[float], d.pop("delete groups of grouptype")
        )

        edit_group = cast(list[float], d.pop("edit group"))

        edit_group_memberships_of_group = cast(
            list[float], d.pop("edit group memberships of group")
        )

        edit_group_memberships_of_grouptype = cast(
            list[float], d.pop("edit group memberships of grouptype")
        )

        edit_groups_of_grouptype = cast(list[float], d.pop("edit groups of grouptype"))

        edit_masterdata = d.pop("edit masterdata")

        security_level_group = cast(list[float], d.pop("security level group"))

        view = d.pop("view")

        view_group = cast(list[float], d.pop("view group"))

        view_group_history = d.pop("view group history")

        view_group_tags = d.pop("view group tags")

        view_groups_of_grouptype = cast(list[float], d.pop("view groups of grouptype"))

        global_permissions_churchgroup = cls(
            administer_global_views=administer_global_views,
            administer_groups=administer_groups,
            create_groups_of_grouptype=create_groups_of_grouptype,
            delete_group=delete_group,
            delete_groups_of_grouptype=delete_groups_of_grouptype,
            edit_group=edit_group,
            edit_group_memberships_of_group=edit_group_memberships_of_group,
            edit_group_memberships_of_grouptype=edit_group_memberships_of_grouptype,
            edit_groups_of_grouptype=edit_groups_of_grouptype,
            edit_masterdata=edit_masterdata,
            security_level_group=security_level_group,
            view=view,
            view_group=view_group,
            view_group_history=view_group_history,
            view_group_tags=view_group_tags,
            view_groups_of_grouptype=view_groups_of_grouptype,
        )

        global_permissions_churchgroup.additional_properties = d
        return global_permissions_churchgroup

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
