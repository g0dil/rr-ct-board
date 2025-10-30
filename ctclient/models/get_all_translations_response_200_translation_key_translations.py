from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_all_translations_response_200_translation_key_translations_translation import (
        GetAllTranslationsResponse200TranslationKeyTranslationsTranslation,
    )


T = TypeVar("T", bound="GetAllTranslationsResponse200TranslationKeyTranslations")


@_attrs_define
class GetAllTranslationsResponse200TranslationKeyTranslations:
    """
    Attributes:
        additional_properties (GetAllTranslationsResponse200TranslationKeyTranslationsTranslation | Unset): Translation
            object
    """

    additional_properties: (
        GetAllTranslationsResponse200TranslationKeyTranslationsTranslation | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_properties, Unset):
            additional_properties = self.additional_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_properties is not UNSET:
            field_dict["additionalProperties"] = additional_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_all_translations_response_200_translation_key_translations_translation import (
            GetAllTranslationsResponse200TranslationKeyTranslationsTranslation,
        )

        d = dict(src_dict)
        _additional_properties = d.pop("additionalProperties", UNSET)
        additional_properties: (
            GetAllTranslationsResponse200TranslationKeyTranslationsTranslation | Unset
        )
        if isinstance(_additional_properties, Unset):
            additional_properties = UNSET
        else:
            additional_properties = GetAllTranslationsResponse200TranslationKeyTranslationsTranslation.from_dict(
                _additional_properties
            )

        get_all_translations_response_200_translation_key_translations = cls(
            additional_properties=additional_properties,
        )

        get_all_translations_response_200_translation_key_translations.additional_properties = d
        return get_all_translations_response_200_translation_key_translations

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
