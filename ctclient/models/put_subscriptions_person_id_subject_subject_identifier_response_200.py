from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_0 import (
        PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0,
    )
    from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1 import (
        PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1,
    )
    from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_2 import (
        PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2,
    )
    from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_3 import (
        PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3,
    )
    from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_4 import (
        PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4,
    )
    from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_5 import (
        PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5,
    )


T = TypeVar("T", bound="PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200")


@_attrs_define
class PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200:
    """
    Attributes:
        data (list[PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0 |
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1 |
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2 |
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3 |
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4 |
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5] | Unset):
    """

    data: (
        list[
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0
            | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1
            | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2
            | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3
            | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4
            | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5
        ]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_0 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0,
        )
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1,
        )
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_2 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2,
        )
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_3 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3,
        )
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_4 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4,
        )

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item: dict[str, Any]
                if isinstance(
                    data_item_data,
                    PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0,
                ):
                    data_item = data_item_data.to_dict()
                elif isinstance(
                    data_item_data,
                    PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1,
                ):
                    data_item = data_item_data.to_dict()
                elif isinstance(
                    data_item_data,
                    PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2,
                ):
                    data_item = data_item_data.to_dict()
                elif isinstance(
                    data_item_data,
                    PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3,
                ):
                    data_item = data_item_data.to_dict()
                elif isinstance(
                    data_item_data,
                    PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4,
                ):
                    data_item = data_item_data.to_dict()
                else:
                    data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_0 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0,
        )
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1,
        )
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_2 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2,
        )
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_3 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3,
        )
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_4 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4,
        )
        from ..models.put_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_5 import (
            PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:

            def _parse_data_item(
                data: object,
            ) -> (
                PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0
                | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1
                | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2
                | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3
                | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4
                | PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_0 = PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0.from_dict(
                        data
                    )

                    return data_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1.from_dict(
                        data
                    )

                    return data_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_2 = PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2.from_dict(
                        data
                    )

                    return data_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_3 = PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3.from_dict(
                        data
                    )

                    return data_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_4 = PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4.from_dict(
                        data
                    )

                    return data_item_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                data_item_type_5 = PutSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5.from_dict(
                    data
                )

                return data_item_type_5

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)

        put_subscriptions_person_id_subject_subject_identifier_response_200 = cls(
            data=data,
        )

        put_subscriptions_person_id_subject_subject_identifier_response_200.additional_properties = d
        return put_subscriptions_person_id_subject_subject_identifier_response_200

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
