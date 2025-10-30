from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_object_image_meta import DomainObjectImageMeta


T = TypeVar("T", bound="DomainObjectImage")


@_attrs_define
class DomainObjectImage:
    """
    Attributes:
        additional_infos (list[str] | Unset):
        api_url (str | Unset):
        domain_id (str | Unset):
        domain_type (str | Unset):  Default: 'file'. Example: file.
        file_url (str | Unset):
        filename (str | Unset):
        frontend_url (str | Unset):
        image_url (str | Unset):
        meta (DomainObjectImageMeta | Unset):  Example: {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson': {'id':
            1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        name (str | Unset):
        relative_url (str | Unset):
        security_level_id (str | Unset):
        show_only_when_editable (bool | Unset):
        size (int | None | Unset):
    """

    additional_infos: list[str] | Unset = UNSET
    api_url: str | Unset = UNSET
    domain_id: str | Unset = UNSET
    domain_type: str | Unset = "file"
    file_url: str | Unset = UNSET
    filename: str | Unset = UNSET
    frontend_url: str | Unset = UNSET
    image_url: str | Unset = UNSET
    meta: DomainObjectImageMeta | Unset = UNSET
    name: str | Unset = UNSET
    relative_url: str | Unset = UNSET
    security_level_id: str | Unset = UNSET
    show_only_when_editable: bool | Unset = UNSET
    size: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_infos: list[str] | Unset = UNSET
        if not isinstance(self.additional_infos, Unset):
            additional_infos = self.additional_infos

        api_url = self.api_url

        domain_id = self.domain_id

        domain_type = self.domain_type

        file_url = self.file_url

        filename = self.filename

        frontend_url = self.frontend_url

        image_url = self.image_url

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        name = self.name

        relative_url = self.relative_url

        security_level_id = self.security_level_id

        show_only_when_editable = self.show_only_when_editable

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_infos is not UNSET:
            field_dict["additionalInfos"] = additional_infos
        if api_url is not UNSET:
            field_dict["apiUrl"] = api_url
        if domain_id is not UNSET:
            field_dict["domainId"] = domain_id
        if domain_type is not UNSET:
            field_dict["domainType"] = domain_type
        if file_url is not UNSET:
            field_dict["fileUrl"] = file_url
        if filename is not UNSET:
            field_dict["filename"] = filename
        if frontend_url is not UNSET:
            field_dict["frontendUrl"] = frontend_url
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if meta is not UNSET:
            field_dict["meta"] = meta
        if name is not UNSET:
            field_dict["name"] = name
        if relative_url is not UNSET:
            field_dict["relativeUrl"] = relative_url
        if security_level_id is not UNSET:
            field_dict["securityLevelId"] = security_level_id
        if show_only_when_editable is not UNSET:
            field_dict["showOnlyWhenEditable"] = show_only_when_editable
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_object_image_meta import DomainObjectImageMeta

        d = dict(src_dict)
        additional_infos = cast(list[str], d.pop("additionalInfos", UNSET))

        api_url = d.pop("apiUrl", UNSET)

        domain_id = d.pop("domainId", UNSET)

        domain_type = d.pop("domainType", UNSET)

        file_url = d.pop("fileUrl", UNSET)

        filename = d.pop("filename", UNSET)

        frontend_url = d.pop("frontendUrl", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: DomainObjectImageMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = DomainObjectImageMeta.from_dict(_meta)

        name = d.pop("name", UNSET)

        relative_url = d.pop("relativeUrl", UNSET)

        security_level_id = d.pop("securityLevelId", UNSET)

        show_only_when_editable = d.pop("showOnlyWhenEditable", UNSET)

        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        domain_object_image = cls(
            additional_infos=additional_infos,
            api_url=api_url,
            domain_id=domain_id,
            domain_type=domain_type,
            file_url=file_url,
            filename=filename,
            frontend_url=frontend_url,
            image_url=image_url,
            meta=meta,
            name=name,
            relative_url=relative_url,
            security_level_id=security_level_id,
            show_only_when_editable=show_only_when_editable,
            size=size,
        )

        domain_object_image.additional_properties = d
        return domain_object_image

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
