from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSyncExecutionsResponse200DataItemBoth")


@_attrs_define
class GetSyncExecutionsResponse200DataItemBoth:
    """
    Attributes:
        create (int):
        delete (int):
        link (int):
        update (int):
    """

    create: int
    delete: int
    link: int
    update: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create = self.create

        delete = self.delete

        link = self.link

        update = self.update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create": create,
                "delete": delete,
                "link": link,
                "update": update,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create = d.pop("create")

        delete = d.pop("delete")

        link = d.pop("link")

        update = d.pop("update")

        get_sync_executions_response_200_data_item_both = cls(
            create=create,
            delete=delete,
            link=link,
            update=update,
        )

        get_sync_executions_response_200_data_item_both.additional_properties = d
        return get_sync_executions_response_200_data_item_both

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
