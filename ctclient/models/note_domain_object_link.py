from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.note_domain_object_link_domain_type import NoteDomainObjectLinkDomainType

T = TypeVar("T", bound="NoteDomainObjectLink")


@_attrs_define
class NoteDomainObjectLink:
    """
    Attributes:
        comment_viewer_id (int | None):
        domain_id (int):
        domain_type (NoteDomainObjectLinkDomainType): Domain types that notes can be used with Example: group.
        security_level_id (int | None):
    """

    comment_viewer_id: int | None
    domain_id: int
    domain_type: NoteDomainObjectLinkDomainType
    security_level_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_viewer_id: int | None
        comment_viewer_id = self.comment_viewer_id

        domain_id = self.domain_id

        domain_type = self.domain_type.value

        security_level_id: int | None
        security_level_id = self.security_level_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentViewerId": comment_viewer_id,
                "domainId": domain_id,
                "domainType": domain_type,
                "securityLevelId": security_level_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_comment_viewer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        comment_viewer_id = _parse_comment_viewer_id(d.pop("commentViewerId"))

        domain_id = d.pop("domainId")

        domain_type = NoteDomainObjectLinkDomainType(d.pop("domainType"))

        def _parse_security_level_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        security_level_id = _parse_security_level_id(d.pop("securityLevelId"))

        note_domain_object_link = cls(
            comment_viewer_id=comment_viewer_id,
            domain_id=domain_id,
            domain_type=domain_type,
            security_level_id=security_level_id,
        )

        note_domain_object_link.additional_properties = d
        return note_domain_object_link

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
