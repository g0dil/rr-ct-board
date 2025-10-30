from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.privacy_policy_owner import PrivacyPolicyOwner
    from ..models.privacy_policy_relationships_item import (
        PrivacyPolicyRelationshipsItem,
    )


T = TypeVar("T", bound="PrivacyPolicy")


@_attrs_define
class PrivacyPolicy:
    """
    Attributes:
        owner (PrivacyPolicyOwner):
        relationships (list[PrivacyPolicyRelationshipsItem]):
        show_banner (bool):
        text (str):
        text_relations (str):
        type_id (int):
        who_id (int):
    """

    owner: PrivacyPolicyOwner
    relationships: list[PrivacyPolicyRelationshipsItem]
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
        from ..models.privacy_policy_owner import PrivacyPolicyOwner
        from ..models.privacy_policy_relationships_item import (
            PrivacyPolicyRelationshipsItem,
        )

        d = dict(src_dict)
        owner = PrivacyPolicyOwner.from_dict(d.pop("owner"))

        relationships = []
        _relationships = d.pop("relationships")
        for relationships_item_data in _relationships:
            relationships_item = PrivacyPolicyRelationshipsItem.from_dict(
                relationships_item_data
            )

            relationships.append(relationships_item)

        show_banner = d.pop("showBanner")

        text = d.pop("text")

        text_relations = d.pop("textRelations")

        type_id = d.pop("typeId")

        who_id = d.pop("whoId")

        privacy_policy = cls(
            owner=owner,
            relationships=relationships,
            show_banner=show_banner,
            text=text,
            text_relations=text_relations,
            type_id=type_id,
            who_id=who_id,
        )

        privacy_policy.additional_properties = d
        return privacy_policy

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
