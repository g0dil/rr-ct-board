from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_member_history_entry_origin import GroupMemberHistoryEntryOrigin
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_member_history_entry_current import (
        GroupMemberHistoryEntryCurrent,
    )
    from ..models.group_member_history_entry_meta import GroupMemberHistoryEntryMeta
    from ..models.group_member_history_entry_previous import (
        GroupMemberHistoryEntryPrevious,
    )


T = TypeVar("T", bound="GroupMemberHistoryEntry")


@_attrs_define
class GroupMemberHistoryEntry:
    """
    Attributes:
        current (GroupMemberHistoryEntryCurrent):
        group_id (int):
        id (int):
        member_id (int):
        meta (GroupMemberHistoryEntryMeta):
        previous (GroupMemberHistoryEntryPrevious):
        origin (GroupMemberHistoryEntryOrigin | Unset):
    """

    current: GroupMemberHistoryEntryCurrent
    group_id: int
    id: int
    member_id: int
    meta: GroupMemberHistoryEntryMeta
    previous: GroupMemberHistoryEntryPrevious
    origin: GroupMemberHistoryEntryOrigin | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current = self.current.to_dict()

        group_id = self.group_id

        id = self.id

        member_id = self.member_id

        meta = self.meta.to_dict()

        previous = self.previous.to_dict()

        origin: str | Unset = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current": current,
                "groupId": group_id,
                "id": id,
                "memberId": member_id,
                "meta": meta,
                "previous": previous,
            }
        )
        if origin is not UNSET:
            field_dict["origin"] = origin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_member_history_entry_current import (
            GroupMemberHistoryEntryCurrent,
        )
        from ..models.group_member_history_entry_meta import GroupMemberHistoryEntryMeta
        from ..models.group_member_history_entry_previous import (
            GroupMemberHistoryEntryPrevious,
        )

        d = dict(src_dict)
        current = GroupMemberHistoryEntryCurrent.from_dict(d.pop("current"))

        group_id = d.pop("groupId")

        id = d.pop("id")

        member_id = d.pop("memberId")

        meta = GroupMemberHistoryEntryMeta.from_dict(d.pop("meta"))

        previous = GroupMemberHistoryEntryPrevious.from_dict(d.pop("previous"))

        _origin = d.pop("origin", UNSET)
        origin: GroupMemberHistoryEntryOrigin | Unset
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = GroupMemberHistoryEntryOrigin(_origin)

        group_member_history_entry = cls(
            current=current,
            group_id=group_id,
            id=id,
            member_id=member_id,
            meta=meta,
            previous=previous,
            origin=origin,
        )

        group_member_history_entry.additional_properties = d
        return group_member_history_entry

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
