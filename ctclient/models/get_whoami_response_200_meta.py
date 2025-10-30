from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWhoamiResponse200Meta")


@_attrs_define
class GetWhoamiResponse200Meta:
    """
    Attributes:
        simulating_user_id (int | None | Unset):
    """

    simulating_user_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        simulating_user_id: int | None | Unset
        if isinstance(self.simulating_user_id, Unset):
            simulating_user_id = UNSET
        else:
            simulating_user_id = self.simulating_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if simulating_user_id is not UNSET:
            field_dict["simulatingUserId"] = simulating_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_simulating_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        simulating_user_id = _parse_simulating_user_id(d.pop("simulatingUserId", UNSET))

        get_whoami_response_200_meta = cls(
            simulating_user_id=simulating_user_id,
        )

        get_whoami_response_200_meta.additional_properties = d
        return get_whoami_response_200_meta

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
