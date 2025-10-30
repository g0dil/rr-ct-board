from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSyncLogsBodyLogsItemChangesItem")


@_attrs_define
class PostSyncLogsBodyLogsItemChangesItem:
    """
    Attributes:
        field_attribute (None | str | Unset): Secondary value for FieldName. Used for Group Roles.
        field_name (str | Unset): Name of field. Translation Key allowed
        new_value (str | Unset):
        old_value (None | str | Unset): `null` if new
    """

    field_attribute: None | str | Unset = UNSET
    field_name: str | Unset = UNSET
    new_value: str | Unset = UNSET
    old_value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_attribute: None | str | Unset
        if isinstance(self.field_attribute, Unset):
            field_attribute = UNSET
        else:
            field_attribute = self.field_attribute

        field_name = self.field_name

        new_value = self.new_value

        old_value: None | str | Unset
        if isinstance(self.old_value, Unset):
            old_value = UNSET
        else:
            old_value = self.old_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_attribute is not UNSET:
            field_dict["fieldAttribute"] = field_attribute
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if new_value is not UNSET:
            field_dict["newValue"] = new_value
        if old_value is not UNSET:
            field_dict["oldValue"] = old_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_field_attribute(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_attribute = _parse_field_attribute(d.pop("fieldAttribute", UNSET))

        field_name = d.pop("fieldName", UNSET)

        new_value = d.pop("newValue", UNSET)

        def _parse_old_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_value = _parse_old_value(d.pop("oldValue", UNSET))

        post_sync_logs_body_logs_item_changes_item = cls(
            field_attribute=field_attribute,
            field_name=field_name,
            new_value=new_value,
            old_value=old_value,
        )

        post_sync_logs_body_logs_item_changes_item.additional_properties = d
        return post_sync_logs_body_logs_item_changes_item

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
