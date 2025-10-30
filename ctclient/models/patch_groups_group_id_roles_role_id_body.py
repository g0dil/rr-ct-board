from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchGroupsGroupIdRolesRoleIdBody")


@_attrs_define
class PatchGroupsGroupIdRolesRoleIdBody:
    """
    Attributes:
        can_read_chat (bool | Unset):
        can_write_chat (bool | Unset):
        counts_towards_seats (bool | Unset):
        force_two_factor_auth (bool | Unset):
        grow_path_id (int | None | Unset):
        html_template_ids (list[int] | Unset):
        is_active (bool | Unset):
        receive_qr_code (bool | Unset):
    """

    can_read_chat: bool | Unset = UNSET
    can_write_chat: bool | Unset = UNSET
    counts_towards_seats: bool | Unset = UNSET
    force_two_factor_auth: bool | Unset = UNSET
    grow_path_id: int | None | Unset = UNSET
    html_template_ids: list[int] | Unset = UNSET
    is_active: bool | Unset = UNSET
    receive_qr_code: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_read_chat = self.can_read_chat

        can_write_chat = self.can_write_chat

        counts_towards_seats = self.counts_towards_seats

        force_two_factor_auth = self.force_two_factor_auth

        grow_path_id: int | None | Unset
        if isinstance(self.grow_path_id, Unset):
            grow_path_id = UNSET
        else:
            grow_path_id = self.grow_path_id

        html_template_ids: list[int] | Unset = UNSET
        if not isinstance(self.html_template_ids, Unset):
            html_template_ids = self.html_template_ids

        is_active = self.is_active

        receive_qr_code = self.receive_qr_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_read_chat is not UNSET:
            field_dict["canReadChat"] = can_read_chat
        if can_write_chat is not UNSET:
            field_dict["canWriteChat"] = can_write_chat
        if counts_towards_seats is not UNSET:
            field_dict["countsTowardsSeats"] = counts_towards_seats
        if force_two_factor_auth is not UNSET:
            field_dict["forceTwoFactorAuth"] = force_two_factor_auth
        if grow_path_id is not UNSET:
            field_dict["growPathId"] = grow_path_id
        if html_template_ids is not UNSET:
            field_dict["htmlTemplateIds"] = html_template_ids
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if receive_qr_code is not UNSET:
            field_dict["receiveQRCode"] = receive_qr_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_read_chat = d.pop("canReadChat", UNSET)

        can_write_chat = d.pop("canWriteChat", UNSET)

        counts_towards_seats = d.pop("countsTowardsSeats", UNSET)

        force_two_factor_auth = d.pop("forceTwoFactorAuth", UNSET)

        def _parse_grow_path_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        grow_path_id = _parse_grow_path_id(d.pop("growPathId", UNSET))

        html_template_ids = cast(list[int], d.pop("htmlTemplateIds", UNSET))

        is_active = d.pop("isActive", UNSET)

        receive_qr_code = d.pop("receiveQRCode", UNSET)

        patch_groups_group_id_roles_role_id_body = cls(
            can_read_chat=can_read_chat,
            can_write_chat=can_write_chat,
            counts_towards_seats=counts_towards_seats,
            force_two_factor_auth=force_two_factor_auth,
            grow_path_id=grow_path_id,
            html_template_ids=html_template_ids,
            is_active=is_active,
            receive_qr_code=receive_qr_code,
        )

        patch_groups_group_id_roles_role_id_body.additional_properties = d
        return patch_groups_group_id_roles_role_id_body

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
