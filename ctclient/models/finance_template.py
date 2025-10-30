from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finance_template_counts import FinanceTemplateCounts


T = TypeVar("T", bound="FinanceTemplate")


@_attrs_define
class FinanceTemplate:
    """
    Attributes:
        domain_identifier (str):
        domain_type (str):
        filename (str):
        id (float):
        name (str):
        relative_url (str):
        url (str):
        counts (FinanceTemplateCounts | Unset):
        security_level_id (float | Unset):
        size (float | Unset):
    """

    domain_identifier: str
    domain_type: str
    filename: str
    id: float
    name: str
    relative_url: str
    url: str
    counts: FinanceTemplateCounts | Unset = UNSET
    security_level_id: float | Unset = UNSET
    size: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_identifier = self.domain_identifier

        domain_type = self.domain_type

        filename = self.filename

        id = self.id

        name = self.name

        relative_url = self.relative_url

        url = self.url

        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        security_level_id = self.security_level_id

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainIdentifier": domain_identifier,
                "domainType": domain_type,
                "filename": filename,
                "id": id,
                "name": name,
                "relativeUrl": relative_url,
                "url": url,
            }
        )
        if counts is not UNSET:
            field_dict["counts"] = counts
        if security_level_id is not UNSET:
            field_dict["securityLevelId"] = security_level_id
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.finance_template_counts import FinanceTemplateCounts

        d = dict(src_dict)
        domain_identifier = d.pop("domainIdentifier")

        domain_type = d.pop("domainType")

        filename = d.pop("filename")

        id = d.pop("id")

        name = d.pop("name")

        relative_url = d.pop("relativeUrl")

        url = d.pop("url")

        _counts = d.pop("counts", UNSET)
        counts: FinanceTemplateCounts | Unset
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = FinanceTemplateCounts.from_dict(_counts)

        security_level_id = d.pop("securityLevelId", UNSET)

        size = d.pop("size", UNSET)

        finance_template = cls(
            domain_identifier=domain_identifier,
            domain_type=domain_type,
            filename=filename,
            id=id,
            name=name,
            relative_url=relative_url,
            url=url,
            counts=counts,
            security_level_id=security_level_id,
            size=size,
        )

        finance_template.additional_properties = d
        return finance_template

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
