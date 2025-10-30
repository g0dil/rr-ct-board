from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateGroupResponse201DataRolesItem")


@_attrs_define
class DuplicateGroupResponse201DataRolesItem:
    """
    Attributes:
        can_read_chat (bool):
        can_write_chat (bool):
        counts_towards_seats (bool):
        force_two_factor_auth (bool):
        group_type_role_id (int):
        is_active (bool):
        receive_qr_code (bool):
        html_template_ids (list[int] | None | Unset):
    """

    can_read_chat: bool
    can_write_chat: bool
    counts_towards_seats: bool
    force_two_factor_auth: bool
    group_type_role_id: int
    is_active: bool
    receive_qr_code: bool
    html_template_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_read_chat = self.can_read_chat

        can_write_chat = self.can_write_chat

        counts_towards_seats = self.counts_towards_seats

        force_two_factor_auth = self.force_two_factor_auth

        group_type_role_id = self.group_type_role_id

        is_active = self.is_active

        receive_qr_code = self.receive_qr_code

        html_template_ids: list[int] | None | Unset
        if isinstance(self.html_template_ids, Unset):
            html_template_ids = UNSET
        elif isinstance(self.html_template_ids, list):
            html_template_ids = self.html_template_ids

        else:
            html_template_ids = self.html_template_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canReadChat": can_read_chat,
                "canWriteChat": can_write_chat,
                "countsTowardsSeats": counts_towards_seats,
                "forceTwoFactorAuth": force_two_factor_auth,
                "groupTypeRoleId": group_type_role_id,
                "isActive": is_active,
                "receiveQRCode": receive_qr_code,
            }
        )
        if html_template_ids is not UNSET:
            field_dict["htmlTemplateIds"] = html_template_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_read_chat = d.pop("canReadChat")

        can_write_chat = d.pop("canWriteChat")

        counts_towards_seats = d.pop("countsTowardsSeats")

        force_two_factor_auth = d.pop("forceTwoFactorAuth")

        group_type_role_id = d.pop("groupTypeRoleId")

        is_active = d.pop("isActive")

        receive_qr_code = d.pop("receiveQRCode")

        def _parse_html_template_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                html_template_ids_type_0 = cast(list[int], data)

                return html_template_ids_type_0
            except:  # noqa: E722
                pass
            return cast(list[int] | None | Unset, data)

        html_template_ids = _parse_html_template_ids(d.pop("htmlTemplateIds", UNSET))

        duplicate_group_response_201_data_roles_item = cls(
            can_read_chat=can_read_chat,
            can_write_chat=can_write_chat,
            counts_towards_seats=counts_towards_seats,
            force_two_factor_auth=force_two_factor_auth,
            group_type_role_id=group_type_role_id,
            is_active=is_active,
            receive_qr_code=receive_qr_code,
            html_template_ids=html_template_ids,
        )

        duplicate_group_response_201_data_roles_item.additional_properties = d
        return duplicate_group_response_201_data_roles_item

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
