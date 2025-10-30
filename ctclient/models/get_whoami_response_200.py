from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_whoami_response_200_data import GetWhoamiResponse200Data
    from ..models.get_whoami_response_200_meta import GetWhoamiResponse200Meta


T = TypeVar("T", bound="GetWhoamiResponse200")


@_attrs_define
class GetWhoamiResponse200:
    """
    Attributes:
        data (GetWhoamiResponse200Data): A person object includes all fields the logged in user may see depending on the
            security level. Additional DB fields, created by the admin, are also part of the response. Those fields have the
            same name as the column name.
        meta (GetWhoamiResponse200Meta):
    """

    data: GetWhoamiResponse200Data
    meta: GetWhoamiResponse200Meta
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_whoami_response_200_data import GetWhoamiResponse200Data
        from ..models.get_whoami_response_200_meta import GetWhoamiResponse200Meta

        d = dict(src_dict)
        data = GetWhoamiResponse200Data.from_dict(d.pop("data"))

        meta = GetWhoamiResponse200Meta.from_dict(d.pop("meta"))

        get_whoami_response_200 = cls(
            data=data,
            meta=meta,
        )

        get_whoami_response_200.additional_properties = d
        return get_whoami_response_200

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
