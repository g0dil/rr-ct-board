from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAccountsImportTemplateBody")


@_attrs_define
class GetAccountsImportTemplateBody:
    """
    Attributes:
        client_id (float | Unset):
        template_id (float | Unset):
        with_clients (bool | Unset): if set to true, export also contains the columns "client" and "booking year"
            Default: False.
        year (float | Unset):
    """

    client_id: float | Unset = UNSET
    template_id: float | Unset = UNSET
    with_clients: bool | Unset = False
    year: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        template_id = self.template_id

        with_clients = self.with_clients

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if with_clients is not UNSET:
            field_dict["withClients"] = with_clients
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("clientId", UNSET)

        template_id = d.pop("templateId", UNSET)

        with_clients = d.pop("withClients", UNSET)

        year = d.pop("year", UNSET)

        get_accounts_import_template_body = cls(
            client_id=client_id,
            template_id=template_id,
            with_clients=with_clients,
            year=year,
        )

        get_accounts_import_template_body.additional_properties = d
        return get_accounts_import_template_body

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
