from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_facts_body_field_type import PostFactsBodyFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFactsBody")


@_attrs_define
class PostFactsBody:
    """
    Attributes:
        field_type (PostFactsBodyFieldType | Unset):
        name (str | Unset):
        options (list[Any] | Unset): Will not be saved if fieldType = number
        sort_key (int | Unset):
    """

    field_type: PostFactsBodyFieldType | Unset = UNSET
    name: str | Unset = UNSET
    options: list[Any] | Unset = UNSET
    sort_key: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_type: str | Unset = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        name = self.name

        options: list[Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        sort_key = self.sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if name is not UNSET:
            field_dict["name"] = name
        if options is not UNSET:
            field_dict["options"] = options
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _field_type = d.pop("fieldType", UNSET)
        field_type: PostFactsBodyFieldType | Unset
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = PostFactsBodyFieldType(_field_type)

        name = d.pop("name", UNSET)

        options = cast(list[Any], d.pop("options", UNSET))

        sort_key = d.pop("sortKey", UNSET)

        post_facts_body = cls(
            field_type=field_type,
            name=name,
            options=options,
            sort_key=sort_key,
        )

        post_facts_body.additional_properties = d
        return post_facts_body

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
