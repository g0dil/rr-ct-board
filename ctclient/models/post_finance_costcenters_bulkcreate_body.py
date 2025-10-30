from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_finance_costcenters_bulkcreate_body_cost_centers_item import (
        PostFinanceCostcentersBulkcreateBodyCostCentersItem,
    )


T = TypeVar("T", bound="PostFinanceCostcentersBulkcreateBody")


@_attrs_define
class PostFinanceCostcentersBulkcreateBody:
    """
    Attributes:
        cost_centers (list[PostFinanceCostcentersBulkcreateBodyCostCentersItem] | Unset):
    """

    cost_centers: list[PostFinanceCostcentersBulkcreateBodyCostCentersItem] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_centers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cost_centers, Unset):
            cost_centers = []
            for cost_centers_item_data in self.cost_centers:
                cost_centers_item = cost_centers_item_data.to_dict()
                cost_centers.append(cost_centers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_centers is not UNSET:
            field_dict["costCenters"] = cost_centers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_finance_costcenters_bulkcreate_body_cost_centers_item import (
            PostFinanceCostcentersBulkcreateBodyCostCentersItem,
        )

        d = dict(src_dict)
        cost_centers = []
        _cost_centers = d.pop("costCenters", UNSET)
        for cost_centers_item_data in _cost_centers or []:
            cost_centers_item = (
                PostFinanceCostcentersBulkcreateBodyCostCentersItem.from_dict(
                    cost_centers_item_data
                )
            )

            cost_centers.append(cost_centers_item)

        post_finance_costcenters_bulkcreate_body = cls(
            cost_centers=cost_centers,
        )

        post_finance_costcenters_bulkcreate_body.additional_properties = d
        return post_finance_costcenters_bulkcreate_body

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
