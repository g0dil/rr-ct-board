from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_person_privacy_policy_response_200_data_relationships_item_relationship_type import (
        GetPersonPrivacyPolicyResponse200DataRelationshipsItemRelationshipType,
    )


T = TypeVar("T", bound="GetPersonPrivacyPolicyResponse200DataRelationshipsItem")


@_attrs_define
class GetPersonPrivacyPolicyResponse200DataRelationshipsItem:
    """
    Attributes:
        accepted (bool):
        accepted_type (str):
        age (int):
        allowed_to_accept (bool):
        allowed_to_decline (bool):
        edit_birthday (bool):
        first_name (str):
        guid (str):
        id (int):
        last_name (str):
        accepted_date (str | Unset):
        accepted_who (int | Unset):
        image (str | Unset):
        relationship_type (GetPersonPrivacyPolicyResponse200DataRelationshipsItemRelationshipType | Unset):
    """

    accepted: bool
    accepted_type: str
    age: int
    allowed_to_accept: bool
    allowed_to_decline: bool
    edit_birthday: bool
    first_name: str
    guid: str
    id: int
    last_name: str
    accepted_date: str | Unset = UNSET
    accepted_who: int | Unset = UNSET
    image: str | Unset = UNSET
    relationship_type: (
        GetPersonPrivacyPolicyResponse200DataRelationshipsItemRelationshipType | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        accepted_type = self.accepted_type

        age = self.age

        allowed_to_accept = self.allowed_to_accept

        allowed_to_decline = self.allowed_to_decline

        edit_birthday = self.edit_birthday

        first_name = self.first_name

        guid = self.guid

        id = self.id

        last_name = self.last_name

        accepted_date = self.accepted_date

        accepted_who = self.accepted_who

        image = self.image

        relationship_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relationship_type, Unset):
            relationship_type = self.relationship_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted": accepted,
                "acceptedType": accepted_type,
                "age": age,
                "allowedToAccept": allowed_to_accept,
                "allowedToDecline": allowed_to_decline,
                "editBirthday": edit_birthday,
                "firstName": first_name,
                "guid": guid,
                "id": id,
                "lastName": last_name,
            }
        )
        if accepted_date is not UNSET:
            field_dict["acceptedDate"] = accepted_date
        if accepted_who is not UNSET:
            field_dict["acceptedWho"] = accepted_who
        if image is not UNSET:
            field_dict["image"] = image
        if relationship_type is not UNSET:
            field_dict["relationshipType"] = relationship_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_person_privacy_policy_response_200_data_relationships_item_relationship_type import (
            GetPersonPrivacyPolicyResponse200DataRelationshipsItemRelationshipType,
        )

        d = dict(src_dict)
        accepted = d.pop("accepted")

        accepted_type = d.pop("acceptedType")

        age = d.pop("age")

        allowed_to_accept = d.pop("allowedToAccept")

        allowed_to_decline = d.pop("allowedToDecline")

        edit_birthday = d.pop("editBirthday")

        first_name = d.pop("firstName")

        guid = d.pop("guid")

        id = d.pop("id")

        last_name = d.pop("lastName")

        accepted_date = d.pop("acceptedDate", UNSET)

        accepted_who = d.pop("acceptedWho", UNSET)

        image = d.pop("image", UNSET)

        _relationship_type = d.pop("relationshipType", UNSET)
        relationship_type: (
            GetPersonPrivacyPolicyResponse200DataRelationshipsItemRelationshipType
            | Unset
        )
        if isinstance(_relationship_type, Unset):
            relationship_type = UNSET
        else:
            relationship_type = GetPersonPrivacyPolicyResponse200DataRelationshipsItemRelationshipType.from_dict(
                _relationship_type
            )

        get_person_privacy_policy_response_200_data_relationships_item = cls(
            accepted=accepted,
            accepted_type=accepted_type,
            age=age,
            allowed_to_accept=allowed_to_accept,
            allowed_to_decline=allowed_to_decline,
            edit_birthday=edit_birthday,
            first_name=first_name,
            guid=guid,
            id=id,
            last_name=last_name,
            accepted_date=accepted_date,
            accepted_who=accepted_who,
            image=image,
            relationship_type=relationship_type,
        )

        get_person_privacy_policy_response_200_data_relationships_item.additional_properties = d
        return get_person_privacy_policy_response_200_data_relationships_item

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
