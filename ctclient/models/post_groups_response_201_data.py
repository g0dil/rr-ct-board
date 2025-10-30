from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_groups_response_201_data_follow_up import (
        PostGroupsResponse201DataFollowUp,
    )
    from ..models.post_groups_response_201_data_information import (
        PostGroupsResponse201DataInformation,
    )
    from ..models.post_groups_response_201_data_member_statistics import (
        PostGroupsResponse201DataMemberStatistics,
    )
    from ..models.post_groups_response_201_data_meta import (
        PostGroupsResponse201DataMeta,
    )
    from ..models.post_groups_response_201_data_modified_person import (
        PostGroupsResponse201DataModifiedPerson,
    )
    from ..models.post_groups_response_201_data_permissions import (
        PostGroupsResponse201DataPermissions,
    )
    from ..models.post_groups_response_201_data_places_item import (
        PostGroupsResponse201DataPlacesItem,
    )
    from ..models.post_groups_response_201_data_public_posts_statistic import (
        PostGroupsResponse201DataPublicPostsStatistic,
    )
    from ..models.post_groups_response_201_data_roles_item import (
        PostGroupsResponse201DataRolesItem,
    )
    from ..models.post_groups_response_201_data_settings import (
        PostGroupsResponse201DataSettings,
    )
    from ..models.post_groups_response_201_data_signup_conditions import (
        PostGroupsResponse201DataSignupConditions,
    )
    from ..models.post_groups_response_201_data_tags_item import (
        PostGroupsResponse201DataTagsItem,
    )


T = TypeVar("T", bound="PostGroupsResponse201Data")


