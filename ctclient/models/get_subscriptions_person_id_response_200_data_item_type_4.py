from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_subscriptions_person_id_response_200_data_item_type_4_origin import (
    GetSubscriptionsPersonIdResponse200DataItemType4Origin,
)
from ..models.get_subscriptions_person_id_response_200_data_item_type_4_subject import (
    GetSubscriptionsPersonIdResponse200DataItemType4Subject,
)

if TYPE_CHECKING:
    from ..models.get_subscriptions_person_id_response_200_data_item_type_4_meta_type_0 import (
        GetSubscriptionsPersonIdResponse200DataItemType4MetaType0,
    )


T = TypeVar("T", bound="GetSubscriptionsPersonIdResponse200DataItemType4")


@_attrs_define
class GetSubscriptionsPersonIdResponse200DataItemType4:
    """
    Attributes:
        is_active (bool):
        is_explicit (bool):
        meta (GetSubscriptionsPersonIdResponse200DataItemType4MetaType0 | None):
        origin (GetSubscriptionsPersonIdResponse200DataItemType4Origin):
        origin_hint (None | str): Translation key addressed to end user
        person_id (int):
        subject_identifier (str):
        subject (GetSubscriptionsPersonIdResponse200DataItemType4Subject):
    """

    is_active: bool
    is_explicit: bool
    meta: GetSubscriptionsPersonIdResponse200DataItemType4MetaType0 | None
    origin: GetSubscriptionsPersonIdResponse200DataItemType4Origin
    origin_hint: None | str
    person_id: int
    subject_identifier: str
    subject: GetSubscriptionsPersonIdResponse200DataItemType4Subject
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_subscriptions_person_id_response_200_data_item_type_4_meta_type_0 import (
            GetSubscriptionsPersonIdResponse200DataItemType4MetaType0,
        )

        is_active = self.is_active

        is_explicit = self.is_explicit

        meta: dict[str, Any] | None
        if isinstance(
            self.meta, GetSubscriptionsPersonIdResponse200DataItemType4MetaType0
        ):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        origin = self.origin.value

        origin_hint: None | str
        origin_hint = self.origin_hint

        person_id = self.person_id

        subject_identifier = self.subject_identifier

        subject = self.subject.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isActive": is_active,
                "isExplicit": is_explicit,
                "meta": meta,
                "origin": origin,
                "originHint": origin_hint,
                "personId": person_id,
                "subjectIdentifier": subject_identifier,
                "subject": subject,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_subscriptions_person_id_response_200_data_item_type_4_meta_type_0 import (
            GetSubscriptionsPersonIdResponse200DataItemType4MetaType0,
        )

        d = dict(src_dict)
        is_active = d.pop("isActive")

        is_explicit = d.pop("isExplicit")

        def _parse_meta(
            data: object,
        ) -> GetSubscriptionsPersonIdResponse200DataItemType4MetaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = (
                    GetSubscriptionsPersonIdResponse200DataItemType4MetaType0.from_dict(
                        data
                    )
                )

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(
                GetSubscriptionsPersonIdResponse200DataItemType4MetaType0 | None, data
            )

        meta = _parse_meta(d.pop("meta"))

        origin = GetSubscriptionsPersonIdResponse200DataItemType4Origin(d.pop("origin"))

        def _parse_origin_hint(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        origin_hint = _parse_origin_hint(d.pop("originHint"))

        person_id = d.pop("personId")

        subject_identifier = d.pop("subjectIdentifier")

        subject = GetSubscriptionsPersonIdResponse200DataItemType4Subject(
            d.pop("subject")
        )

        get_subscriptions_person_id_response_200_data_item_type_4 = cls(
            is_active=is_active,
            is_explicit=is_explicit,
            meta=meta,
            origin=origin,
            origin_hint=origin_hint,
            person_id=person_id,
            subject_identifier=subject_identifier,
            subject=subject,
        )

        get_subscriptions_person_id_response_200_data_item_type_4.additional_properties = d
        return get_subscriptions_person_id_response_200_data_item_type_4

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
