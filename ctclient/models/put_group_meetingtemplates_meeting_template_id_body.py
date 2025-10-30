from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_group_meetingtemplates_meeting_template_id_body_template_item import (
        PutGroupMeetingtemplatesMeetingTemplateIdBodyTemplateItem,
    )


T = TypeVar("T", bound="PutGroupMeetingtemplatesMeetingTemplateIdBody")


@_attrs_define
class PutGroupMeetingtemplatesMeetingTemplateIdBody:
    """
    Attributes:
        name (str):  Example: Lowlights / Highlights.
        template (list[PutGroupMeetingtemplatesMeetingTemplateIdBodyTemplateItem]):
        id (int):  Example: 1.
    """

    name: str
    template: list[PutGroupMeetingtemplatesMeetingTemplateIdBodyTemplateItem]
    id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        template = []
        for template_item_data in self.template:
            template_item = template_item_data.to_dict()
            template.append(template_item)

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "template": template,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_group_meetingtemplates_meeting_template_id_body_template_item import (
            PutGroupMeetingtemplatesMeetingTemplateIdBodyTemplateItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        template = []
        _template = d.pop("template")
        for template_item_data in _template:
            template_item = (
                PutGroupMeetingtemplatesMeetingTemplateIdBodyTemplateItem.from_dict(
                    template_item_data
                )
            )

            template.append(template_item)

        id = d.pop("id")

        put_group_meetingtemplates_meeting_template_id_body = cls(
            name=name,
            template=template,
            id=id,
        )

        put_group_meetingtemplates_meeting_template_id_body.additional_properties = d
        return put_group_meetingtemplates_meeting_template_id_body

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
