from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.registration_config_fields_item_field import (
        RegistrationConfigFieldsItemField,
    )


T = TypeVar("T", bound="RegistrationConfigFieldsItem")


@_attrs_define
class RegistrationConfigFieldsItem:
    """
    Attributes:
        field (RegistrationConfigFieldsItemField):
        field_id (int):
        is_required (bool):
    """

    field: RegistrationConfigFieldsItemField
    field_id: int
    is_required: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field.to_dict()

        field_id = self.field_id

        is_required = self.is_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "fieldId": field_id,
                "isRequired": is_required,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registration_config_fields_item_field import (
            RegistrationConfigFieldsItemField,
        )

        d = dict(src_dict)
        field = RegistrationConfigFieldsItemField.from_dict(d.pop("field"))

        field_id = d.pop("fieldId")

        is_required = d.pop("isRequired")

        registration_config_fields_item = cls(
            field=field,
            field_id=field_id,
            is_required=is_required,
        )

        registration_config_fields_item.additional_properties = d
        return registration_config_fields_item

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
