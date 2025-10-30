from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.permission_domain_type import PermissionDomainType
from ..models.permission_type import PermissionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permission_meta import PermissionMeta


T = TypeVar("T", bound="Permission")


@_attrs_define
class Permission:
    """
    Attributes:
        auth_id (int | Unset):
        data_id (int | None | Unset):
        domain_id (int | Unset):
        domain_type (PermissionDomainType | Unset):
        is_inherited (bool | Unset):
        meta (PermissionMeta | Unset):
        reason (None | str | Unset):
        type_ (PermissionType | Unset):
    """

    auth_id: int | Unset = UNSET
    data_id: int | None | Unset = UNSET
    domain_id: int | Unset = UNSET
    domain_type: PermissionDomainType | Unset = UNSET
    is_inherited: bool | Unset = UNSET
    meta: PermissionMeta | Unset = UNSET
    reason: None | str | Unset = UNSET
    type_: PermissionType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_id = self.auth_id

        data_id: int | None | Unset
        if isinstance(self.data_id, Unset):
            data_id = UNSET
        else:
            data_id = self.data_id

        domain_id = self.domain_id

        domain_type: str | Unset = UNSET
        if not isinstance(self.domain_type, Unset):
            domain_type = self.domain_type.value

        is_inherited = self.is_inherited

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_id is not UNSET:
            field_dict["authId"] = auth_id
        if data_id is not UNSET:
            field_dict["dataId"] = data_id
        if domain_id is not UNSET:
            field_dict["domainId"] = domain_id
        if domain_type is not UNSET:
            field_dict["domainType"] = domain_type
        if is_inherited is not UNSET:
            field_dict["isInherited"] = is_inherited
        if meta is not UNSET:
            field_dict["meta"] = meta
        if reason is not UNSET:
            field_dict["reason"] = reason
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_meta import PermissionMeta

        d = dict(src_dict)
        auth_id = d.pop("authId", UNSET)

        def _parse_data_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        data_id = _parse_data_id(d.pop("dataId", UNSET))

        domain_id = d.pop("domainId", UNSET)

        _domain_type = d.pop("domainType", UNSET)
        domain_type: PermissionDomainType | Unset
        if isinstance(_domain_type, Unset):
            domain_type = UNSET
        else:
            domain_type = PermissionDomainType(_domain_type)

        is_inherited = d.pop("isInherited", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: PermissionMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = PermissionMeta.from_dict(_meta)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: PermissionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PermissionType(_type_)

        permission = cls(
            auth_id=auth_id,
            data_id=data_id,
            domain_id=domain_id,
            domain_type=domain_type,
            is_inherited=is_inherited,
            meta=meta,
            reason=reason,
            type_=type_,
        )

        permission.additional_properties = d
        return permission

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
