from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_all_for_service_response_200_item_meta import (
        GetAllForServiceResponse200ItemMeta,
    )
    from ..models.get_all_for_service_response_200_item_requested_event import (
        GetAllForServiceResponse200ItemRequestedEvent,
    )
    from ..models.get_all_for_service_response_200_item_requested_person import (
        GetAllForServiceResponse200ItemRequestedPerson,
    )
    from ..models.get_all_for_service_response_200_item_requesting_event import (
        GetAllForServiceResponse200ItemRequestingEvent,
    )
    from ..models.get_all_for_service_response_200_item_requesting_person import (
        GetAllForServiceResponse200ItemRequestingPerson,
    )


T = TypeVar("T", bound="GetAllForServiceResponse200Item")


@_attrs_define
class GetAllForServiceResponse200Item:
    """
    Attributes:
        id (int | Unset):
        is_archived (bool | Unset):
        meta (GetAllForServiceResponse200ItemMeta | Unset):
        requested_event (GetAllForServiceResponse200ItemRequestedEvent | Unset):
        requested_person (GetAllForServiceResponse200ItemRequestedPerson | Unset): A person object includes all fields
            the logged in user may see depending on the security level. Additional DB fields, created by the admin, are also
            part of the response. Those fields have the same name as the column name.
        requested_service_id (int | Unset):
        requesting_event (GetAllForServiceResponse200ItemRequestingEvent | Unset):
        requesting_person (GetAllForServiceResponse200ItemRequestingPerson | Unset): A person object includes all fields
            the logged in user may see depending on the security level. Additional DB fields, created by the admin, are also
            part of the response. Those fields have the same name as the column name.
        requesting_service_id (int | Unset):
        status (str | Unset):
    """

    id: int | Unset = UNSET
    is_archived: bool | Unset = UNSET
    meta: GetAllForServiceResponse200ItemMeta | Unset = UNSET
    requested_event: GetAllForServiceResponse200ItemRequestedEvent | Unset = UNSET
    requested_person: GetAllForServiceResponse200ItemRequestedPerson | Unset = UNSET
    requested_service_id: int | Unset = UNSET
    requesting_event: GetAllForServiceResponse200ItemRequestingEvent | Unset = UNSET
    requesting_person: GetAllForServiceResponse200ItemRequestingPerson | Unset = UNSET
    requesting_service_id: int | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_archived = self.is_archived

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        requested_event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requested_event, Unset):
            requested_event = self.requested_event.to_dict()

        requested_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requested_person, Unset):
            requested_person = self.requested_person.to_dict()

        requested_service_id = self.requested_service_id

        requesting_event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requesting_event, Unset):
            requesting_event = self.requesting_event.to_dict()

        requesting_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requesting_person, Unset):
            requesting_person = self.requesting_person.to_dict()

        requesting_service_id = self.requesting_service_id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if meta is not UNSET:
            field_dict["meta"] = meta
        if requested_event is not UNSET:
            field_dict["requestedEvent"] = requested_event
        if requested_person is not UNSET:
            field_dict["requestedPerson"] = requested_person
        if requested_service_id is not UNSET:
            field_dict["requestedServiceId"] = requested_service_id
        if requesting_event is not UNSET:
            field_dict["requestingEvent"] = requesting_event
        if requesting_person is not UNSET:
            field_dict["requestingPerson"] = requesting_person
        if requesting_service_id is not UNSET:
            field_dict["requestingServiceId"] = requesting_service_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_all_for_service_response_200_item_meta import (
            GetAllForServiceResponse200ItemMeta,
        )
        from ..models.get_all_for_service_response_200_item_requested_event import (
            GetAllForServiceResponse200ItemRequestedEvent,
        )
        from ..models.get_all_for_service_response_200_item_requested_person import (
            GetAllForServiceResponse200ItemRequestedPerson,
        )
        from ..models.get_all_for_service_response_200_item_requesting_event import (
            GetAllForServiceResponse200ItemRequestingEvent,
        )
        from ..models.get_all_for_service_response_200_item_requesting_person import (
            GetAllForServiceResponse200ItemRequestingPerson,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: GetAllForServiceResponse200ItemMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GetAllForServiceResponse200ItemMeta.from_dict(_meta)

        _requested_event = d.pop("requestedEvent", UNSET)
        requested_event: GetAllForServiceResponse200ItemRequestedEvent | Unset
        if isinstance(_requested_event, Unset):
            requested_event = UNSET
        else:
            requested_event = GetAllForServiceResponse200ItemRequestedEvent.from_dict(
                _requested_event
            )

        _requested_person = d.pop("requestedPerson", UNSET)
        requested_person: GetAllForServiceResponse200ItemRequestedPerson | Unset
        if isinstance(_requested_person, Unset):
            requested_person = UNSET
        else:
            requested_person = GetAllForServiceResponse200ItemRequestedPerson.from_dict(
                _requested_person
            )

        requested_service_id = d.pop("requestedServiceId", UNSET)

        _requesting_event = d.pop("requestingEvent", UNSET)
        requesting_event: GetAllForServiceResponse200ItemRequestingEvent | Unset
        if isinstance(_requesting_event, Unset):
            requesting_event = UNSET
        else:
            requesting_event = GetAllForServiceResponse200ItemRequestingEvent.from_dict(
                _requesting_event
            )

        _requesting_person = d.pop("requestingPerson", UNSET)
        requesting_person: GetAllForServiceResponse200ItemRequestingPerson | Unset
        if isinstance(_requesting_person, Unset):
            requesting_person = UNSET
        else:
            requesting_person = (
                GetAllForServiceResponse200ItemRequestingPerson.from_dict(
                    _requesting_person
                )
            )

        requesting_service_id = d.pop("requestingServiceId", UNSET)

        status = d.pop("status", UNSET)

        get_all_for_service_response_200_item = cls(
            id=id,
            is_archived=is_archived,
            meta=meta,
            requested_event=requested_event,
            requested_person=requested_person,
            requested_service_id=requested_service_id,
            requesting_event=requesting_event,
            requesting_person=requesting_person,
            requesting_service_id=requesting_service_id,
            status=status,
        )

        get_all_for_service_response_200_item.additional_properties = d
        return get_all_for_service_response_200_item

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
