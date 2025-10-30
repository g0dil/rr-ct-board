from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_ruleset_response_200_data_process import (
        EditRulesetResponse200DataProcess,
    )
    from ..models.edit_ruleset_response_200_data_query import (
        EditRulesetResponse200DataQuery,
    )


T = TypeVar("T", bound="EditRulesetResponse200Data")


@_attrs_define
class EditRulesetResponse200Data:
    """
    Attributes:
        description (str | Unset):
        importance (int | Unset):
        person_id_field_name (str | Unset):
        process (EditRulesetResponse200DataProcess | Unset):
        query (EditRulesetResponse200DataQuery | Unset):
        shorty (str | Unset):
    """

    description: str | Unset = UNSET
    importance: int | Unset = UNSET
    person_id_field_name: str | Unset = UNSET
    process: EditRulesetResponse200DataProcess | Unset = UNSET
    query: EditRulesetResponse200DataQuery | Unset = UNSET
    shorty: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        importance = self.importance

        person_id_field_name = self.person_id_field_name

        process: dict[str, Any] | Unset = UNSET
        if not isinstance(self.process, Unset):
            process = self.process.to_dict()

        query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        shorty = self.shorty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if importance is not UNSET:
            field_dict["importance"] = importance
        if person_id_field_name is not UNSET:
            field_dict["personIdFieldName"] = person_id_field_name
        if process is not UNSET:
            field_dict["process"] = process
        if query is not UNSET:
            field_dict["query"] = query
        if shorty is not UNSET:
            field_dict["shorty"] = shorty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_ruleset_response_200_data_process import (
            EditRulesetResponse200DataProcess,
        )
        from ..models.edit_ruleset_response_200_data_query import (
            EditRulesetResponse200DataQuery,
        )

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        importance = d.pop("importance", UNSET)

        person_id_field_name = d.pop("personIdFieldName", UNSET)

        _process = d.pop("process", UNSET)
        process: EditRulesetResponse200DataProcess | Unset
        if isinstance(_process, Unset):
            process = UNSET
        else:
            process = EditRulesetResponse200DataProcess.from_dict(_process)

        _query = d.pop("query", UNSET)
        query: EditRulesetResponse200DataQuery | Unset
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = EditRulesetResponse200DataQuery.from_dict(_query)

        shorty = d.pop("shorty", UNSET)

        edit_ruleset_response_200_data = cls(
            description=description,
            importance=importance,
            person_id_field_name=person_id_field_name,
            process=process,
            query=query,
            shorty=shorty,
        )

        edit_ruleset_response_200_data.additional_properties = d
        return edit_ruleset_response_200_data

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
