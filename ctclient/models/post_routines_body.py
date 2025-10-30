from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_routines_body_domain_type import PostRoutinesBodyDomainType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_routines_body_domain_context import PostRoutinesBodyDomainContext


T = TypeVar("T", bound="PostRoutinesBody")


@_attrs_define
class PostRoutinesBody:
    """
    Attributes:
        domain_type (PostRoutinesBodyDomainType):
        name (str):
        description (None | str | Unset):
        domain_context (PostRoutinesBodyDomainContext | Unset): Attributes of the context in which this routine is going
            to be executed.
        is_enabled (bool | Unset):  Default: False.
        priority (int | Unset):  Default: 0.
    """

    domain_type: PostRoutinesBodyDomainType
    name: str
    description: None | str | Unset = UNSET
    domain_context: PostRoutinesBodyDomainContext | Unset = UNSET
    is_enabled: bool | Unset = False
    priority: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_type = self.domain_type.value

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        domain_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain_context, Unset):
            domain_context = self.domain_context.to_dict()

        is_enabled = self.is_enabled

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainType": domain_type,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if domain_context is not UNSET:
            field_dict["domainContext"] = domain_context
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_routines_body_domain_context import (
            PostRoutinesBodyDomainContext,
        )

        d = dict(src_dict)
        domain_type = PostRoutinesBodyDomainType(d.pop("domainType"))

        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _domain_context = d.pop("domainContext", UNSET)
        domain_context: PostRoutinesBodyDomainContext | Unset
        if isinstance(_domain_context, Unset):
            domain_context = UNSET
        else:
            domain_context = PostRoutinesBodyDomainContext.from_dict(_domain_context)

        is_enabled = d.pop("isEnabled", UNSET)

        priority = d.pop("priority", UNSET)

        post_routines_body = cls(
            domain_type=domain_type,
            name=name,
            description=description,
            domain_context=domain_context,
            is_enabled=is_enabled,
            priority=priority,
        )

        post_routines_body.additional_properties = d
        return post_routines_body

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
