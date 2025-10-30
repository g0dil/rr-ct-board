from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_base_empty_strategy import WidgetBaseEmptyStrategy
from ..models.widget_base_orientation import WidgetBaseOrientation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget_base_filter_type_0 import WidgetBaseFilterType0
    from ..models.widget_base_widget_action import WidgetBaseWidgetAction
    from ..models.widget_base_widget_settings_type_0 import (
        WidgetBaseWidgetSettingsType0,
    )
    from ..models.widget_base_widget_settings_type_1 import (
        WidgetBaseWidgetSettingsType1,
    )


T = TypeVar("T", bound="WidgetBase")


@_attrs_define
class WidgetBase:
    """
    Attributes:
        key (str):  Example: birthday-next.
        title (str):  Example: Geburtstage.
        widget_settings (WidgetBaseWidgetSettingsType0 | WidgetBaseWidgetSettingsType1):
        actions (list[WidgetBaseWidgetAction] | Unset):
        empty_strategy (WidgetBaseEmptyStrategy | Unset): Strategy for handling empty widget content Example: SHOW.
        empty_text (str | Unset):  Example: Keine Geburtstage in den nächsten 7 Tagen.
        filter_ (None | Unset | WidgetBaseFilterType0):
        help_link (str | Unset):  Example: https://www.church.tools.
        is_mandatory (bool | Unset):  Example: True.
        orientation (WidgetBaseOrientation | Unset):  Example: horizontal.
        replacement (str | Unset):
    """

    key: str
    title: str
    widget_settings: WidgetBaseWidgetSettingsType0 | WidgetBaseWidgetSettingsType1
    actions: list[WidgetBaseWidgetAction] | Unset = UNSET
    empty_strategy: WidgetBaseEmptyStrategy | Unset = UNSET
    empty_text: str | Unset = UNSET
    filter_: None | Unset | WidgetBaseFilterType0 = UNSET
    help_link: str | Unset = UNSET
    is_mandatory: bool | Unset = UNSET
    orientation: WidgetBaseOrientation | Unset = UNSET
    replacement: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.widget_base_filter_type_0 import WidgetBaseFilterType0
        from ..models.widget_base_widget_settings_type_0 import (
            WidgetBaseWidgetSettingsType0,
        )

        key = self.key

        title = self.title

        widget_settings: dict[str, Any]
        if isinstance(self.widget_settings, WidgetBaseWidgetSettingsType0):
            widget_settings = self.widget_settings.to_dict()
        else:
            widget_settings = self.widget_settings.to_dict()

        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        empty_strategy: str | Unset = UNSET
        if not isinstance(self.empty_strategy, Unset):
            empty_strategy = self.empty_strategy.value

        empty_text = self.empty_text

        filter_: dict[str, Any] | None | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        elif isinstance(self.filter_, WidgetBaseFilterType0):
            filter_ = self.filter_.to_dict()
        else:
            filter_ = self.filter_

        help_link = self.help_link

        is_mandatory = self.is_mandatory

        orientation: str | Unset = UNSET
        if not isinstance(self.orientation, Unset):
            orientation = self.orientation.value

        replacement = self.replacement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "title": title,
                "widgetSettings": widget_settings,
            }
        )
        if actions is not UNSET:
            field_dict["actions"] = actions
        if empty_strategy is not UNSET:
            field_dict["emptyStrategy"] = empty_strategy
        if empty_text is not UNSET:
            field_dict["emptyText"] = empty_text
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if help_link is not UNSET:
            field_dict["helpLink"] = help_link
        if is_mandatory is not UNSET:
            field_dict["isMandatory"] = is_mandatory
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if replacement is not UNSET:
            field_dict["replacement"] = replacement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_base_filter_type_0 import WidgetBaseFilterType0
        from ..models.widget_base_widget_action import WidgetBaseWidgetAction
        from ..models.widget_base_widget_settings_type_0 import (
            WidgetBaseWidgetSettingsType0,
        )
        from ..models.widget_base_widget_settings_type_1 import (
            WidgetBaseWidgetSettingsType1,
        )

        d = dict(src_dict)
        key = d.pop("key")

        title = d.pop("title")

        def _parse_widget_settings(
            data: object,
        ) -> WidgetBaseWidgetSettingsType0 | WidgetBaseWidgetSettingsType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                widget_settings_type_0 = WidgetBaseWidgetSettingsType0.from_dict(data)

                return widget_settings_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            widget_settings_type_1 = WidgetBaseWidgetSettingsType1.from_dict(data)

            return widget_settings_type_1

        widget_settings = _parse_widget_settings(d.pop("widgetSettings"))

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = WidgetBaseWidgetAction.from_dict(actions_item_data)

            actions.append(actions_item)

        _empty_strategy = d.pop("emptyStrategy", UNSET)
        empty_strategy: WidgetBaseEmptyStrategy | Unset
        if isinstance(_empty_strategy, Unset):
            empty_strategy = UNSET
        else:
            empty_strategy = WidgetBaseEmptyStrategy(_empty_strategy)

        empty_text = d.pop("emptyText", UNSET)

        def _parse_filter_(data: object) -> None | Unset | WidgetBaseFilterType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_type_0 = WidgetBaseFilterType0.from_dict(data)

                return filter_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | WidgetBaseFilterType0, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        help_link = d.pop("helpLink", UNSET)

        is_mandatory = d.pop("isMandatory", UNSET)

        _orientation = d.pop("orientation", UNSET)
        orientation: WidgetBaseOrientation | Unset
        if isinstance(_orientation, Unset):
            orientation = UNSET
        else:
            orientation = WidgetBaseOrientation(_orientation)

        replacement = d.pop("replacement", UNSET)

        widget_base = cls(
            key=key,
            title=title,
            widget_settings=widget_settings,
            actions=actions,
            empty_strategy=empty_strategy,
            empty_text=empty_text,
            filter_=filter_,
            help_link=help_link,
            is_mandatory=is_mandatory,
            orientation=orientation,
            replacement=replacement,
        )

        widget_base.additional_properties = d
        return widget_base

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
