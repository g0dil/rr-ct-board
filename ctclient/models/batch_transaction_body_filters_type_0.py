from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchTransactionBodyFiltersType0")


@_attrs_define
class BatchTransactionBodyFiltersType0:
    """Transaction Filter

    Attributes:
        accounting_period_id (int): Filter by Accounting Period Example: 1.
        account_ids (list[int] | Unset): Filter by account/contra account. All transactions match, where either account
            or contra account is in the list.
        cost_center_ids (list[int] | Unset): Filter by Cost Centers.
        created_pid (int | Unset): Filter by person ID. Get all transactions the person has created. But only show those
            the user can see.
        donator_ids (list[int] | Unset): Filter by donator or donator spouse. Provide an array of person ids.
        end_date (datetime.date | Unset): Show transactions before this date.
        is_donation (bool | Unset): Filter by donations. `true` = Only donations, `false` = Other than donation.
        is_immutable (bool | Unset): Filter transactions, whether transaction is immutable.
        is_income (bool | Unset): Filter transactions by income or outcome transactions. An account group has a flag
            `cash asset account` to indicate accounts for income/outcome.
        start_date (datetime.date | Unset): Show transactions after this date.
    """

    accounting_period_id: int
    account_ids: list[int] | Unset = UNSET
    cost_center_ids: list[int] | Unset = UNSET
    created_pid: int | Unset = UNSET
    donator_ids: list[int] | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    is_donation: bool | Unset = UNSET
    is_immutable: bool | Unset = UNSET
    is_income: bool | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_period_id = self.accounting_period_id

        account_ids: list[int] | Unset = UNSET
        if not isinstance(self.account_ids, Unset):
            account_ids = self.account_ids

        cost_center_ids: list[int] | Unset = UNSET
        if not isinstance(self.cost_center_ids, Unset):
            cost_center_ids = self.cost_center_ids

        created_pid = self.created_pid

        donator_ids: list[int] | Unset = UNSET
        if not isinstance(self.donator_ids, Unset):
            donator_ids = self.donator_ids

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        is_donation = self.is_donation

        is_immutable = self.is_immutable

        is_income = self.is_income

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountingPeriodId": accounting_period_id,
            }
        )
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids
        if cost_center_ids is not UNSET:
            field_dict["costCenterIds"] = cost_center_ids
        if created_pid is not UNSET:
            field_dict["createdPid"] = created_pid
        if donator_ids is not UNSET:
            field_dict["donatorIds"] = donator_ids
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if is_donation is not UNSET:
            field_dict["isDonation"] = is_donation
        if is_immutable is not UNSET:
            field_dict["isImmutable"] = is_immutable
        if is_income is not UNSET:
            field_dict["isIncome"] = is_income
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounting_period_id = d.pop("accountingPeriodId")

        account_ids = cast(list[int], d.pop("accountIds", UNSET))

        cost_center_ids = cast(list[int], d.pop("costCenterIds", UNSET))

        created_pid = d.pop("createdPid", UNSET)

        donator_ids = cast(list[int], d.pop("donatorIds", UNSET))

        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        is_donation = d.pop("isDonation", UNSET)

        is_immutable = d.pop("isImmutable", UNSET)

        is_income = d.pop("isIncome", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        batch_transaction_body_filters_type_0 = cls(
            accounting_period_id=accounting_period_id,
            account_ids=account_ids,
            cost_center_ids=cost_center_ids,
            created_pid=created_pid,
            donator_ids=donator_ids,
            end_date=end_date,
            is_donation=is_donation,
            is_immutable=is_immutable,
            is_income=is_income,
            start_date=start_date,
        )

        batch_transaction_body_filters_type_0.additional_properties = d
        return batch_transaction_body_filters_type_0

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
