from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_html_template_body_domain_type import (
    CreateHtmlTemplateBodyDomainType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateHtmlTemplateBody")


@_attrs_define
class CreateHtmlTemplateBody:
    """
    Attributes:
        domain_type (CreateHtmlTemplateBodyDomainType | Unset):  Example: email.
        html (str | Unset):
        is_global (bool | Unset): Indicator if HTML template is globally available for all users.
        mjml (str | Unset):
        name (str | Unset): Name of HTML template Example: Rundbrief.
    """

    domain_type: CreateHtmlTemplateBodyDomainType | Unset = UNSET
    html: str | Unset = UNSET
    is_global: bool | Unset = UNSET
    mjml: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_type: str | Unset = UNSET
        if not isinstance(self.domain_type, Unset):
            domain_type = self.domain_type.value

        html = self.html

        is_global = self.is_global

        mjml = self.mjml

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_type is not UNSET:
            field_dict["domainType"] = domain_type
        if html is not UNSET:
            field_dict["html"] = html
        if is_global is not UNSET:
            field_dict["isGlobal"] = is_global
        if mjml is not UNSET:
            field_dict["mjml"] = mjml
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _domain_type = d.pop("domainType", UNSET)
        domain_type: CreateHtmlTemplateBodyDomainType | Unset
        if isinstance(_domain_type, Unset):
            domain_type = UNSET
        else:
            domain_type = CreateHtmlTemplateBodyDomainType(_domain_type)

        html = d.pop("html", UNSET)

        is_global = d.pop("isGlobal", UNSET)

        mjml = d.pop("mjml", UNSET)

        name = d.pop("name", UNSET)

        create_html_template_body = cls(
            domain_type=domain_type,
            html=html,
            is_global=is_global,
            mjml=mjml,
            name=name,
        )

        create_html_template_body.additional_properties = d
        return create_html_template_body

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
