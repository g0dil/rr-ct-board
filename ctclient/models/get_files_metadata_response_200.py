from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFilesMetadataResponse200")


@_attrs_define
class GetFilesMetadataResponse200:
    """
    Attributes:
        bezeichnung (str | Unset):
        deletion_date (str | Unset):
        domain_id (str | Unset):
        domain_type (str | Unset):
        filename (str | Unset):
        id (str | Unset):
        image_options (str | Unset):
        modified_date (str | Unset):
        modified_pid (str | Unset):
        securitylevel_id (str | Unset):
        showonlywheneditable_yn (str | Unset):
        sortkey (str | Unset):
        url (str | Unset):
    """

    bezeichnung: str | Unset = UNSET
    deletion_date: str | Unset = UNSET
    domain_id: str | Unset = UNSET
    domain_type: str | Unset = UNSET
    filename: str | Unset = UNSET
    id: str | Unset = UNSET
    image_options: str | Unset = UNSET
    modified_date: str | Unset = UNSET
    modified_pid: str | Unset = UNSET
    securitylevel_id: str | Unset = UNSET
    showonlywheneditable_yn: str | Unset = UNSET
    sortkey: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bezeichnung = self.bezeichnung

        deletion_date = self.deletion_date

        domain_id = self.domain_id

        domain_type = self.domain_type

        filename = self.filename

        id = self.id

        image_options = self.image_options

        modified_date = self.modified_date

        modified_pid = self.modified_pid

        securitylevel_id = self.securitylevel_id

        showonlywheneditable_yn = self.showonlywheneditable_yn

        sortkey = self.sortkey

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bezeichnung is not UNSET:
            field_dict["bezeichnung"] = bezeichnung
        if deletion_date is not UNSET:
            field_dict["deletion_date"] = deletion_date
        if domain_id is not UNSET:
            field_dict["domain_id"] = domain_id
        if domain_type is not UNSET:
            field_dict["domain_type"] = domain_type
        if filename is not UNSET:
            field_dict["filename"] = filename
        if id is not UNSET:
            field_dict["id"] = id
        if image_options is not UNSET:
            field_dict["image_options"] = image_options
        if modified_date is not UNSET:
            field_dict["modified_date"] = modified_date
        if modified_pid is not UNSET:
            field_dict["modified_pid"] = modified_pid
        if securitylevel_id is not UNSET:
            field_dict["securitylevel_id"] = securitylevel_id
        if showonlywheneditable_yn is not UNSET:
            field_dict["showonlywheneditable_yn"] = showonlywheneditable_yn
        if sortkey is not UNSET:
            field_dict["sortkey"] = sortkey
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bezeichnung = d.pop("bezeichnung", UNSET)

        deletion_date = d.pop("deletion_date", UNSET)

        domain_id = d.pop("domain_id", UNSET)

        domain_type = d.pop("domain_type", UNSET)

        filename = d.pop("filename", UNSET)

        id = d.pop("id", UNSET)

        image_options = d.pop("image_options", UNSET)

        modified_date = d.pop("modified_date", UNSET)

        modified_pid = d.pop("modified_pid", UNSET)

        securitylevel_id = d.pop("securitylevel_id", UNSET)

        showonlywheneditable_yn = d.pop("showonlywheneditable_yn", UNSET)

        sortkey = d.pop("sortkey", UNSET)

        url = d.pop("url", UNSET)

        get_files_metadata_response_200 = cls(
            bezeichnung=bezeichnung,
            deletion_date=deletion_date,
            domain_id=domain_id,
            domain_type=domain_type,
            filename=filename,
            id=id,
            image_options=image_options,
            modified_date=modified_date,
            modified_pid=modified_pid,
            securitylevel_id=securitylevel_id,
            showonlywheneditable_yn=showonlywheneditable_yn,
            sortkey=sortkey,
            url=url,
        )

        get_files_metadata_response_200.additional_properties = d
        return get_files_metadata_response_200

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
