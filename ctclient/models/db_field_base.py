from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DbFieldBase")


@_attrs_define
class DbFieldBase:
    """
    Attributes:
        delete_on_archive (bool):
        is_active (bool):
        is_new_person_field (bool):
        line_ending (str):
        name (str):
        security_level (int):
        sort_key (int):
        use_as_placeholder (bool):
        length (int | None | Unset):
        shorty (str | Unset):
    """

    delete_on_archive: bool
    is_active: bool
    is_new_person_field: bool
    line_ending: str
    name: str
    security_level: int
    sort_key: int
    use_as_placeholder: bool
    length: int | None | Unset = UNSET
    shorty: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_on_archive = self.delete_on_archive

        is_active = self.is_active

        is_new_person_field = self.is_new_person_field

        line_ending = self.line_ending

        name = self.name

        security_level = self.security_level

        sort_key = self.sort_key

        use_as_placeholder = self.use_as_placeholder

        length: int | None | Unset
        if isinstance(self.length, Unset):
            length = UNSET
        else:
            length = self.length

        shorty = self.shorty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deleteOnArchive": delete_on_archive,
                "isActive": is_active,
                "isNewPersonField": is_new_person_field,
                "lineEnding": line_ending,
                "name": name,
                "securityLevel": security_level,
                "sortKey": sort_key,
                "useAsPlaceholder": use_as_placeholder,
            }
        )
        if length is not UNSET:
            field_dict["length"] = length
        if shorty is not UNSET:
            field_dict["shorty"] = shorty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete_on_archive = d.pop("deleteOnArchive")

        is_active = d.pop("isActive")

        is_new_person_field = d.pop("isNewPersonField")

        line_ending = d.pop("lineEnding")

        name = d.pop("name")

        security_level = d.pop("securityLevel")

        sort_key = d.pop("sortKey")

        use_as_placeholder = d.pop("useAsPlaceholder")

        def _parse_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        length = _parse_length(d.pop("length", UNSET))

        shorty = d.pop("shorty", UNSET)

        db_field_base = cls(
            delete_on_archive=delete_on_archive,
            is_active=is_active,
            is_new_person_field=is_new_person_field,
            line_ending=line_ending,
            name=name,
            security_level=security_level,
            sort_key=sort_key,
            use_as_placeholder=use_as_placeholder,
            length=length,
            shorty=shorty,
        )

        db_field_base.additional_properties = d
        return db_field_base

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
