from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPersonMasterdataResponse200Meta")


@_attrs_define
class GetPersonMasterdataResponse200Meta:
    """
    Attributes:
        age_groups (int | Unset):
        campuses (int | Unset):
        comment_viewers (int | Unset):
        contact_labels (int | Unset):
        departments (int | Unset):
        follow_up_intervals (int | Unset):
        follow_ups (int | Unset):
        group_categories (int | Unset):
        group_meeting_templates (int | Unset):
        group_statuses (int | Unset):
        group_types (int | Unset):
        grow_paths (int | Unset):
        roles (int | Unset):
        statuses (int | Unset):
        target_groups (int | Unset):
    """

    age_groups: int | Unset = UNSET
    campuses: int | Unset = UNSET
    comment_viewers: int | Unset = UNSET
    contact_labels: int | Unset = UNSET
    departments: int | Unset = UNSET
    follow_up_intervals: int | Unset = UNSET
    follow_ups: int | Unset = UNSET
    group_categories: int | Unset = UNSET
    group_meeting_templates: int | Unset = UNSET
    group_statuses: int | Unset = UNSET
    group_types: int | Unset = UNSET
    grow_paths: int | Unset = UNSET
    roles: int | Unset = UNSET
    statuses: int | Unset = UNSET
    target_groups: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        age_groups = self.age_groups

        campuses = self.campuses

        comment_viewers = self.comment_viewers

        contact_labels = self.contact_labels

        departments = self.departments

        follow_up_intervals = self.follow_up_intervals

        follow_ups = self.follow_ups

        group_categories = self.group_categories

        group_meeting_templates = self.group_meeting_templates

        group_statuses = self.group_statuses

        group_types = self.group_types

        grow_paths = self.grow_paths

        roles = self.roles

        statuses = self.statuses

        target_groups = self.target_groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if age_groups is not UNSET:
            field_dict["ageGroups"] = age_groups
        if campuses is not UNSET:
            field_dict["campuses"] = campuses
        if comment_viewers is not UNSET:
            field_dict["commentViewers"] = comment_viewers
        if contact_labels is not UNSET:
            field_dict["contactLabels"] = contact_labels
        if departments is not UNSET:
            field_dict["departments"] = departments
        if follow_up_intervals is not UNSET:
            field_dict["followUpIntervals"] = follow_up_intervals
        if follow_ups is not UNSET:
            field_dict["followUps"] = follow_ups
        if group_categories is not UNSET:
            field_dict["groupCategories"] = group_categories
        if group_meeting_templates is not UNSET:
            field_dict["groupMeetingTemplates"] = group_meeting_templates
        if group_statuses is not UNSET:
            field_dict["groupStatuses"] = group_statuses
        if group_types is not UNSET:
            field_dict["groupTypes"] = group_types
        if grow_paths is not UNSET:
            field_dict["growPaths"] = grow_paths
        if roles is not UNSET:
            field_dict["roles"] = roles
        if statuses is not UNSET:
            field_dict["statuses"] = statuses
        if target_groups is not UNSET:
            field_dict["targetGroups"] = target_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        age_groups = d.pop("ageGroups", UNSET)

        campuses = d.pop("campuses", UNSET)

        comment_viewers = d.pop("commentViewers", UNSET)

        contact_labels = d.pop("contactLabels", UNSET)

        departments = d.pop("departments", UNSET)

        follow_up_intervals = d.pop("followUpIntervals", UNSET)

        follow_ups = d.pop("followUps", UNSET)

        group_categories = d.pop("groupCategories", UNSET)

        group_meeting_templates = d.pop("groupMeetingTemplates", UNSET)

        group_statuses = d.pop("groupStatuses", UNSET)

        group_types = d.pop("groupTypes", UNSET)

        grow_paths = d.pop("growPaths", UNSET)

        roles = d.pop("roles", UNSET)

        statuses = d.pop("statuses", UNSET)

        target_groups = d.pop("targetGroups", UNSET)

        get_person_masterdata_response_200_meta = cls(
            age_groups=age_groups,
            campuses=campuses,
            comment_viewers=comment_viewers,
            contact_labels=contact_labels,
            departments=departments,
            follow_up_intervals=follow_up_intervals,
            follow_ups=follow_ups,
            group_categories=group_categories,
            group_meeting_templates=group_meeting_templates,
            group_statuses=group_statuses,
            group_types=group_types,
            grow_paths=grow_paths,
            roles=roles,
            statuses=statuses,
            target_groups=target_groups,
        )

        get_person_masterdata_response_200_meta.additional_properties = d
        return get_person_masterdata_response_200_meta

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
