from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person_master_data_age_groups_item import (
        PersonMasterDataAgeGroupsItem,
    )
    from ..models.person_master_data_campuses_item import PersonMasterDataCampusesItem
    from ..models.person_master_data_comment_viewers_item import (
        PersonMasterDataCommentViewersItem,
    )
    from ..models.person_master_data_contact_labels_item import (
        PersonMasterDataContactLabelsItem,
    )
    from ..models.person_master_data_departments_item import (
        PersonMasterDataDepartmentsItem,
    )
    from ..models.person_master_data_follow_up_intervals_item import (
        PersonMasterDataFollowUpIntervalsItem,
    )
    from ..models.person_master_data_follow_ups_item import (
        PersonMasterDataFollowUpsItem,
    )
    from ..models.person_master_data_group_categories_item import (
        PersonMasterDataGroupCategoriesItem,
    )
    from ..models.person_master_data_group_meeting_templates_item import (
        PersonMasterDataGroupMeetingTemplatesItem,
    )
    from ..models.person_master_data_group_statuses_item import (
        PersonMasterDataGroupStatusesItem,
    )
    from ..models.person_master_data_group_types_item import (
        PersonMasterDataGroupTypesItem,
    )
    from ..models.person_master_data_grow_paths_item import (
        PersonMasterDataGrowPathsItem,
    )
    from ..models.person_master_data_relationship_types_item import (
        PersonMasterDataRelationshipTypesItem,
    )
    from ..models.person_master_data_roles_item import PersonMasterDataRolesItem
    from ..models.person_master_data_sexes_item import PersonMasterDataSexesItem
    from ..models.person_master_data_statuses_item import PersonMasterDataStatusesItem
    from ..models.person_master_data_target_groups_item import (
        PersonMasterDataTargetGroupsItem,
    )


T = TypeVar("T", bound="PersonMasterData")


