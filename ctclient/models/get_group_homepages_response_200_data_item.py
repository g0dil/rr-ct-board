from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_group_homepages_response_200_data_item_domain_type import (
    GetGroupHomepagesResponse200DataItemDomainType,
)
from ..models.get_group_homepages_response_200_data_item_icon import (
    GetGroupHomepagesResponse200DataItemIcon,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_group_homepages_response_200_data_item_color import (
        GetGroupHomepagesResponse200DataItemColor,
    )
    from ..models.get_group_homepages_response_200_data_item_domain_attributes import (
        GetGroupHomepagesResponse200DataItemDomainAttributes,
    )


T = TypeVar("T", bound="GetGroupHomepagesResponse200DataItem")


@_attrs_define
class GetGroupHomepagesResponse200DataItem:
    """
    Attributes:
        domain_identifier (str):
        frontend_url (None | str):
        title (str):
        domain_attributes (GetGroupHomepagesResponse200DataItemDomainAttributes):
        domain_type (GetGroupHomepagesResponse200DataItemDomainType):
        icon (GetGroupHomepagesResponse200DataItemIcon):
        api_url (None | str | Unset):
        color (GetGroupHomepagesResponse200DataItemColor | None | Unset):
        image_url (None | str | Unset):
        infos (list[str] | Unset):
        initials (None | str | Unset):
    """

    domain_identifier: str
    frontend_url: None | str
    title: str
    domain_attributes: GetGroupHomepagesResponse200DataItemDomainAttributes
    domain_type: GetGroupHomepagesResponse200DataItemDomainType
    icon: GetGroupHomepagesResponse200DataItemIcon
    api_url: None | str | Unset = UNSET
    color: GetGroupHomepagesResponse200DataItemColor | None | Unset = UNSET
    image_url: None | str | Unset = UNSET
    infos: list[str] | Unset = UNSET
    initials: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_group_homepages_response_200_data_item_color import (
            GetGroupHomepagesResponse200DataItemColor,
        )

        domain_identifier = self.domain_identifier

        frontend_url: None | str
        frontend_url = self.frontend_url

        title = self.title

        domain_attributes = self.domain_attributes.to_dict()

        domain_type = self.domain_type.value

        icon = self.icon.value

        api_url: None | str | Unset
        if isinstance(self.api_url, Unset):
            api_url = UNSET
        else:
            api_url = self.api_url

        color: dict[str, Any] | None | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        elif isinstance(self.color, GetGroupHomepagesResponse200DataItemColor):
            color = self.color.to_dict()
        else:
            color = self.color

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        infos: list[str] | Unset = UNSET
        if not isinstance(self.infos, Unset):
            infos = self.infos

        initials: None | str | Unset
        if isinstance(self.initials, Unset):
            initials = UNSET
        else:
            initials = self.initials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainIdentifier": domain_identifier,
                "frontendUrl": frontend_url,
                "title": title,
                "domainAttributes": domain_attributes,
                "domainType": domain_type,
                "icon": icon,
            }
        )
        if api_url is not UNSET:
            field_dict["apiUrl"] = api_url
        if color is not UNSET:
            field_dict["color"] = color
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if infos is not UNSET:
            field_dict["infos"] = infos
        if initials is not UNSET:
            field_dict["initials"] = initials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_group_homepages_response_200_data_item_color import (
            GetGroupHomepagesResponse200DataItemColor,
        )
        from ..models.get_group_homepages_response_200_data_item_domain_attributes import (
            GetGroupHomepagesResponse200DataItemDomainAttributes,
        )

        d = dict(src_dict)
        domain_identifier = d.pop("domainIdentifier")

        def _parse_frontend_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        frontend_url = _parse_frontend_url(d.pop("frontendUrl"))

        title = d.pop("title")

        domain_attributes = (
            GetGroupHomepagesResponse200DataItemDomainAttributes.from_dict(
                d.pop("domainAttributes")
            )
        )

        domain_type = GetGroupHomepagesResponse200DataItemDomainType(
            d.pop("domainType")
        )

        icon = GetGroupHomepagesResponse200DataItemIcon(d.pop("icon"))

        def _parse_api_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_url = _parse_api_url(d.pop("apiUrl", UNSET))

        def _parse_color(
            data: object,
        ) -> GetGroupHomepagesResponse200DataItemColor | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                color_color = GetGroupHomepagesResponse200DataItemColor.from_dict(data)

                return color_color
            except:  # noqa: E722
                pass
            return cast(GetGroupHomepagesResponse200DataItemColor | None | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("imageUrl", UNSET))

        infos = cast(list[str], d.pop("infos", UNSET))

        def _parse_initials(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initials = _parse_initials(d.pop("initials", UNSET))

        get_group_homepages_response_200_data_item = cls(
            domain_identifier=domain_identifier,
            frontend_url=frontend_url,
            title=title,
            domain_attributes=domain_attributes,
            domain_type=domain_type,
            icon=icon,
            api_url=api_url,
            color=color,
            image_url=image_url,
            infos=infos,
            initials=initials,
        )

        get_group_homepages_response_200_data_item.additional_properties = d
        return get_group_homepages_response_200_data_item

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
