from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.appointment_base_image_type_0_image_option import (
        AppointmentBaseImageType0ImageOption,
    )
    from ..models.appointment_base_image_type_0_meta import (
        AppointmentBaseImageType0Meta,
    )


T = TypeVar("T", bound="AppointmentBaseImageType0")


@_attrs_define
class AppointmentBaseImageType0:
    """
    Attributes:
        additional_infos (list[str]):
        domain_id (str):  Example: 1303847.
        domain_type (str):  Example: appointment_image.
        file_url (str):  Example: http://churchtools.test/?q=public/filedownload&id=6071&filename=47207ecf8417a84f836109
            4d87b8b5beabb30d7aa72fe0840861346aa9587149.
        filename (str):  Example: 47207ecf8417a84f8361094d87b8b5beabb30d7aa72fe0840861346aa9587149.
        id (int):  Example: 6071.
        image_option (AppointmentBaseImageType0ImageOption):
        image_url (str):  Example:
            http://churchtools.test/images/6071/70987c31abdea3986f69a6d601222ac9a388c36a6510564a80fae29311faec89.
        meta (AppointmentBaseImageType0Meta):  Example: {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson': {'id':
            1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        name (str):  Example: example.jpg.
        relative_url (str):  Example:
            ?q=public/filedownload&id=6071&filename=47207ecf8417a84f8361094d87b8b5beabb30d7aa72fe0840861346aa9587149.
        security_level_id (int | None):
        show_only_when_editable (bool):
        size (int | None):
        type_ (str):  Example: file.
    """

    additional_infos: list[str]
    domain_id: str
    domain_type: str
    file_url: str
    filename: str
    id: int
    image_option: AppointmentBaseImageType0ImageOption
    image_url: str
    meta: AppointmentBaseImageType0Meta
    name: str
    relative_url: str
    security_level_id: int | None
    show_only_when_editable: bool
    size: int | None
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_infos = self.additional_infos

        domain_id = self.domain_id

        domain_type = self.domain_type

        file_url = self.file_url

        filename = self.filename

        id = self.id

        image_option = self.image_option.to_dict()

        image_url = self.image_url

        meta = self.meta.to_dict()

        name = self.name

        relative_url = self.relative_url

        security_level_id: int | None
        security_level_id = self.security_level_id

        show_only_when_editable = self.show_only_when_editable

        size: int | None
        size = self.size

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "additionalInfos": additional_infos,
                "domainId": domain_id,
                "domainType": domain_type,
                "fileUrl": file_url,
                "filename": filename,
                "id": id,
                "imageOption": image_option,
                "imageUrl": image_url,
                "meta": meta,
                "name": name,
                "relativeUrl": relative_url,
                "securityLevelId": security_level_id,
                "showOnlyWhenEditable": show_only_when_editable,
                "size": size,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appointment_base_image_type_0_image_option import (
            AppointmentBaseImageType0ImageOption,
        )
        from ..models.appointment_base_image_type_0_meta import (
            AppointmentBaseImageType0Meta,
        )

        d = dict(src_dict)
        additional_infos = cast(list[str], d.pop("additionalInfos"))

        domain_id = d.pop("domainId")

        domain_type = d.pop("domainType")

        file_url = d.pop("fileUrl")

        filename = d.pop("filename")

        id = d.pop("id")

        image_option = AppointmentBaseImageType0ImageOption.from_dict(
            d.pop("imageOption")
        )

        image_url = d.pop("imageUrl")

        meta = AppointmentBaseImageType0Meta.from_dict(d.pop("meta"))

        name = d.pop("name")

        relative_url = d.pop("relativeUrl")

        def _parse_security_level_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        security_level_id = _parse_security_level_id(d.pop("securityLevelId"))

        show_only_when_editable = d.pop("showOnlyWhenEditable")

        def _parse_size(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        size = _parse_size(d.pop("size"))

        type_ = d.pop("type")

        appointment_base_image_type_0 = cls(
            additional_infos=additional_infos,
            domain_id=domain_id,
            domain_type=domain_type,
            file_url=file_url,
            filename=filename,
            id=id,
            image_option=image_option,
            image_url=image_url,
            meta=meta,
            name=name,
            relative_url=relative_url,
            security_level_id=security_level_id,
            show_only_when_editable=show_only_when_editable,
            size=size,
            type_=type_,
        )

        appointment_base_image_type_0.additional_properties = d
        return appointment_base_image_type_0

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
