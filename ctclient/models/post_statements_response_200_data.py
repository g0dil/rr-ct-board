from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="PostStatementsResponse200Data")


@_attrs_define
class PostStatementsResponse200Data:
    """
    Attributes:
        duplicates (int):
        end_amount (int): end amount in cents
        end_date (datetime.date): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
        file_name (str):
        file_type (str):
        identifier (str):
        movements (int):
        start_amount (int): start amount in cents
        start_date (datetime.date): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
    """

    duplicates: int
    end_amount: int
    end_date: datetime.date
    file_name: str
    file_type: str
    identifier: str
    movements: int
    start_amount: int
    start_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duplicates = self.duplicates

        end_amount = self.end_amount

        end_date = self.end_date.isoformat()

        file_name = self.file_name

        file_type = self.file_type

        identifier = self.identifier

        movements = self.movements

        start_amount = self.start_amount

        start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duplicates": duplicates,
                "endAmount": end_amount,
                "endDate": end_date,
                "fileName": file_name,
                "fileType": file_type,
                "identifier": identifier,
                "movements": movements,
                "startAmount": start_amount,
                "startDate": start_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duplicates = d.pop("duplicates")

        end_amount = d.pop("endAmount")

        end_date = isoparse(d.pop("endDate")).date()

        file_name = d.pop("fileName")

        file_type = d.pop("fileType")

        identifier = d.pop("identifier")

        movements = d.pop("movements")

        start_amount = d.pop("startAmount")

        start_date = isoparse(d.pop("startDate")).date()

        post_statements_response_200_data = cls(
            duplicates=duplicates,
            end_amount=end_amount,
            end_date=end_date,
            file_name=file_name,
            file_type=file_type,
            identifier=identifier,
            movements=movements,
            start_amount=start_amount,
            start_date=start_date,
        )

        post_statements_response_200_data.additional_properties = d
        return post_statements_response_200_data

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
