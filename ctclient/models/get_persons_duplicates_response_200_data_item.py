from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_persons_duplicates_response_200_data_item_relationships_item import (
        GetPersonsDuplicatesResponse200DataItemRelationshipsItem,
    )


T = TypeVar("T", bound="GetPersonsDuplicatesResponse200DataItem")


@_attrs_define
class GetPersonsDuplicatesResponse200DataItem:
    """
    Attributes:
        relationship_type_id (int | None):
        relationships (list[GetPersonsDuplicatesResponse200DataItemRelationshipsItem]):
    """

    relationship_type_id: int | None
    relationships: list[GetPersonsDuplicatesResponse200DataItemRelationshipsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relationship_type_id: int | None
        relationship_type_id = self.relationship_type_id

        relationships = []
        for relationships_item_data in self.relationships:
            relationships_item = relationships_item_data.to_dict()
            relationships.append(relationships_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relationshipTypeId": relationship_type_id,
                "relationships": relationships,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_persons_duplicates_response_200_data_item_relationships_item import (
            GetPersonsDuplicatesResponse200DataItemRelationshipsItem,
        )

        d = dict(src_dict)

        def _parse_relationship_type_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        relationship_type_id = _parse_relationship_type_id(d.pop("relationshipTypeId"))

        relationships = []
        _relationships = d.pop("relationships")
        for relationships_item_data in _relationships:
            relationships_item = (
                GetPersonsDuplicatesResponse200DataItemRelationshipsItem.from_dict(
                    relationships_item_data
                )
            )

            relationships.append(relationships_item)

        get_persons_duplicates_response_200_data_item = cls(
            relationship_type_id=relationship_type_id,
            relationships=relationships,
        )

        get_persons_duplicates_response_200_data_item.additional_properties = d
        return get_persons_duplicates_response_200_data_item

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
