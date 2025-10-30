from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.accounting_period_meta import AccountingPeriodMeta
    from ..models.accounting_period_permissions import AccountingPeriodPermissions


T = TypeVar("T", bound="AccountingPeriod")


@_attrs_define
class AccountingPeriod:
    """
    Attributes:
        client_id (int):
        end_date (datetime.date):
        increment_document_number (bool):
        is_closed (bool):
        start_date (datetime.date):
        donation_receipts_created (str):
        id (int):
        meta (AccountingPeriodMeta):  Example: {'createdDate': '2020-01-01T00:00:00Z', 'createdPerson': {'id': 1},
            'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
        permissions (AccountingPeriodPermissions):
    """

    client_id: int
    end_date: datetime.date
    increment_document_number: bool
    is_closed: bool
    start_date: datetime.date
    donation_receipts_created: str
    id: int
    meta: AccountingPeriodMeta
    permissions: AccountingPeriodPermissions
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        end_date = self.end_date.isoformat()

        increment_document_number = self.increment_document_number

        is_closed = self.is_closed

        start_date = self.start_date.isoformat()

        donation_receipts_created = self.donation_receipts_created

        id = self.id

        meta = self.meta.to_dict()

        permissions = self.permissions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientId": client_id,
                "endDate": end_date,
                "incrementDocumentNumber": increment_document_number,
                "isClosed": is_closed,
                "startDate": start_date,
                "donationReceiptsCreated": donation_receipts_created,
                "id": id,
                "meta": meta,
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accounting_period_meta import AccountingPeriodMeta
        from ..models.accounting_period_permissions import AccountingPeriodPermissions

        d = dict(src_dict)
        client_id = d.pop("clientId")

        end_date = isoparse(d.pop("endDate")).date()

        increment_document_number = d.pop("incrementDocumentNumber")

        is_closed = d.pop("isClosed")

        start_date = isoparse(d.pop("startDate")).date()

        donation_receipts_created = d.pop("donationReceiptsCreated")

        id = d.pop("id")

        meta = AccountingPeriodMeta.from_dict(d.pop("meta"))

        permissions = AccountingPeriodPermissions.from_dict(d.pop("permissions"))

        accounting_period = cls(
            client_id=client_id,
            end_date=end_date,
            increment_document_number=increment_document_number,
            is_closed=is_closed,
            start_date=start_date,
            donation_receipts_created=donation_receipts_created,
            id=id,
            meta=meta,
            permissions=permissions,
        )

        accounting_period.additional_properties = d
        return accounting_period

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