@_attrs_define
class PersonMasterData:
    """
    Attributes:
        age_groups (list[PersonMasterDataAgeGroupsItem] | Unset):
        campuses (list[PersonMasterDataCampusesItem] | Unset):
        comment_viewers (list[PersonMasterDataCommentViewersItem] | Unset):
        contact_labels (list[PersonMasterDataContactLabelsItem] | Unset):
        departments (list[PersonMasterDataDepartmentsItem] | Unset):
        follow_up_intervals (list[PersonMasterDataFollowUpIntervalsItem] | Unset):
        follow_ups (list[PersonMasterDataFollowUpsItem] | Unset):
        group_categories (list[PersonMasterDataGroupCategoriesItem] | Unset):
        group_meeting_templates (list[PersonMasterDataGroupMeetingTemplatesItem] | Unset):
        group_statuses (list[PersonMasterDataGroupStatusesItem] | Unset):
        group_types (list[PersonMasterDataGroupTypesItem] | Unset):
        grow_paths (list[PersonMasterDataGrowPathsItem] | Unset):
        relationship_types (list[PersonMasterDataRelationshipTypesItem] | Unset):
        roles (list[PersonMasterDataRolesItem] | Unset):
        sexes (list[PersonMasterDataSexesItem] | Unset):
        statuses (list[PersonMasterDataStatusesItem] | Unset):
        target_groups (list[PersonMasterDataTargetGroupsItem] | Unset):
    """

    age_groups: list[PersonMasterDataAgeGroupsItem] | Unset = UNSET
    campuses: list[PersonMasterDataCampusesItem] | Unset = UNSET
    comment_viewers: list[PersonMasterDataCommentViewersItem] | Unset = UNSET
    contact_labels: list[PersonMasterDataContactLabelsItem] | Unset = UNSET
    departments: list[PersonMasterDataDepartmentsItem] | Unset = UNSET
    follow_up_intervals: list[PersonMasterDataFollowUpIntervalsItem] | Unset = UNSET
    follow_ups: list[PersonMasterDataFollowUpsItem] | Unset = UNSET
    group_categories: list[PersonMasterDataGroupCategoriesItem] | Unset = UNSET
    group_meeting_templates: list[PersonMasterDataGroupMeetingTemplatesItem] | Unset = (
        UNSET
    )
    group_statuses: list[PersonMasterDataGroupStatusesItem] | Unset = UNSET
    group_types: list[PersonMasterDataGroupTypesItem] | Unset = UNSET
    grow_paths: list[PersonMasterDataGrowPathsItem] | Unset = UNSET
    relationship_types: list[PersonMasterDataRelationshipTypesItem] | Unset = UNSET
    roles: list[PersonMasterDataRolesItem] | Unset = UNSET
    sexes: list[PersonMasterDataSexesItem] | Unset = UNSET
    statuses: list[PersonMasterDataStatusesItem] | Unset = UNSET
    target_groups: list[PersonMasterDataTargetGroupsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        age_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.age_groups, Unset):
            age_groups = []
            for age_groups_item_data in self.age_groups:
                age_groups_item = age_groups_item_data.to_dict()
                age_groups.append(age_groups_item)

        campuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.campuses, Unset):
            campuses = []
            for campuses_item_data in self.campuses:
                campuses_item = campuses_item_data.to_dict()
                campuses.append(campuses_item)

        comment_viewers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comment_viewers, Unset):
            comment_viewers = []
            for comment_viewers_item_data in self.comment_viewers:
                comment_viewers_item = comment_viewers_item_data.to_dict()
                comment_viewers.append(comment_viewers_item)

        contact_labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contact_labels, Unset):
            contact_labels = []
            for contact_labels_item_data in self.contact_labels:
                contact_labels_item = contact_labels_item_data.to_dict()
                contact_labels.append(contact_labels_item)

        departments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.departments, Unset):
            departments = []
            for departments_item_data in self.departments:
                departments_item = departments_item_data.to_dict()
                departments.append(departments_item)

        follow_up_intervals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.follow_up_intervals, Unset):
            follow_up_intervals = []
            for follow_up_intervals_item_data in self.follow_up_intervals:
                follow_up_intervals_item = follow_up_intervals_item_data.to_dict()
                follow_up_intervals.append(follow_up_intervals_item)

        follow_ups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.follow_ups, Unset):
            follow_ups = []
            for follow_ups_item_data in self.follow_ups:
                follow_ups_item = follow_ups_item_data.to_dict()
                follow_ups.append(follow_ups_item)

        group_categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_categories, Unset):
            group_categories = []
            for group_categories_item_data in self.group_categories:
                group_categories_item = group_categories_item_data.to_dict()
                group_categories.append(group_categories_item)

        group_meeting_templates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_meeting_templates, Unset):
            group_meeting_templates = []
            for group_meeting_templates_item_data in self.group_meeting_templates:
                group_meeting_templates_item = (
                    group_meeting_templates_item_data.to_dict()
                )
                group_meeting_templates.append(group_meeting_templates_item)

        group_statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_statuses, Unset):
            group_statuses = []
            for group_statuses_item_data in self.group_statuses:
                group_statuses_item = group_statuses_item_data.to_dict()
                group_statuses.append(group_statuses_item)

        group_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_types, Unset):
            group_types = []
            for group_types_item_data in self.group_types:
                group_types_item = group_types_item_data.to_dict()
                group_types.append(group_types_item)

        grow_paths: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grow_paths, Unset):
            grow_paths = []
            for grow_paths_item_data in self.grow_paths:
                grow_paths_item = grow_paths_item_data.to_dict()
                grow_paths.append(grow_paths_item)

        relationship_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.relationship_types, Unset):
            relationship_types = []
            for relationship_types_item_data in self.relationship_types:
                relationship_types_item = relationship_types_item_data.to_dict()
                relationship_types.append(relationship_types_item)

        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        sexes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sexes, Unset):
            sexes = []
            for sexes_item_data in self.sexes:
                sexes_item = sexes_item_data.to_dict()
                sexes.append(sexes_item)

        statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.to_dict()
                statuses.append(statuses_item)

        target_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target_groups, Unset):
            target_groups = []
            for target_groups_item_data in self.target_groups:
                target_groups_item = target_groups_item_data.to_dict()
                target_groups.append(target_groups_item)

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
        if relationship_types is not UNSET:
            field_dict["relationshipTypes"] = relationship_types
        if roles is not UNSET:
            field_dict["roles"] = roles
        if sexes is not UNSET:
            field_dict["sexes"] = sexes
        if statuses is not UNSET:
            field_dict["statuses"] = statuses
        if target_groups is not UNSET:
            field_dict["targetGroups"] = target_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person_master_data_age_groups_item import (
            PersonMasterDataAgeGroupsItem,
        )
        from ..models.person_master_data_campuses_item import (
            PersonMasterDataCampusesItem,
        )
        from ..models.person_master_data_comment_viewers_item import (
            PersonMasterDataCommentViewersItem,
        )
        from ..models.person_master_data_contact_labels_item import (
            PersonMasterDataContactLabelsItem,
        )
        from ..models.person_master_data_departments_item import (
            PersonMasterDataDepartmentsItem,
        )
        from ..models.person_master_data_follow_up_intervals_item import (
            PersonMasterDataFollowUpIntervalsItem,
        )
        from ..models.person_master_data_follow_ups_item import (
            PersonMasterDataFollowUpsItem,
        )
        from ..models.person_master_data_group_categories_item import (
            PersonMasterDataGroupCategoriesItem,
        )
        from ..models.person_master_data_group_meeting_templates_item import (
            PersonMasterDataGroupMeetingTemplatesItem,
        )
        from ..models.person_master_data_group_statuses_item import (
            PersonMasterDataGroupStatusesItem,
        )
        from ..models.person_master_data_group_types_item import (
            PersonMasterDataGroupTypesItem,
        )
        from ..models.person_master_data_grow_paths_item import (
            PersonMasterDataGrowPathsItem,
        )
        from ..models.person_master_data_relationship_types_item import (
            PersonMasterDataRelationshipTypesItem,
        )
        from ..models.person_master_data_roles_item import PersonMasterDataRolesItem
        from ..models.person_master_data_sexes_item import PersonMasterDataSexesItem
        from ..models.person_master_data_statuses_item import (
            PersonMasterDataStatusesItem,
        )
        from ..models.person_master_data_target_groups_item import (
            PersonMasterDataTargetGroupsItem,
        )

        d = dict(src_dict)
        age_groups = []
        _age_groups = d.pop("ageGroups", UNSET)
        for age_groups_item_data in _age_groups or []:
            age_groups_item = PersonMasterDataAgeGroupsItem.from_dict(
                age_groups_item_data
            )

            age_groups.append(age_groups_item)

        campuses = []
        _campuses = d.pop("campuses", UNSET)
        for campuses_item_data in _campuses or []:
            campuses_item = PersonMasterDataCampusesItem.from_dict(campuses_item_data)

            campuses.append(campuses_item)

        comment_viewers = []
        _comment_viewers = d.pop("commentViewers", UNSET)
        for comment_viewers_item_data in _comment_viewers or []:
            comment_viewers_item = PersonMasterDataCommentViewersItem.from_dict(
                comment_viewers_item_data
            )

            comment_viewers.append(comment_viewers_item)

        contact_labels = []
        _contact_labels = d.pop("contactLabels", UNSET)
        for contact_labels_item_data in _contact_labels or []:
            contact_labels_item = PersonMasterDataContactLabelsItem.from_dict(
                contact_labels_item_data
            )

            contact_labels.append(contact_labels_item)

        departments = []
        _departments = d.pop("departments", UNSET)
        for departments_item_data in _departments or []:
            departments_item = PersonMasterDataDepartmentsItem.from_dict(
                departments_item_data
            )

            departments.append(departments_item)

        follow_up_intervals = []
        _follow_up_intervals = d.pop("followUpIntervals", UNSET)
        for follow_up_intervals_item_data in _follow_up_intervals or []:
            follow_up_intervals_item = PersonMasterDataFollowUpIntervalsItem.from_dict(
                follow_up_intervals_item_data
            )

            follow_up_intervals.append(follow_up_intervals_item)

        follow_ups = []
        _follow_ups = d.pop("followUps", UNSET)
        for follow_ups_item_data in _follow_ups or []:
            follow_ups_item = PersonMasterDataFollowUpsItem.from_dict(
                follow_ups_item_data
            )

            follow_ups.append(follow_ups_item)

        group_categories = []
        _group_categories = d.pop("groupCategories", UNSET)
        for group_categories_item_data in _group_categories or []:
            group_categories_item = PersonMasterDataGroupCategoriesItem.from_dict(
                group_categories_item_data
            )

            group_categories.append(group_categories_item)

        group_meeting_templates = []
        _group_meeting_templates = d.pop("groupMeetingTemplates", UNSET)
        for group_meeting_templates_item_data in _group_meeting_templates or []:
            group_meeting_templates_item = (
                PersonMasterDataGroupMeetingTemplatesItem.from_dict(
                    group_meeting_templates_item_data
                )
            )

            group_meeting_templates.append(group_meeting_templates_item)

        group_statuses = []
        _group_statuses = d.pop("groupStatuses", UNSET)
        for group_statuses_item_data in _group_statuses or []:
            group_statuses_item = PersonMasterDataGroupStatusesItem.from_dict(
                group_statuses_item_data
            )

            group_statuses.append(group_statuses_item)

        group_types = []
        _group_types = d.pop("groupTypes", UNSET)
        for group_types_item_data in _group_types or []:
            group_types_item = PersonMasterDataGroupTypesItem.from_dict(
                group_types_item_data
            )

            group_types.append(group_types_item)

        grow_paths = []
        _grow_paths = d.pop("growPaths", UNSET)
        for grow_paths_item_data in _grow_paths or []:
            grow_paths_item = PersonMasterDataGrowPathsItem.from_dict(
                grow_paths_item_data
            )

            grow_paths.append(grow_paths_item)

        relationship_types = []
        _relationship_types = d.pop("relationshipTypes", UNSET)
        for relationship_types_item_data in _relationship_types or []:
            relationship_types_item = PersonMasterDataRelationshipTypesItem.from_dict(
                relationship_types_item_data
            )

            relationship_types.append(relationship_types_item)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = PersonMasterDataRolesItem.from_dict(roles_item_data)

            roles.append(roles_item)

        sexes = []
        _sexes = d.pop("sexes", UNSET)
        for sexes_item_data in _sexes or []:
            sexes_item = PersonMasterDataSexesItem.from_dict(sexes_item_data)

            sexes.append(sexes_item)

        statuses = []
        _statuses = d.pop("statuses", UNSET)
        for statuses_item_data in _statuses or []:
            statuses_item = PersonMasterDataStatusesItem.from_dict(statuses_item_data)

            statuses.append(statuses_item)

        target_groups = []
        _target_groups = d.pop("targetGroups", UNSET)
        for target_groups_item_data in _target_groups or []:
            target_groups_item = PersonMasterDataTargetGroupsItem.from_dict(
                target_groups_item_data
            )

            target_groups.append(target_groups_item)

        person_master_data = cls(
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
            relationship_types=relationship_types,
            roles=roles,
            sexes=sexes,
            statuses=statuses,
            target_groups=target_groups,
        )

        person_master_data.additional_properties = d
        return person_master_data

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
