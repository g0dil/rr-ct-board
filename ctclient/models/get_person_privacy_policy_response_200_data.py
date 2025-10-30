from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_person_privacy_policy_response_200_data_owner import (
        GetPersonPrivacyPolicyResponse200DataOwner,
    )
    from ..models.get_person_privacy_policy_response_200_data_relationships_item import (
        GetPersonPrivacyPolicyResponse200DataRelationshipsItem,
    )


T = TypeVar("T", bound="GetPersonPrivacyPolicyResponse200Data")


@_attrs_define
class GetPersonPrivacyPolicyResponse200Data:
    """
    Attributes:
        owner (GetPersonPrivacyPolicyResponse200DataOwner):
        relationships (list[GetPersonPrivacyPolicyResponse200DataRelationshipsItem]):
        show_banner (bool):
        text (str):
        text_relations (str):
        type_id (int):
        who_id (int):
    """

    owner: GetPersonPrivacyPolicyResponse200DataOwner
    relationships: list[GetPersonPrivacyPolicyResponse200DataRelationshipsItem]
    show_banner: bool
    text: str
    text_relations: str
    type_id: int
    who_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner = self.owner.to_dict()

        relationships = []
        for relationships_item_data in self.relationships:
            relationships_item = relationships_item_data.to_dict()
            relationships.append(relationships_item)

        show_banner = self.show_banner

        text = self.text

        text_relations = self.text_relations

        type_id = self.type_id

        who_id = self.who_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "relationships": relationships,
                "showBanner": show_banner,
                "text": text,
                "textRelations": text_relations,
                "typeId": type_id,
                "whoId": who_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_person_privacy_policy_response_200_data_owner import (
            GetPersonPrivacyPolicyResponse200DataOwner,
        )
        from ..models.get_person_privacy_policy_response_200_data_relationships_item import (
            GetPersonPrivacyPolicyResponse200DataRelationshipsItem,
        )

        d = dict(src_dict)
        owner = GetPersonPrivacyPolicyResponse200DataOwner.from_dict(d.pop("owner"))

        relationships = []
        _relationships = d.pop("relationships")
        for relationships_item_data in _relationships:
            relationships_item = (
                GetPersonPrivacyPolicyResponse200DataRelationshipsItem.from_dict(
                    relationships_item_data
                )
            )

            relationships.append(relationships_item)

        show_banner = d.pop("showBanner")

        text = d.pop("text")

        text_relations = d.pop("textRelations")

        type_id = d.pop("typeId")

        who_id = d.pop("whoId")

        get_person_privacy_policy_response_200_data = cls(
            owner=owner,
            relationships=relationships,
            show_banner=show_banner,
            text=text,
            text_relations=text_relations,
            type_id=type_id,
            who_id=who_id,
        )

        get_person_privacy_policy_response_200_data.additional_properties = d
        return get_person_privacy_policy_response_200_data

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
