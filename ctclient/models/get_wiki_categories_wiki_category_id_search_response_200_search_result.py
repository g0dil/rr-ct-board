from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wiki_categories_wiki_category_id_search_response_200_search_result_domain_attributes import (
        GetWikiCategoriesWikiCategoryIdSearchResponse200SearchResultDomainAttributes,
    )


T = TypeVar("T", bound="GetWikiCategoriesWikiCategoryIdSearchResponse200SearchResult")


@_attrs_define
class GetWikiCategoriesWikiCategoryIdSearchResponse200SearchResult:
    """
    Attributes:
        api_url (str | Unset):  Example:
            http://churchtools.test/api/wiki/categories/0/pages/014CE18E-B72D-4511-81D4-ED12B6DD5770/versions/7.
        domain_attributes (GetWikiCategoriesWikiCategoryIdSearchResponse200SearchResultDomainAttributes | Unset):
        domain_identifier (str | Unset):  Example: 014CE18E-B72D-4511-81D4-ED12B6DD5770.
        domain_type (str | Unset):  Example: wiki_page.
        frontend_url (str | Unset):  Example:
            http://churchtools.test/?q=churchwiki#WikiView/filterWikicategory_id:0/doc:main.
        image_url (None | str | Unset):
        preview (None | str | Unset):  Example: Was ist das **Wiki**? Das Wiki soll als Dokumentation, Informations- und
            Arbeitsgrundlage für die verschiedenen Dienstb….
        title (str | Unset):  Example: main.
    """

    api_url: str | Unset = UNSET
    domain_attributes: (
        GetWikiCategoriesWikiCategoryIdSearchResponse200SearchResultDomainAttributes
        | Unset
    ) = UNSET
    domain_identifier: str | Unset = UNSET
    domain_type: str | Unset = UNSET
    frontend_url: str | Unset = UNSET
    image_url: None | str | Unset = UNSET
    preview: None | str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_url = self.api_url

        domain_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain_attributes, Unset):
            domain_attributes = self.domain_attributes.to_dict()

        domain_identifier = self.domain_identifier

        domain_type = self.domain_type

        frontend_url = self.frontend_url

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        preview: None | str | Unset
        if isinstance(self.preview, Unset):
            preview = UNSET
        else:
            preview = self.preview

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_url is not UNSET:
            field_dict["apiUrl"] = api_url
        if domain_attributes is not UNSET:
            field_dict["domainAttributes"] = domain_attributes
        if domain_identifier is not UNSET:
            field_dict["domainIdentifier"] = domain_identifier
        if domain_type is not UNSET:
            field_dict["domainType"] = domain_type
        if frontend_url is not UNSET:
            field_dict["frontendUrl"] = frontend_url
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if preview is not UNSET:
            field_dict["preview"] = preview
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wiki_categories_wiki_category_id_search_response_200_search_result_domain_attributes import (
            GetWikiCategoriesWikiCategoryIdSearchResponse200SearchResultDomainAttributes,
        )

        d = dict(src_dict)
        api_url = d.pop("apiUrl", UNSET)

        _domain_attributes = d.pop("domainAttributes", UNSET)
        domain_attributes: (
            GetWikiCategoriesWikiCategoryIdSearchResponse200SearchResultDomainAttributes
            | Unset
        )
        if isinstance(_domain_attributes, Unset):
            domain_attributes = UNSET
        else:
            domain_attributes = GetWikiCategoriesWikiCategoryIdSearchResponse200SearchResultDomainAttributes.from_dict(
                _domain_attributes
            )

        domain_identifier = d.pop("domainIdentifier", UNSET)

        domain_type = d.pop("domainType", UNSET)

        frontend_url = d.pop("frontendUrl", UNSET)

        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("imageUrl", UNSET))

        def _parse_preview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preview = _parse_preview(d.pop("preview", UNSET))

        title = d.pop("title", UNSET)

        get_wiki_categories_wiki_category_id_search_response_200_search_result = cls(
            api_url=api_url,
            domain_attributes=domain_attributes,
            domain_identifier=domain_identifier,
            domain_type=domain_type,
            frontend_url=frontend_url,
            image_url=image_url,
            preview=preview,
            title=title,
        )

        get_wiki_categories_wiki_category_id_search_response_200_search_result.additional_properties = d
        return get_wiki_categories_wiki_category_id_search_response_200_search_result

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
