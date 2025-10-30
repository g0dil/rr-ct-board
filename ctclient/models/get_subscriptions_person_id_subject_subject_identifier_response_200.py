from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_0 import (
        GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0,
    )
    from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1 import (
        GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1,
    )
    from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_2 import (
        GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2,
    )
    from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_3 import (
        GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3,
    )
    from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_4 import (
        GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4,
    )
    from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_5 import (
        GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5,
    )


T = TypeVar("T", bound="GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200")


@_attrs_define
class GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200:
    """
    Attributes:
        data (list[GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0 |
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1 |
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2 |
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3 |
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4 |
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5] | Unset):
    """

    data: (
        list[
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0
            | GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1
            | GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2
            | GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3
            | GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4
            | GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5
        ]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_0 import (
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0,
        )
        from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1 import (
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1,
        )
        from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_2 import (
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2,
        )
        from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_3 import (
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3,
        )
        from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_4 import (
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4,
        )

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item: dict[str, Any]
                if isinstance(
                    data_item_data,
                    GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0,
                ):
                    data_item = data_item_data.to_dict()
                elif isinstance(
                    data_item_data,
                    GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1,
                ):
                    data_item = data_item_data.to_dict()
                elif isinstance(
                    data_item_data,
                    GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2,
                ):
                    data_item = data_item_data.to_dict()
                elif isinstance(
                    data_item_data,
                    GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3,
                ):
                    data_item = data_item_data.to_dict()
                elif isinstance(
                    data_item_data,
                    GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4,
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
        from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_0 import (
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0,
        )
        from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_1 import (
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1,
        )
        from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_2 import (
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2,
        )
        from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_3 import (
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3,
        )
        from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_4 import (
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4,
        )
        from ..models.get_subscriptions_person_id_subject_subject_identifier_response_200_data_item_type_5 import (
            GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:

            def _parse_data_item(
                data: object,
            ) -> (
                GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0
                | GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1
                | GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2
                | GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3
                | GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4
                | GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_0 = GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType0.from_dict(
                        data
                    )

                    return data_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType1.from_dict(
                        data
                    )

                    return data_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_2 = GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType2.from_dict(
                        data
                    )

                    return data_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_3 = GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType3.from_dict(
                        data
                    )

                    return data_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_4 = GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType4.from_dict(
                        data
                    )

                    return data_item_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                data_item_type_5 = GetSubscriptionsPersonIdSubjectSubjectIdentifierResponse200DataItemType5.from_dict(
                    data
                )

                return data_item_type_5

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)

        get_subscriptions_person_id_subject_subject_identifier_response_200 = cls(
            data=data,
        )

        get_subscriptions_person_id_subject_subject_identifier_response_200.additional_properties = d
        return get_subscriptions_person_id_subject_subject_identifier_response_200

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
