from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTranslationKeyTranslationKeyTranslationsTranslation")


@_attrs_define
class UpdateTranslationKeyTranslationKeyTranslationsTranslation:
    """Translation object

    Attributes:
        translation (str | Unset): The translation value for the key Example: Der Titel der Personen.
        updated (datetime.datetime | None | Unset): Last updated Example: 2018-05-06T19:33:00Z.
        updated_by_church (bool | Unset): Determines if the translation was updated or created by the church Example:
            True.
    """

    translation: str | Unset = UNSET
    updated: datetime.datetime | None | Unset = UNSET
    updated_by_church: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        translation = self.translation

        updated: None | str | Unset
        if isinstance(self.updated, Unset):
            updated = UNSET
        elif isinstance(self.updated, datetime.datetime):
            updated = self.updated.isoformat()
        else:
            updated = self.updated

        updated_by_church = self.updated_by_church

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if translation is not UNSET:
            field_dict["translation"] = translation
        if updated is not UNSET:
            field_dict["updated"] = updated
        if updated_by_church is not UNSET:
            field_dict["updatedByChurch"] = updated_by_church

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        translation = d.pop("translation", UNSET)

        def _parse_updated(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_type_0 = isoparse(data)

                return updated_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated = _parse_updated(d.pop("updated", UNSET))

        updated_by_church = d.pop("updatedByChurch", UNSET)

        update_translation_key_translation_key_translations_translation = cls(
            translation=translation,
            updated=updated,
            updated_by_church=updated_by_church,
        )

        update_translation_key_translation_key_translations_translation.additional_properties = d
        return update_translation_key_translation_key_translations_translation

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
