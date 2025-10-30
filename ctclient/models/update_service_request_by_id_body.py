from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateServiceRequestByIdBody")


@_attrs_define
class UpdateServiceRequestByIdBody:
    """
    Example:
        {'agreed': True, 'comment': ''}

    Attributes:
        agreed (bool | Unset): Only true is allowed when updating.
        comment (str | Unset):
    """

    agreed: bool | Unset = UNSET
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agreed = self.agreed

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agreed is not UNSET:
            field_dict["agreed"] = agreed
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agreed = d.pop("agreed", UNSET)

        comment = d.pop("comment", UNSET)

        update_service_request_by_id_body = cls(
            agreed=agreed,
            comment=comment,
        )

        update_service_request_by_id_body.additional_properties = d
        return update_service_request_by_id_body

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