@_attrs_define
class PostGroupsResponse201Data:
    """The group model structures all information in different objects: `information`, `settings`, `followUp`, and `roles`.
    Custom group fields are added to the root level of this model.

        Attributes:
            follow_up (PostGroupsResponse201DataFollowUp):
            guid (str):  Example: 681F54E3-2EB7-40A4-84F0-EFF8E8F05727.
            id (int):  Example: 42.
            information (PostGroupsResponse201DataInformation):
            meta (PostGroupsResponse201DataMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson': {'id':
                1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
            name (str):  Example: Smallgroup West.
            permissions (PostGroupsResponse201DataPermissions):
            security_level_for_group (int): You can see group fields up to this security level. Example: 3.
            settings (PostGroupsResponse201DataSettings):
            has_permissions (bool | Unset):
            member_statistics (PostGroupsResponse201DataMemberStatistics | Unset):
            modified_date (str | Unset):
            modified_person (PostGroupsResponse201DataModifiedPerson | Unset):
            places (list[PostGroupsResponse201DataPlacesItem] | Unset):
            public_posts_statistic (PostGroupsResponse201DataPublicPostsStatistic | Unset):
            roles (list[PostGroupsResponse201DataRolesItem] | Unset):
            signup_conditions (PostGroupsResponse201DataSignupConditions | Unset):
            tags (list[PostGroupsResponse201DataTagsItem] | Unset):
    """

    follow_up: PostGroupsResponse201DataFollowUp
    guid: str
    id: int
    information: PostGroupsResponse201DataInformation
    meta: PostGroupsResponse201DataMeta
    name: str
    permissions: PostGroupsResponse201DataPermissions
    security_level_for_group: int
    settings: PostGroupsResponse201DataSettings
    has_permissions: bool | Unset = UNSET
    member_statistics: PostGroupsResponse201DataMemberStatistics | Unset = UNSET
    modified_date: str | Unset = UNSET
    modified_person: PostGroupsResponse201DataModifiedPerson | Unset = UNSET
    places: list[PostGroupsResponse201DataPlacesItem] | Unset = UNSET
    public_posts_statistic: PostGroupsResponse201DataPublicPostsStatistic | Unset = (
        UNSET
    )
    roles: list[PostGroupsResponse201DataRolesItem] | Unset = UNSET
    signup_conditions: PostGroupsResponse201DataSignupConditions | Unset = UNSET
    tags: list[PostGroupsResponse201DataTagsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        follow_up = self.follow_up.to_dict()

        guid = self.guid

        id = self.id

        information = self.information.to_dict()

        meta = self.meta.to_dict()

        name = self.name

        permissions = self.permissions.to_dict()

        security_level_for_group = self.security_level_for_group

        settings = self.settings.to_dict()

        has_permissions = self.has_permissions

        member_statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.member_statistics, Unset):
            member_statistics = self.member_statistics.to_dict()

        modified_date = self.modified_date

        modified_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modified_person, Unset):
            modified_person = self.modified_person.to_dict()

        places: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.places, Unset):
            places = []
            for places_item_data in self.places:
                places_item = places_item_data.to_dict()
                places.append(places_item)

        public_posts_statistic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_posts_statistic, Unset):
            public_posts_statistic = self.public_posts_statistic.to_dict()

        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        signup_conditions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signup_conditions, Unset):
            signup_conditions = self.signup_conditions.to_dict()

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "followUp": follow_up,
                "guid": guid,
                "id": id,
                "information": information,
                "meta": meta,
                "name": name,
                "permissions": permissions,
                "securityLevelForGroup": security_level_for_group,
                "settings": settings,
            }
        )
        if has_permissions is not UNSET:
            field_dict["hasPermissions"] = has_permissions
        if member_statistics is not UNSET:
            field_dict["memberStatistics"] = member_statistics
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if modified_person is not UNSET:
            field_dict["modifiedPerson"] = modified_person
        if places is not UNSET:
            field_dict["places"] = places
        if public_posts_statistic is not UNSET:
            field_dict["publicPostsStatistic"] = public_posts_statistic
        if roles is not UNSET:
            field_dict["roles"] = roles
        if signup_conditions is not UNSET:
            field_dict["signupConditions"] = signup_conditions
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_groups_response_201_data_follow_up import (
            PostGroupsResponse201DataFollowUp,
        )
        from ..models.post_groups_response_201_data_information import (
            PostGroupsResponse201DataInformation,
        )
        from ..models.post_groups_response_201_data_member_statistics import (
            PostGroupsResponse201DataMemberStatistics,
        )
        from ..models.post_groups_response_201_data_meta import (
            PostGroupsResponse201DataMeta,
        )
        from ..models.post_groups_response_201_data_modified_person import (
            PostGroupsResponse201DataModifiedPerson,
        )
        from ..models.post_groups_response_201_data_permissions import (
            PostGroupsResponse201DataPermissions,
        )
        from ..models.post_groups_response_201_data_places_item import (
            PostGroupsResponse201DataPlacesItem,
        )
        from ..models.post_groups_response_201_data_public_posts_statistic import (
            PostGroupsResponse201DataPublicPostsStatistic,
        )
        from ..models.post_groups_response_201_data_roles_item import (
            PostGroupsResponse201DataRolesItem,
        )
        from ..models.post_groups_response_201_data_settings import (
            PostGroupsResponse201DataSettings,
        )
        from ..models.post_groups_response_201_data_signup_conditions import (
            PostGroupsResponse201DataSignupConditions,
        )
        from ..models.post_groups_response_201_data_tags_item import (
            PostGroupsResponse201DataTagsItem,
        )

        d = dict(src_dict)
        follow_up = PostGroupsResponse201DataFollowUp.from_dict(d.pop("followUp"))

        guid = d.pop("guid")

        id = d.pop("id")

        information = PostGroupsResponse201DataInformation.from_dict(
            d.pop("information")
        )

        meta = PostGroupsResponse201DataMeta.from_dict(d.pop("meta"))

        name = d.pop("name")

        permissions = PostGroupsResponse201DataPermissions.from_dict(
            d.pop("permissions")
        )

        security_level_for_group = d.pop("securityLevelForGroup")

        settings = PostGroupsResponse201DataSettings.from_dict(d.pop("settings"))

        has_permissions = d.pop("hasPermissions", UNSET)

        _member_statistics = d.pop("memberStatistics", UNSET)
        member_statistics: PostGroupsResponse201DataMemberStatistics | Unset
        if isinstance(_member_statistics, Unset):
            member_statistics = UNSET
        else:
            member_statistics = PostGroupsResponse201DataMemberStatistics.from_dict(
                _member_statistics
            )

        modified_date = d.pop("modifiedDate", UNSET)

        _modified_person = d.pop("modifiedPerson", UNSET)
        modified_person: PostGroupsResponse201DataModifiedPerson | Unset
        if isinstance(_modified_person, Unset):
            modified_person = UNSET
        else:
            modified_person = PostGroupsResponse201DataModifiedPerson.from_dict(
                _modified_person
            )

        places = []
        _places = d.pop("places", UNSET)
        for places_item_data in _places or []:
            places_item = PostGroupsResponse201DataPlacesItem.from_dict(
                places_item_data
            )

            places.append(places_item)

        _public_posts_statistic = d.pop("publicPostsStatistic", UNSET)
        public_posts_statistic: PostGroupsResponse201DataPublicPostsStatistic | Unset
        if isinstance(_public_posts_statistic, Unset):
            public_posts_statistic = UNSET
        else:
            public_posts_statistic = (
                PostGroupsResponse201DataPublicPostsStatistic.from_dict(
                    _public_posts_statistic
                )
            )

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = PostGroupsResponse201DataRolesItem.from_dict(roles_item_data)

            roles.append(roles_item)

        _signup_conditions = d.pop("signupConditions", UNSET)
        signup_conditions: PostGroupsResponse201DataSignupConditions | Unset
        if isinstance(_signup_conditions, Unset):
            signup_conditions = UNSET
        else:
            signup_conditions = PostGroupsResponse201DataSignupConditions.from_dict(
                _signup_conditions
            )

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = PostGroupsResponse201DataTagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        post_groups_response_201_data = cls(
            follow_up=follow_up,
            guid=guid,
            id=id,
            information=information,
            meta=meta,
            name=name,
            permissions=permissions,
            security_level_for_group=security_level_for_group,
            settings=settings,
            has_permissions=has_permissions,
            member_statistics=member_statistics,
            modified_date=modified_date,
            modified_person=modified_person,
            places=places,
            public_posts_statistic=public_posts_statistic,
            roles=roles,
            signup_conditions=signup_conditions,
            tags=tags,
        )

        post_groups_response_201_data.additional_properties = d
        return post_groups_response_201_data

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
