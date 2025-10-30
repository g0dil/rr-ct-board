from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.get_account_statements_response_200_data_item_statistics import (
        GetAccountStatementsResponse200DataItemStatistics,
    )


T = TypeVar("T", bound="GetAccountStatementsResponse200DataItem")


@_attrs_define
class GetAccountStatementsResponse200DataItem:
    """
    Attributes:
        duplicates (int):
        end_amount (float): amount in cents
        end_date (datetime.date): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
        id (int):
        identifier (str):
        name (str):
        start_amount (float): amount in cents
        start_date (datetime.date): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
        statistics (GetAccountStatementsResponse200DataItemStatistics):
    """

    duplicates: int
    end_amount: float
    end_date: datetime.date
    id: int
    identifier: str
    name: str
    start_amount: float
    start_date: datetime.date
    statistics: GetAccountStatementsResponse200DataItemStatistics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duplicates = self.duplicates

        end_amount = self.end_amount

        end_date = self.end_date.isoformat()

        id = self.id

        identifier = self.identifier

        name = self.name

        start_amount = self.start_amount

        start_date = self.start_date.isoformat()

        statistics = self.statistics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duplicates": duplicates,
                "endAmount": end_amount,
                "endDate": end_date,
                "id": id,
                "identifier": identifier,
                "name": name,
                "startAmount": start_amount,
                "startDate": start_date,
                "statistics": statistics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_account_statements_response_200_data_item_statistics import (
            GetAccountStatementsResponse200DataItemStatistics,
        )

        d = dict(src_dict)
        duplicates = d.pop("duplicates")

        end_amount = d.pop("endAmount")

        end_date = isoparse(d.pop("endDate")).date()

        id = d.pop("id")

        identifier = d.pop("identifier")

        name = d.pop("name")

        start_amount = d.pop("startAmount")

        start_date = isoparse(d.pop("startDate")).date()

        statistics = GetAccountStatementsResponse200DataItemStatistics.from_dict(
            d.pop("statistics")
        )

        get_account_statements_response_200_data_item = cls(
            duplicates=duplicates,
            end_amount=end_amount,
            end_date=end_date,
            id=id,
            identifier=identifier,
            name=name,
            start_amount=start_amount,
            start_date=start_date,
            statistics=statistics,
        )

        get_account_statements_response_200_data_item.additional_properties = d
        return get_account_statements_response_200_data_item

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
