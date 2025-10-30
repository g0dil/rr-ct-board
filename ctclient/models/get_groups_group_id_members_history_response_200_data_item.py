from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_groups_group_id_members_history_response_200_data_item_origin import (
    GetGroupsGroupIdMembersHistoryResponse200DataItemOrigin,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_groups_group_id_members_history_response_200_data_item_current import (
        GetGroupsGroupIdMembersHistoryResponse200DataItemCurrent,
    )
    from ..models.get_groups_group_id_members_history_response_200_data_item_meta import (
        GetGroupsGroupIdMembersHistoryResponse200DataItemMeta,
    )
    from ..models.get_groups_group_id_members_history_response_200_data_item_previous import (
        GetGroupsGroupIdMembersHistoryResponse200DataItemPrevious,
    )


T = TypeVar("T", bound="GetGroupsGroupIdMembersHistoryResponse200DataItem")


@_attrs_define
class GetGroupsGroupIdMembersHistoryResponse200DataItem:
    """
    Attributes:
        current (GetGroupsGroupIdMembersHistoryResponse200DataItemCurrent):
        group_id (int):
        id (int):
        member_id (int):
        meta (GetGroupsGroupIdMembersHistoryResponse200DataItemMeta):
        previous (GetGroupsGroupIdMembersHistoryResponse200DataItemPrevious):
        origin (GetGroupsGroupIdMembersHistoryResponse200DataItemOrigin | Unset):
    """

    current: GetGroupsGroupIdMembersHistoryResponse200DataItemCurrent
    group_id: int
    id: int
    member_id: int
    meta: GetGroupsGroupIdMembersHistoryResponse200DataItemMeta
    previous: GetGroupsGroupIdMembersHistoryResponse200DataItemPrevious
    origin: GetGroupsGroupIdMembersHistoryResponse200DataItemOrigin | Unset = UNSET
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
        from ..models.get_groups_group_id_members_history_response_200_data_item_current import (
            GetGroupsGroupIdMembersHistoryResponse200DataItemCurrent,
        )
        from ..models.get_groups_group_id_members_history_response_200_data_item_meta import (
            GetGroupsGroupIdMembersHistoryResponse200DataItemMeta,
        )
        from ..models.get_groups_group_id_members_history_response_200_data_item_previous import (
            GetGroupsGroupIdMembersHistoryResponse200DataItemPrevious,
        )

        d = dict(src_dict)
        current = GetGroupsGroupIdMembersHistoryResponse200DataItemCurrent.from_dict(
            d.pop("current")
        )

        group_id = d.pop("groupId")

        id = d.pop("id")

        member_id = d.pop("memberId")

        meta = GetGroupsGroupIdMembersHistoryResponse200DataItemMeta.from_dict(
            d.pop("meta")
        )

        previous = GetGroupsGroupIdMembersHistoryResponse200DataItemPrevious.from_dict(
            d.pop("previous")
        )

        _origin = d.pop("origin", UNSET)
        origin: GetGroupsGroupIdMembersHistoryResponse200DataItemOrigin | Unset
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = GetGroupsGroupIdMembersHistoryResponse200DataItemOrigin(_origin)

        get_groups_group_id_members_history_response_200_data_item = cls(
            current=current,
            group_id=group_id,
            id=id,
            member_id=member_id,
            meta=meta,
            previous=previous,
            origin=origin,
        )

        get_groups_group_id_members_history_response_200_data_item.additional_properties = d
        return get_groups_group_id_members_history_response_200_data_item

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
