from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFinanceCostcentersBulkcreateBodyCostCentersItem")


@_attrs_define
class PostFinanceCostcentersBulkcreateBodyCostCentersItem:
    """
    Attributes:
        accounting_period_id (int | Unset):
        budget (float | None | Unset):
        group_id (int | None | Unset):
        name (str | Unset):
        number (str | Unset):
    """

    accounting_period_id: int | Unset = UNSET
    budget: float | None | Unset = UNSET
    group_id: int | None | Unset = UNSET
    name: str | Unset = UNSET
    number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_period_id = self.accounting_period_id

        budget: float | None | Unset
        if isinstance(self.budget, Unset):
            budget = UNSET
        else:
            budget = self.budget

        group_id: int | None | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        name = self.name

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounting_period_id is not UNSET:
            field_dict["accountingPeriodId"] = accounting_period_id
        if budget is not UNSET:
            field_dict["budget"] = budget
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounting_period_id = d.pop("accountingPeriodId", UNSET)

        def _parse_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        budget = _parse_budget(d.pop("budget", UNSET))

        def _parse_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))

        name = d.pop("name", UNSET)

        number = d.pop("number", UNSET)

        post_finance_costcenters_bulkcreate_body_cost_centers_item = cls(
            accounting_period_id=accounting_period_id,
            budget=budget,
            group_id=group_id,
            name=name,
            number=number,
        )

        post_finance_costcenters_bulkcreate_body_cost_centers_item.additional_properties = d
        return post_finance_costcenters_bulkcreate_body_cost_centers_item

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
