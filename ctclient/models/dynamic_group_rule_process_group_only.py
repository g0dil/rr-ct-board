from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dynamic_group_rule_process_group_only_active import (
        DynamicGroupRuleProcessGroupOnlyActive,
    )
    from ..models.dynamic_group_rule_process_group_only_none import (
        DynamicGroupRuleProcessGroupOnlyNone,
    )
    from ..models.dynamic_group_rule_process_group_only_requested import (
        DynamicGroupRuleProcessGroupOnlyRequested,
    )
    from ..models.dynamic_group_rule_process_group_only_to_delete import (
        DynamicGroupRuleProcessGroupOnlyToDelete,
    )
    from ..models.dynamic_group_rule_process_group_only_waiting import (
        DynamicGroupRuleProcessGroupOnlyWaiting,
    )


T = TypeVar("T", bound="DynamicGroupRuleProcessGroupOnly")


@_attrs_define
class DynamicGroupRuleProcessGroupOnly:
    """
    Attributes:
        active (DynamicGroupRuleProcessGroupOnlyActive | Unset):
        none (DynamicGroupRuleProcessGroupOnlyNone | Unset):
        requested (DynamicGroupRuleProcessGroupOnlyRequested | Unset):
        to_delete (DynamicGroupRuleProcessGroupOnlyToDelete | Unset):
        waiting (DynamicGroupRuleProcessGroupOnlyWaiting | Unset):
    """

    active: DynamicGroupRuleProcessGroupOnlyActive | Unset = UNSET
    none: DynamicGroupRuleProcessGroupOnlyNone | Unset = UNSET
    requested: DynamicGroupRuleProcessGroupOnlyRequested | Unset = UNSET
    to_delete: DynamicGroupRuleProcessGroupOnlyToDelete | Unset = UNSET
    waiting: DynamicGroupRuleProcessGroupOnlyWaiting | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active, Unset):
            active = self.active.to_dict()

        none: dict[str, Any] | Unset = UNSET
        if not isinstance(self.none, Unset):
            none = self.none.to_dict()

        requested: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requested, Unset):
            requested = self.requested.to_dict()

        to_delete: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_delete, Unset):
            to_delete = self.to_delete.to_dict()

        waiting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.waiting, Unset):
            waiting = self.waiting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if none is not UNSET:
            field_dict["none"] = none
        if requested is not UNSET:
            field_dict["requested"] = requested
        if to_delete is not UNSET:
            field_dict["to_delete"] = to_delete
        if waiting is not UNSET:
            field_dict["waiting"] = waiting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dynamic_group_rule_process_group_only_active import (
            DynamicGroupRuleProcessGroupOnlyActive,
        )
        from ..models.dynamic_group_rule_process_group_only_none import (
            DynamicGroupRuleProcessGroupOnlyNone,
        )
        from ..models.dynamic_group_rule_process_group_only_requested import (
            DynamicGroupRuleProcessGroupOnlyRequested,
        )
        from ..models.dynamic_group_rule_process_group_only_to_delete import (
            DynamicGroupRuleProcessGroupOnlyToDelete,
        )
        from ..models.dynamic_group_rule_process_group_only_waiting import (
            DynamicGroupRuleProcessGroupOnlyWaiting,
        )

        d = dict(src_dict)
        _active = d.pop("active", UNSET)
        active: DynamicGroupRuleProcessGroupOnlyActive | Unset
        if isinstance(_active, Unset):
            active = UNSET
        else:
            active = DynamicGroupRuleProcessGroupOnlyActive.from_dict(_active)

        _none = d.pop("none", UNSET)
        none: DynamicGroupRuleProcessGroupOnlyNone | Unset
        if isinstance(_none, Unset):
            none = UNSET
        else:
            none = DynamicGroupRuleProcessGroupOnlyNone.from_dict(_none)

        _requested = d.pop("requested", UNSET)
        requested: DynamicGroupRuleProcessGroupOnlyRequested | Unset
        if isinstance(_requested, Unset):
            requested = UNSET
        else:
            requested = DynamicGroupRuleProcessGroupOnlyRequested.from_dict(_requested)

        _to_delete = d.pop("to_delete", UNSET)
        to_delete: DynamicGroupRuleProcessGroupOnlyToDelete | Unset
        if isinstance(_to_delete, Unset):
            to_delete = UNSET
        else:
            to_delete = DynamicGroupRuleProcessGroupOnlyToDelete.from_dict(_to_delete)

        _waiting = d.pop("waiting", UNSET)
        waiting: DynamicGroupRuleProcessGroupOnlyWaiting | Unset
        if isinstance(_waiting, Unset):
            waiting = UNSET
        else:
            waiting = DynamicGroupRuleProcessGroupOnlyWaiting.from_dict(_waiting)

        dynamic_group_rule_process_group_only = cls(
            active=active,
            none=none,
            requested=requested,
            to_delete=to_delete,
            waiting=waiting,
        )

        dynamic_group_rule_process_group_only.additional_properties = d
        return dynamic_group_rule_process_group_only

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
