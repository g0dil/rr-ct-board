from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.meeting_template_field_type import MeetingTemplateFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MeetingTemplateField")


@_attrs_define
class MeetingTemplateField:
    """
    Attributes:
        label (str):
        type_ (MeetingTemplateFieldType):  Example: color.
        options (list[str] | None | str | Unset):
        value (None | str | Unset):
    """

    label: str
    type_: MeetingTemplateFieldType
    options: list[str] | None | str | Unset = UNSET
    value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        type_ = self.type_.value

        options: list[str] | None | str | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = self.options

        else:
            options = self.options

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "type": type_,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        type_ = MeetingTemplateFieldType(d.pop("type"))

        def _parse_options(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_1_type_0 = cast(list[str], data)

                return options_type_1_type_0
            except:  # noqa: E722
                pass
            return cast(list[str] | None | str | Unset, data)

        options = _parse_options(d.pop("options", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        meeting_template_field = cls(
            label=label,
            type_=type_,
            options=options,
            value=value,
        )

        meeting_template_field.additional_properties = d
        return meeting_template_field

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
