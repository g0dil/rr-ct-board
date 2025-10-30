from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_object_action_color_type_0 import DomainObjectActionColorType0
from ..models.domain_object_action_domain_type import DomainObjectActionDomainType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_object_action_domain_attributes import (
        DomainObjectActionDomainAttributes,
    )


T = TypeVar("T", bound="DomainObjectAction")


@_attrs_define
class DomainObjectAction:
    """Action as Domain Object

    Attributes:
        domain_type (DomainObjectActionDomainType):
        icon (str):
        api_url (None | Unset):
        color (DomainObjectActionColorType0 | None | Unset):
        domain_attributes (DomainObjectActionDomainAttributes | Unset):
        domain_identifier (str | Unset):
        frontend_url (str | Unset):
        image_url (None | Unset):
        infos (list[str] | Unset):
        initials (None | Unset):
        title (str | Unset):
    """

    domain_type: DomainObjectActionDomainType
    icon: str
    api_url: None | Unset = UNSET
    color: DomainObjectActionColorType0 | None | Unset = UNSET
    domain_attributes: DomainObjectActionDomainAttributes | Unset = UNSET
    domain_identifier: str | Unset = UNSET
    frontend_url: str | Unset = UNSET
    image_url: None | Unset = UNSET
    infos: list[str] | Unset = UNSET
    initials: None | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_type = self.domain_type.value

        icon = self.icon

        api_url = self.api_url

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        elif isinstance(self.color, DomainObjectActionColorType0):
            color = self.color.value
        else:
            color = self.color

        domain_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain_attributes, Unset):
            domain_attributes = self.domain_attributes.to_dict()

        domain_identifier = self.domain_identifier

        frontend_url = self.frontend_url

        image_url = self.image_url

        infos: list[str] | Unset = UNSET
        if not isinstance(self.infos, Unset):
            infos = self.infos

        initials = self.initials

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainType": domain_type,
                "icon": icon,
            }
        )
        if api_url is not UNSET:
            field_dict["apiUrl"] = api_url
        if color is not UNSET:
            field_dict["color"] = color
        if domain_attributes is not UNSET:
            field_dict["domainAttributes"] = domain_attributes
        if domain_identifier is not UNSET:
            field_dict["domainIdentifier"] = domain_identifier
        if frontend_url is not UNSET:
            field_dict["frontendUrl"] = frontend_url
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if infos is not UNSET:
            field_dict["infos"] = infos
        if initials is not UNSET:
            field_dict["initials"] = initials
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_object_action_domain_attributes import (
            DomainObjectActionDomainAttributes,
        )

        d = dict(src_dict)
        domain_type = DomainObjectActionDomainType(d.pop("domainType"))

        icon = d.pop("icon")

        api_url = d.pop("apiUrl", UNSET)

        def _parse_color(data: object) -> DomainObjectActionColorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                color_type_0 = DomainObjectActionColorType0(data)

                return color_type_0
            except:  # noqa: E722
                pass
            return cast(DomainObjectActionColorType0 | None | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        _domain_attributes = d.pop("domainAttributes", UNSET)
        domain_attributes: DomainObjectActionDomainAttributes | Unset
        if isinstance(_domain_attributes, Unset):
            domain_attributes = UNSET
        else:
            domain_attributes = DomainObjectActionDomainAttributes.from_dict(
                _domain_attributes
            )

        domain_identifier = d.pop("domainIdentifier", UNSET)

        frontend_url = d.pop("frontendUrl", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        infos = cast(list[str], d.pop("infos", UNSET))

        initials = d.pop("initials", UNSET)

        title = d.pop("title", UNSET)

        domain_object_action = cls(
            domain_type=domain_type,
            icon=icon,
            api_url=api_url,
            color=color,
            domain_attributes=domain_attributes,
            domain_identifier=domain_identifier,
            frontend_url=frontend_url,
            image_url=image_url,
            infos=infos,
            initials=initials,
            title=title,
        )

        domain_object_action.additional_properties = d
        return domain_object_action

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
