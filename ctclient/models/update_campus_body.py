from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_campus_body_denomination import UpdateCampusBodyDenomination
from ..models.update_campus_body_visitors import UpdateCampusBodyVisitors

if TYPE_CHECKING:
    from ..models.update_campus_body_address import UpdateCampusBodyAddress
    from ..models.update_campus_body_groups_item_type_0 import (
        UpdateCampusBodyGroupsItemType0,
    )
    from ..models.update_campus_body_services_item import UpdateCampusBodyServicesItem
    from ..models.update_campus_body_sign_up_group_type_0 import (
        UpdateCampusBodySignUpGroupType0,
    )
    from ..models.update_campus_body_social_media import UpdateCampusBodySocialMedia
    from ..models.update_campus_body_team_item import UpdateCampusBodyTeamItem


T = TypeVar("T", bound="UpdateCampusBody")


@_attrs_define
class UpdateCampusBody:
    """
    Attributes:
        address (UpdateCampusBodyAddress):
        association_id (int):
        denomination (UpdateCampusBodyDenomination): Either exact string or denomination object with name property
        description (str):
        email (str):
        groups (list[float | UpdateCampusBodyGroupsItemType0]): Either array of group IDs or array of objects with
            group-property, which is a domain object wiht 'domainIdentifier'
        is_published (bool):
        name (str):
        phone (str):
        services (list[UpdateCampusBodyServicesItem]):
        short_name (str):
        shorty (str):
        sign_up_group (float | UpdateCampusBodySignUpGroupType0): SignUp Group; Either groupId or domainObject
        slug (str):
        social_media (UpdateCampusBodySocialMedia): Key-Value Pair, where key is the name of the network and value is
            the absolute link
        sort_key (int):  Default: 0.
        tags (list[str]): List of tags.
        team (list[UpdateCampusBodyTeamItem]):
        team_title (str):
        visitors (UpdateCampusBodyVisitors): Single integer, which represents a range.
        website (str):
    """

    address: UpdateCampusBodyAddress
    association_id: int
    denomination: UpdateCampusBodyDenomination
    description: str
    email: str
    groups: list[float | UpdateCampusBodyGroupsItemType0]
    is_published: bool
    name: str
    phone: str
    services: list[UpdateCampusBodyServicesItem]
    short_name: str
    shorty: str
    sign_up_group: float | UpdateCampusBodySignUpGroupType0
    slug: str
    social_media: UpdateCampusBodySocialMedia
    tags: list[str]
    team: list[UpdateCampusBodyTeamItem]
    team_title: str
    visitors: UpdateCampusBodyVisitors
    website: str
    sort_key: int = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_campus_body_groups_item_type_0 import (
            UpdateCampusBodyGroupsItemType0,
        )
        from ..models.update_campus_body_sign_up_group_type_0 import (
            UpdateCampusBodySignUpGroupType0,
        )

        address = self.address.to_dict()

        association_id = self.association_id

        denomination = self.denomination.value

        description = self.description

        email = self.email

        groups = []
        for groups_item_data in self.groups:
            groups_item: dict[str, Any] | float
            if isinstance(groups_item_data, UpdateCampusBodyGroupsItemType0):
                groups_item = groups_item_data.to_dict()
            else:
                groups_item = groups_item_data
            groups.append(groups_item)

        is_published = self.is_published

        name = self.name

        phone = self.phone

        services = []
        for services_item_data in self.services:
            services_item = services_item_data.to_dict()
            services.append(services_item)

        short_name = self.short_name

        shorty = self.shorty

        sign_up_group: dict[str, Any] | float
        if isinstance(self.sign_up_group, UpdateCampusBodySignUpGroupType0):
            sign_up_group = self.sign_up_group.to_dict()
        else:
            sign_up_group = self.sign_up_group

        slug = self.slug

        social_media = self.social_media.to_dict()

        sort_key = self.sort_key

        tags = self.tags

        team = []
        for team_item_data in self.team:
            team_item = team_item_data.to_dict()
            team.append(team_item)

        team_title = self.team_title

        visitors = self.visitors.value

        website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "associationId": association_id,
                "denomination": denomination,
                "description": description,
                "email": email,
                "groups": groups,
                "isPublished": is_published,
                "name": name,
                "phone": phone,
                "services": services,
                "shortName": short_name,
                "shorty": shorty,
                "signUpGroup": sign_up_group,
                "slug": slug,
                "socialMedia": social_media,
                "sortKey": sort_key,
                "tags": tags,
                "team": team,
                "teamTitle": team_title,
                "visitors": visitors,
                "website": website,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_campus_body_address import UpdateCampusBodyAddress
        from ..models.update_campus_body_groups_item_type_0 import (
            UpdateCampusBodyGroupsItemType0,
        )
        from ..models.update_campus_body_services_item import (
            UpdateCampusBodyServicesItem,
        )
        from ..models.update_campus_body_sign_up_group_type_0 import (
            UpdateCampusBodySignUpGroupType0,
        )
        from ..models.update_campus_body_social_media import UpdateCampusBodySocialMedia
        from ..models.update_campus_body_team_item import UpdateCampusBodyTeamItem

        d = dict(src_dict)
        address = UpdateCampusBodyAddress.from_dict(d.pop("address"))

        association_id = d.pop("associationId")

        denomination = UpdateCampusBodyDenomination(d.pop("denomination"))

        description = d.pop("description")

        email = d.pop("email")

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:

            def _parse_groups_item(
                data: object,
            ) -> float | UpdateCampusBodyGroupsItemType0:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    groups_item_type_0 = UpdateCampusBodyGroupsItemType0.from_dict(data)

                    return groups_item_type_0
                except:  # noqa: E722
                    pass
                return cast(float | UpdateCampusBodyGroupsItemType0, data)

            groups_item = _parse_groups_item(groups_item_data)

            groups.append(groups_item)

        is_published = d.pop("isPublished")

        name = d.pop("name")

        phone = d.pop("phone")

        services = []
        _services = d.pop("services")
        for services_item_data in _services:
            services_item = UpdateCampusBodyServicesItem.from_dict(services_item_data)

            services.append(services_item)

        short_name = d.pop("shortName")

        shorty = d.pop("shorty")

        def _parse_sign_up_group(
            data: object,
        ) -> float | UpdateCampusBodySignUpGroupType0:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sign_up_group_type_0 = UpdateCampusBodySignUpGroupType0.from_dict(data)

                return sign_up_group_type_0
            except:  # noqa: E722
                pass
            return cast(float | UpdateCampusBodySignUpGroupType0, data)

        sign_up_group = _parse_sign_up_group(d.pop("signUpGroup"))

        slug = d.pop("slug")

        social_media = UpdateCampusBodySocialMedia.from_dict(d.pop("socialMedia"))

        sort_key = d.pop("sortKey")

        tags = cast(list[str], d.pop("tags"))

        team = []
        _team = d.pop("team")
        for team_item_data in _team:
            team_item = UpdateCampusBodyTeamItem.from_dict(team_item_data)

            team.append(team_item)

        team_title = d.pop("teamTitle")

        visitors = UpdateCampusBodyVisitors(d.pop("visitors"))

        website = d.pop("website")

        update_campus_body = cls(
            address=address,
            association_id=association_id,
            denomination=denomination,
            description=description,
            email=email,
            groups=groups,
            is_published=is_published,
            name=name,
            phone=phone,
            services=services,
            short_name=short_name,
            shorty=shorty,
            sign_up_group=sign_up_group,
            slug=slug,
            social_media=social_media,
            sort_key=sort_key,
            tags=tags,
            team=team,
            team_title=team_title,
            visitors=visitors,
            website=website,
        )

        update_campus_body.additional_properties = d
        return update_campus_body

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
