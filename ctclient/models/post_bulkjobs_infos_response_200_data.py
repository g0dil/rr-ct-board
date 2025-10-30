from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostBulkjobsInfosResponse200Data")


@_attrs_define
class PostBulkjobsInfosResponse200Data:
    """
    Attributes:
        allowed_domain_object_identifiers (list[int | str]):
    """

    allowed_domain_object_identifiers: list[int | str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_domain_object_identifiers = []
        for (
            allowed_domain_object_identifiers_item_data
        ) in self.allowed_domain_object_identifiers:
            allowed_domain_object_identifiers_item: int | str
            allowed_domain_object_identifiers_item = (
                allowed_domain_object_identifiers_item_data
            )
            allowed_domain_object_identifiers.append(
                allowed_domain_object_identifiers_item
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowedDomainObjectIdentifiers": allowed_domain_object_identifiers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_domain_object_identifiers = []
        _allowed_domain_object_identifiers = d.pop("allowedDomainObjectIdentifiers")
        for (
            allowed_domain_object_identifiers_item_data
        ) in _allowed_domain_object_identifiers:

            def _parse_allowed_domain_object_identifiers_item(
                data: object,
            ) -> int | str:
                return cast(int | str, data)

            allowed_domain_object_identifiers_item = (
                _parse_allowed_domain_object_identifiers_item(
                    allowed_domain_object_identifiers_item_data
                )
            )

            allowed_domain_object_identifiers.append(
                allowed_domain_object_identifiers_item
            )

        post_bulkjobs_infos_response_200_data = cls(
            allowed_domain_object_identifiers=allowed_domain_object_identifiers,
        )

        post_bulkjobs_infos_response_200_data.additional_properties = d
        return post_bulkjobs_infos_response_200_data

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
