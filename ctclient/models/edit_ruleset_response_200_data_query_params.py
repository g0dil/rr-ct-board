from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_ruleset_response_200_data_query_params_computed_fields_item import (
        EditRulesetResponse200DataQueryParamsComputedFieldsItem,
    )
    from ..models.edit_ruleset_response_200_data_query_params_filter import (
        EditRulesetResponse200DataQueryParamsFilter,
    )


T = TypeVar("T", bound="EditRulesetResponse200DataQueryParams")


@_attrs_define
class EditRulesetResponse200DataQueryParams:
    """
    Attributes:
        computed_fields (list[EditRulesetResponse200DataQueryParamsComputedFieldsItem] | Unset):
        description (str | Unset):
        filter_ (EditRulesetResponse200DataQueryParamsFilter | Unset):
        group_by (list[str] | Unset):
        order_by (list[str] | Unset):
        outfile_name_part (str | Unset):
        primary_entity_alias (str | Unset):
        response_fields (list[str] | Unset):
        title (str | Unset):
    """

    computed_fields: (
        list[EditRulesetResponse200DataQueryParamsComputedFieldsItem] | Unset
    ) = UNSET
    description: str | Unset = UNSET
    filter_: EditRulesetResponse200DataQueryParamsFilter | Unset = UNSET
    group_by: list[str] | Unset = UNSET
    order_by: list[str] | Unset = UNSET
    outfile_name_part: str | Unset = UNSET
    primary_entity_alias: str | Unset = UNSET
    response_fields: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        computed_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.computed_fields, Unset):
            computed_fields = []
            for computed_fields_item_data in self.computed_fields:
                computed_fields_item = computed_fields_item_data.to_dict()
                computed_fields.append(computed_fields_item)

        description = self.description

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        group_by: list[str] | Unset = UNSET
        if not isinstance(self.group_by, Unset):
            group_by = self.group_by

        order_by: list[str] | Unset = UNSET
        if not isinstance(self.order_by, Unset):
            order_by = self.order_by

        outfile_name_part = self.outfile_name_part

        primary_entity_alias = self.primary_entity_alias

        response_fields: list[str] | Unset = UNSET
        if not isinstance(self.response_fields, Unset):
            response_fields = self.response_fields

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computed_fields is not UNSET:
            field_dict["computedFields"] = computed_fields
        if description is not UNSET:
            field_dict["description"] = description
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if group_by is not UNSET:
            field_dict["groupBy"] = group_by
        if order_by is not UNSET:
            field_dict["orderBy"] = order_by
        if outfile_name_part is not UNSET:
            field_dict["outfileNamePart"] = outfile_name_part
        if primary_entity_alias is not UNSET:
            field_dict["primaryEntityAlias"] = primary_entity_alias
        if response_fields is not UNSET:
            field_dict["responseFields"] = response_fields
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_ruleset_response_200_data_query_params_computed_fields_item import (
            EditRulesetResponse200DataQueryParamsComputedFieldsItem,
        )
        from ..models.edit_ruleset_response_200_data_query_params_filter import (
            EditRulesetResponse200DataQueryParamsFilter,
        )

        d = dict(src_dict)
        computed_fields = []
        _computed_fields = d.pop("computedFields", UNSET)
        for computed_fields_item_data in _computed_fields or []:
            computed_fields_item = (
                EditRulesetResponse200DataQueryParamsComputedFieldsItem.from_dict(
                    computed_fields_item_data
                )
            )

            computed_fields.append(computed_fields_item)

        description = d.pop("description", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: EditRulesetResponse200DataQueryParamsFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = EditRulesetResponse200DataQueryParamsFilter.from_dict(_filter_)

        group_by = cast(list[str], d.pop("groupBy", UNSET))

        order_by = cast(list[str], d.pop("orderBy", UNSET))

        outfile_name_part = d.pop("outfileNamePart", UNSET)

        primary_entity_alias = d.pop("primaryEntityAlias", UNSET)

        response_fields = cast(list[str], d.pop("responseFields", UNSET))

        title = d.pop("title", UNSET)

        edit_ruleset_response_200_data_query_params = cls(
            computed_fields=computed_fields,
            description=description,
            filter_=filter_,
            group_by=group_by,
            order_by=order_by,
            outfile_name_part=outfile_name_part,
            primary_entity_alias=primary_entity_alias,
            response_fields=response_fields,
            title=title,
        )

        edit_ruleset_response_200_data_query_params.additional_properties = d
        return edit_ruleset_response_200_data_query_params

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
