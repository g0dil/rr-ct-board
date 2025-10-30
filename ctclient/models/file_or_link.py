from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_or_link_meta import FileOrLinkMeta


T = TypeVar("T", bound="FileOrLink")


@_attrs_define
class FileOrLink:
    """File or Link for a specific domain type. E.g. uploaded music file for songs or avatar of a person.

    Attributes:
        domain_id (str | Unset):  Example: 1.
        domain_type (str | Unset): ChurchTools Domain Type. Where does this file belong to? Example: avatar.
        file_url (str | Unset): Link to external website or link to file in ChurchTools Example: http://churchtools.test
            /?q=public/filedownload&id=116&filename=57407b0f37e8833cc7ff34f76413885e3856336ff21a263187c6bbd3acb9d385.
        filename (str | Unset): Filename of uploaded file or name of the link Example:
            57407b0f37e8833cc7ff34f76413885e3856336ff21a263187c6bbd3acb9d385.
        meta (FileOrLinkMeta | Unset):
        name (str | Unset): Name of that file, when it's been uploaded Example: myPicture.jpg.
    """

    domain_id: str | Unset = UNSET
    domain_type: str | Unset = UNSET
    file_url: str | Unset = UNSET
    filename: str | Unset = UNSET
    meta: FileOrLinkMeta | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_id = self.domain_id

        domain_type = self.domain_type

        file_url = self.file_url

        filename = self.filename

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_id is not UNSET:
            field_dict["domainId"] = domain_id
        if domain_type is not UNSET:
            field_dict["domainType"] = domain_type
        if file_url is not UNSET:
            field_dict["fileUrl"] = file_url
        if filename is not UNSET:
            field_dict["filename"] = filename
        if meta is not UNSET:
            field_dict["meta"] = meta
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_or_link_meta import FileOrLinkMeta

        d = dict(src_dict)
        domain_id = d.pop("domainId", UNSET)

        domain_type = d.pop("domainType", UNSET)

        file_url = d.pop("fileUrl", UNSET)

        filename = d.pop("filename", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: FileOrLinkMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = FileOrLinkMeta.from_dict(_meta)

        name = d.pop("name", UNSET)

        file_or_link = cls(
            domain_id=domain_id,
            domain_type=domain_type,
            file_url=file_url,
            filename=filename,
            meta=meta,
            name=name,
        )

        file_or_link.additional_properties = d
        return file_or_link

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
