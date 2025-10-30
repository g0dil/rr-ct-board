from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1_origin import (
    PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1Origin,
)
from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1_subject import (
    PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1Subject,
)

if TYPE_CHECKING:
    from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1_meta_type_0 import (
        PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1MetaType0,
    )


T = TypeVar(
    "T",
    bound="PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1",
)


@_attrs_define
class PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1:
    """
    Attributes:
        is_active (bool):
        is_explicit (bool):
        meta (None | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1MetaType0):
        origin (PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1Origin):
        origin_hint (None | str): Translation key addressed to end user
        person_id (int):
        subject_identifier (str):
        subject (PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1Subject):
    """

    is_active: bool
    is_explicit: bool
    meta: (
        None
        | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1MetaType0
    )
    origin: (
        PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1Origin
    )
    origin_hint: None | str
    person_id: int
    subject_identifier: str
    subject: (
        PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1Subject
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1_meta_type_0 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1MetaType0,
        )

        is_active = self.is_active

        is_explicit = self.is_explicit

        meta: dict[str, Any] | None
        if isinstance(
            self.meta,
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1MetaType0,
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
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1_meta_type_0 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1MetaType0,
        )

        d = dict(src_dict)
        is_active = d.pop("isActive")

        is_explicit = d.pop("isExplicit")

        def _parse_meta(
            data: object,
        ) -> (
            None
            | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1MetaType0
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1MetaType0.from_dict(
                    data
                )

                return meta_type_0
            except:  # noqa: E722
                pass
            return cast(
                None
                | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1MetaType0,
                data,
            )

        meta = _parse_meta(d.pop("meta"))

        origin = PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1Origin(
            d.pop("origin")
        )

        def _parse_origin_hint(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        origin_hint = _parse_origin_hint(d.pop("originHint"))

        person_id = d.pop("personId")

        subject_identifier = d.pop("subjectIdentifier")

        subject = PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1Subject(
            d.pop("subject")
        )

        put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1 = cls(
            is_active=is_active,
            is_explicit=is_explicit,
            meta=meta,
            origin=origin,
            origin_hint=origin_hint,
            person_id=person_id,
            subject_identifier=subject_identifier,
            subject=subject,
        )

        put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1.additional_properties = d
        return put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1

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
