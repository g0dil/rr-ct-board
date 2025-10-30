from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceOfPerson")


@_attrs_define
class ServiceOfPerson:
    """
    Attributes:
        comment (None | str):
        id (float):
        index (float | None):
        is_accepted (bool):
        is_valid (bool):
        name (None | str):
        person_id (float | None):
        service_id (float | None):
        service_name (str):
        agreed (bool | Unset):
        counter (float | Unset):
    """

    comment: None | str
    id: float
    index: float | None
    is_accepted: bool
    is_valid: bool
    name: None | str
    person_id: float | None
    service_id: float | None
    service_name: str
    agreed: bool | Unset = UNSET
    counter: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment: None | str
        comment = self.comment

        id = self.id

        index: float | None
        index = self.index

        is_accepted = self.is_accepted

        is_valid = self.is_valid

        name: None | str
        name = self.name

        person_id: float | None
        person_id = self.person_id

        service_id: float | None
        service_id = self.service_id

        service_name = self.service_name

        agreed = self.agreed

        counter = self.counter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "id": id,
                "index": index,
                "isAccepted": is_accepted,
                "isValid": is_valid,
                "name": name,
                "personId": person_id,
                "serviceId": service_id,
                "serviceName": service_name,
            }
        )
        if agreed is not UNSET:
            field_dict["agreed"] = agreed
        if counter is not UNSET:
            field_dict["counter"] = counter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_comment(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        comment = _parse_comment(d.pop("comment"))

        id = d.pop("id")

        def _parse_index(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        index = _parse_index(d.pop("index"))

        is_accepted = d.pop("isAccepted")

        is_valid = d.pop("isValid")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_person_id(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        person_id = _parse_person_id(d.pop("personId"))

        def _parse_service_id(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        service_id = _parse_service_id(d.pop("serviceId"))

        service_name = d.pop("serviceName")

        agreed = d.pop("agreed", UNSET)

        counter = d.pop("counter", UNSET)

        service_of_person = cls(
            comment=comment,
            id=id,
            index=index,
            is_accepted=is_accepted,
            is_valid=is_valid,
            name=name,
            person_id=person_id,
            service_id=service_id,
            service_name=service_name,
            agreed=agreed,
            counter=counter,
        )

        service_of_person.additional_properties = d
        return service_of_person

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
