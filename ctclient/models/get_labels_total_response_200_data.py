from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_labels_total_response_200_data_ignore_address import (
        GetLabelsTotalResponse200DataIgnoreAddress,
    )
    from ..models.get_labels_total_response_200_data_only_complete_address import (
        GetLabelsTotalResponse200DataOnlyCompleteAddress,
    )


T = TypeVar("T", bound="GetLabelsTotalResponse200Data")


@_attrs_define
class GetLabelsTotalResponse200Data:
    """
    Attributes:
        ignore_address (GetLabelsTotalResponse200DataIgnoreAddress | Unset):
        only_complete_address (GetLabelsTotalResponse200DataOnlyCompleteAddress | Unset):
    """

    ignore_address: GetLabelsTotalResponse200DataIgnoreAddress | Unset = UNSET
    only_complete_address: GetLabelsTotalResponse200DataOnlyCompleteAddress | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ignore_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ignore_address, Unset):
            ignore_address = self.ignore_address.to_dict()

        only_complete_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.only_complete_address, Unset):
            only_complete_address = self.only_complete_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ignore_address is not UNSET:
            field_dict["ignoreAddress"] = ignore_address
        if only_complete_address is not UNSET:
            field_dict["onlyCompleteAddress"] = only_complete_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_labels_total_response_200_data_ignore_address import (
            GetLabelsTotalResponse200DataIgnoreAddress,
        )
        from ..models.get_labels_total_response_200_data_only_complete_address import (
            GetLabelsTotalResponse200DataOnlyCompleteAddress,
        )

        d = dict(src_dict)
        _ignore_address = d.pop("ignoreAddress", UNSET)
        ignore_address: GetLabelsTotalResponse200DataIgnoreAddress | Unset
        if isinstance(_ignore_address, Unset):
            ignore_address = UNSET
        else:
            ignore_address = GetLabelsTotalResponse200DataIgnoreAddress.from_dict(
                _ignore_address
            )

        _only_complete_address = d.pop("onlyCompleteAddress", UNSET)
        only_complete_address: GetLabelsTotalResponse200DataOnlyCompleteAddress | Unset
        if isinstance(_only_complete_address, Unset):
            only_complete_address = UNSET
        else:
            only_complete_address = (
                GetLabelsTotalResponse200DataOnlyCompleteAddress.from_dict(
                    _only_complete_address
                )
            )

        get_labels_total_response_200_data = cls(
            ignore_address=ignore_address,
            only_complete_address=only_complete_address,
        )

        get_labels_total_response_200_data.additional_properties = d
        return get_labels_total_response_200_data

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
