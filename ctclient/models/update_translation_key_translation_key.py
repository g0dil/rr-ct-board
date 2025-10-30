from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_translation_key_translation_key_translations import (
        UpdateTranslationKeyTranslationKeyTranslations,
    )


T = TypeVar("T", bound="UpdateTranslationKeyTranslationKey")


@_attrs_define
class UpdateTranslationKeyTranslationKey:
    """Translation key object

    Attributes:
        id (int | Unset):  Example: 42.
        key (str | Unset):  Example: person.title.
        module (str | Unset):  Example: app.
        translations (UpdateTranslationKeyTranslationKeyTranslations | Unset):
        updated (datetime.datetime | None | Unset): Last updated Example: 2018-05-06T19:33:00Z.
    """

    id: int | Unset = UNSET
    key: str | Unset = UNSET
    module: str | Unset = UNSET
    translations: UpdateTranslationKeyTranslationKeyTranslations | Unset = UNSET
    updated: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        module = self.module

        translations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.translations, Unset):
            translations = self.translations.to_dict()

        updated: None | str | Unset
        if isinstance(self.updated, Unset):
            updated = UNSET
        elif isinstance(self.updated, datetime.datetime):
            updated = self.updated.isoformat()
        else:
            updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if module is not UNSET:
            field_dict["module"] = module
        if translations is not UNSET:
            field_dict["translations"] = translations
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_translation_key_translation_key_translations import (
            UpdateTranslationKeyTranslationKeyTranslations,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        module = d.pop("module", UNSET)

        _translations = d.pop("translations", UNSET)
        translations: UpdateTranslationKeyTranslationKeyTranslations | Unset
        if isinstance(_translations, Unset):
            translations = UNSET
        else:
            translations = UpdateTranslationKeyTranslationKeyTranslations.from_dict(
                _translations
            )

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

        update_translation_key_translation_key = cls(
            id=id,
            key=key,
            module=module,
            translations=translations,
            updated=updated,
        )

        update_translation_key_translation_key.additional_properties = d
        return update_translation_key_translation_key

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
