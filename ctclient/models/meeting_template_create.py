from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.meeting_template_create_template_item import (
        MeetingTemplateCreateTemplateItem,
    )


T = TypeVar("T", bound="MeetingTemplateCreate")


@_attrs_define
class MeetingTemplateCreate:
    """
    Attributes:
        name (str):  Example: Lowlights / Highlights.
        template (list[MeetingTemplateCreateTemplateItem]):
    """

    name: str
    template: list[MeetingTemplateCreateTemplateItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        template = []
        for template_item_data in self.template:
            template_item = template_item_data.to_dict()
            template.append(template_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "template": template,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meeting_template_create_template_item import (
            MeetingTemplateCreateTemplateItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        template = []
        _template = d.pop("template")
        for template_item_data in _template:
            template_item = MeetingTemplateCreateTemplateItem.from_dict(
                template_item_data
            )

            template.append(template_item)

        meeting_template_create = cls(
            name=name,
            template=template,
        )

        meeting_template_create.additional_properties = d
        return meeting_template_create

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
