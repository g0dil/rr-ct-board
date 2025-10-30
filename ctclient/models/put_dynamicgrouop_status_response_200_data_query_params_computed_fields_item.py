from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_dynamicgrouop_status_response_200_data_query_params_computed_fields_item_value import (
        PutDynamicgrouopStatusResponse200DataQueryParamsComputedFieldsItemValue,
    )


T = TypeVar(
    "T", bound="PutDynamicgrouopStatusResponse200DataQueryParamsComputedFieldsItem"
)


@_attrs_define
class PutDynamicgrouopStatusResponse200DataQueryParamsComputedFieldsItem:
    """
    Attributes:
        name (str | Unset):
        value (PutDynamicgrouopStatusResponse200DataQueryParamsComputedFieldsItemValue | Unset):
    """

    name: str | Unset = UNSET
    value: (
        PutDynamicgrouopStatusResponse200DataQueryParamsComputedFieldsItemValue | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_dynamicgrouop_status_response_200_data_query_params_computed_fields_item_value import (
            PutDynamicgrouopStatusResponse200DataQueryParamsComputedFieldsItemValue,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _value = d.pop("value", UNSET)
        value: (
            PutDynamicgrouopStatusResponse200DataQueryParamsComputedFieldsItemValue
            | Unset
        )
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = PutDynamicgrouopStatusResponse200DataQueryParamsComputedFieldsItemValue.from_dict(
                _value
            )

        put_dynamicgrouop_status_response_200_data_query_params_computed_fields_item = (
            cls(
                name=name,
                value=value,
            )
        )

        put_dynamicgrouop_status_response_200_data_query_params_computed_fields_item.additional_properties = d
        return (
            put_dynamicgrouop_status_response_200_data_query_params_computed_fields_item
        )

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
