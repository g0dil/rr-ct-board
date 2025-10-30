from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PersonPrivacyPolicyRelationshipsItemRelationshipType")


@_attrs_define
class PersonPrivacyPolicyRelationshipsItemRelationshipType:
    """
    Attributes:
        degree_of_relationship (str):
        relationship_name (str):
        relationship_type_id (int):
    """

    degree_of_relationship: str
    relationship_name: str
    relationship_type_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        degree_of_relationship = self.degree_of_relationship

        relationship_name = self.relationship_name

        relationship_type_id = self.relationship_type_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "degreeOfRelationship": degree_of_relationship,
                "relationshipName": relationship_name,
                "relationshipTypeId": relationship_type_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        degree_of_relationship = d.pop("degreeOfRelationship")

        relationship_name = d.pop("relationshipName")

        relationship_type_id = d.pop("relationshipTypeId")

        person_privacy_policy_relationships_item_relationship_type = cls(
            degree_of_relationship=degree_of_relationship,
            relationship_name=relationship_name,
            relationship_type_id=relationship_type_id,
        )

        person_privacy_policy_relationships_item_relationship_type.additional_properties = d
        return person_privacy_policy_relationships_item_relationship_type

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
