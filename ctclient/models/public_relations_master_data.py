from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.public_relations_master_data_associations_item import (
        PublicRelationsMasterDataAssociationsItem,
    )
    from ..models.public_relations_master_data_denominations_item import (
        PublicRelationsMasterDataDenominationsItem,
    )
    from ..models.public_relations_master_data_group_homepages_item import (
        PublicRelationsMasterDataGroupHomepagesItem,
    )
    from ..models.public_relations_master_data_tags_item import (
        PublicRelationsMasterDataTagsItem,
    )


T = TypeVar("T", bound="PublicRelationsMasterData")


@_attrs_define
class PublicRelationsMasterData:
    """
    Attributes:
        associations (list[PublicRelationsMasterDataAssociationsItem]):
        denominations (list[PublicRelationsMasterDataDenominationsItem]):
        group_homepages (list[PublicRelationsMasterDataGroupHomepagesItem]):
        social_media (list[str]):
        tags (list[PublicRelationsMasterDataTagsItem]):
    """

    associations: list[PublicRelationsMasterDataAssociationsItem]
    denominations: list[PublicRelationsMasterDataDenominationsItem]
    group_homepages: list[PublicRelationsMasterDataGroupHomepagesItem]
    social_media: list[str]
    tags: list[PublicRelationsMasterDataTagsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associations = []
        for associations_item_data in self.associations:
            associations_item = associations_item_data.to_dict()
            associations.append(associations_item)

        denominations = []
        for denominations_item_data in self.denominations:
            denominations_item = denominations_item_data.to_dict()
            denominations.append(denominations_item)

        group_homepages = []
        for group_homepages_item_data in self.group_homepages:
            group_homepages_item = group_homepages_item_data.to_dict()
            group_homepages.append(group_homepages_item)

        social_media = self.social_media

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "associations": associations,
                "denominations": denominations,
                "groupHomepages": group_homepages,
                "socialMedia": social_media,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_relations_master_data_associations_item import (
            PublicRelationsMasterDataAssociationsItem,
        )
        from ..models.public_relations_master_data_denominations_item import (
            PublicRelationsMasterDataDenominationsItem,
        )
        from ..models.public_relations_master_data_group_homepages_item import (
            PublicRelationsMasterDataGroupHomepagesItem,
        )
        from ..models.public_relations_master_data_tags_item import (
            PublicRelationsMasterDataTagsItem,
        )

        d = dict(src_dict)
        associations = []
        _associations = d.pop("associations")
        for associations_item_data in _associations:
            associations_item = PublicRelationsMasterDataAssociationsItem.from_dict(
                associations_item_data
            )

            associations.append(associations_item)

        denominations = []
        _denominations = d.pop("denominations")
        for denominations_item_data in _denominations:
            denominations_item = PublicRelationsMasterDataDenominationsItem.from_dict(
                denominations_item_data
            )

            denominations.append(denominations_item)

        group_homepages = []
        _group_homepages = d.pop("groupHomepages")
        for group_homepages_item_data in _group_homepages:
            group_homepages_item = (
                PublicRelationsMasterDataGroupHomepagesItem.from_dict(
                    group_homepages_item_data
                )
            )

            group_homepages.append(group_homepages_item)

        social_media = cast(list[str], d.pop("socialMedia"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = PublicRelationsMasterDataTagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        public_relations_master_data = cls(
            associations=associations,
            denominations=denominations,
            group_homepages=group_homepages,
            social_media=social_media,
            tags=tags,
        )

        public_relations_master_data.additional_properties = d
        return public_relations_master_data

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
