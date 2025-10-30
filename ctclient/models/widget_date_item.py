from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget_date_item_action_data import WidgetDateItemActionData
    from ..models.widget_date_item_details import WidgetDateItemDetails
    from ..models.widget_date_item_infos_item import WidgetDateItemInfosItem
    from ..models.widget_date_item_widget_item_action import (
        WidgetDateItemWidgetItemAction,
    )


T = TypeVar("T", bound="WidgetDateItem")


@_attrs_define
class WidgetDateItem:
    """Item for widget date lists

    Attributes:
        action_data (WidgetDateItemActionData):
        actions (list[WidgetDateItemWidgetItemAction]):
        details (WidgetDateItemDetails):
        infos (list[WidgetDateItemInfosItem]):
        title (str):  Example: Gottesdienst.
        filter_keys (None | Unset):
        summary_text (str | Unset):  Example: 20.07.2022.
    """

    action_data: WidgetDateItemActionData
    actions: list[WidgetDateItemWidgetItemAction]
    details: WidgetDateItemDetails
    infos: list[WidgetDateItemInfosItem]
    title: str
    filter_keys: None | Unset = UNSET
    summary_text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_data = self.action_data.to_dict()

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        details = self.details.to_dict()

        infos = []
        for infos_item_data in self.infos:
            infos_item = infos_item_data.to_dict()
            infos.append(infos_item)

        title = self.title

        filter_keys = self.filter_keys

        summary_text = self.summary_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionData": action_data,
                "actions": actions,
                "details": details,
                "infos": infos,
                "title": title,
            }
        )
        if filter_keys is not UNSET:
            field_dict["filterKeys"] = filter_keys
        if summary_text is not UNSET:
            field_dict["summaryText"] = summary_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_date_item_action_data import WidgetDateItemActionData
        from ..models.widget_date_item_details import WidgetDateItemDetails
        from ..models.widget_date_item_infos_item import WidgetDateItemInfosItem
        from ..models.widget_date_item_widget_item_action import (
            WidgetDateItemWidgetItemAction,
        )

        d = dict(src_dict)
        action_data = WidgetDateItemActionData.from_dict(d.pop("actionData"))

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = WidgetDateItemWidgetItemAction.from_dict(actions_item_data)

            actions.append(actions_item)

        details = WidgetDateItemDetails.from_dict(d.pop("details"))

        infos = []
        _infos = d.pop("infos")
        for infos_item_data in _infos:
            infos_item = WidgetDateItemInfosItem.from_dict(infos_item_data)

            infos.append(infos_item)

        title = d.pop("title")

        filter_keys = d.pop("filterKeys", UNSET)

        summary_text = d.pop("summaryText", UNSET)

        widget_date_item = cls(
            action_data=action_data,
            actions=actions,
            details=details,
            infos=infos,
            title=title,
            filter_keys=filter_keys,
            summary_text=summary_text,
        )

        widget_date_item.additional_properties = d
        return widget_date_item

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
