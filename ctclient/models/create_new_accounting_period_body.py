from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_new_accounting_period_body_balances import (
        CreateNewAccountingPeriodBodyBalances,
    )


T = TypeVar("T", bound="CreateNewAccountingPeriodBody")


@_attrs_define
class CreateNewAccountingPeriodBody:
    """
    Attributes:
        client_id (int):
        end_date (datetime.date):
        increment_document_number (bool):
        is_closed (bool):
        start_date (datetime.date):
        balances (CreateNewAccountingPeriodBodyBalances | Unset):
        copy_master_data (bool | Unset): Copy all master data from previous accounting period. Default: False.
    """

    client_id: int
    end_date: datetime.date
    increment_document_number: bool
    is_closed: bool
    start_date: datetime.date
    balances: CreateNewAccountingPeriodBodyBalances | Unset = UNSET
    copy_master_data: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        end_date = self.end_date.isoformat()

        increment_document_number = self.increment_document_number

        is_closed = self.is_closed

        start_date = self.start_date.isoformat()

        balances: dict[str, Any] | Unset = UNSET
        if not isinstance(self.balances, Unset):
            balances = self.balances.to_dict()

        copy_master_data = self.copy_master_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientId": client_id,
                "endDate": end_date,
                "incrementDocumentNumber": increment_document_number,
                "isClosed": is_closed,
                "startDate": start_date,
            }
        )
        if balances is not UNSET:
            field_dict["balances"] = balances
        if copy_master_data is not UNSET:
            field_dict["copyMasterData"] = copy_master_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_new_accounting_period_body_balances import (
            CreateNewAccountingPeriodBodyBalances,
        )

        d = dict(src_dict)
        client_id = d.pop("clientId")

        end_date = isoparse(d.pop("endDate")).date()

        increment_document_number = d.pop("incrementDocumentNumber")

        is_closed = d.pop("isClosed")

        start_date = isoparse(d.pop("startDate")).date()

        _balances = d.pop("balances", UNSET)
        balances: CreateNewAccountingPeriodBodyBalances | Unset
        if isinstance(_balances, Unset):
            balances = UNSET
        else:
            balances = CreateNewAccountingPeriodBodyBalances.from_dict(_balances)

        copy_master_data = d.pop("copyMasterData", UNSET)

        create_new_accounting_period_body = cls(
            client_id=client_id,
            end_date=end_date,
            increment_document_number=increment_document_number,
            is_closed=is_closed,
            start_date=start_date,
            balances=balances,
            copy_master_data=copy_master_data,
        )

        create_new_accounting_period_body.additional_properties = d
        return create_new_accounting_period_body

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
