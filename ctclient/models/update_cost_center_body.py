from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCostCenterBody")


@_attrs_define
class UpdateCostCenterBody:
    """
    Example:
        {'accountId': 4, 'accountingPeriodId': 5, 'budget': 2300, 'groupId': 5, 'name': 'Kostenstelle Jugend', 'number':
            '803'}

    Attributes:
        accounting_period_id (int):
        name (str):
        number (str):
        budget (int | Unset): Provide budget in cent.
        group_id (int | Unset):
    """

    accounting_period_id: int
    name: str
    number: str
    budget: int | Unset = UNSET
    group_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_period_id = self.accounting_period_id

        name = self.name

        number = self.number

        budget = self.budget

        group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountingPeriodId": accounting_period_id,
                "name": name,
                "number": number,
            }
        )
        if budget is not UNSET:
            field_dict["budget"] = budget
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounting_period_id = d.pop("accountingPeriodId")

        name = d.pop("name")

        number = d.pop("number")

        budget = d.pop("budget", UNSET)

        group_id = d.pop("groupId", UNSET)

        update_cost_center_body = cls(
            accounting_period_id=accounting_period_id,
            name=name,
            number=number,
            budget=budget,
            group_id=group_id,
        )

        update_cost_center_body.additional_properties = d
        return update_cost_center_body

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
