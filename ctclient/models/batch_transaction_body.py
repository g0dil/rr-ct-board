from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.batch_transaction_body_changeset import BatchTransactionBodyChangeset
    from ..models.batch_transaction_body_filters_type_0 import (
        BatchTransactionBodyFiltersType0,
    )
    from ..models.batch_transaction_body_filters_type_1 import (
        BatchTransactionBodyFiltersType1,
    )
    from ..models.batch_transaction_body_filters_type_2 import (
        BatchTransactionBodyFiltersType2,
    )


T = TypeVar("T", bound="BatchTransactionBody")


@_attrs_define
class BatchTransactionBody:
    """
    Attributes:
        changeset (BatchTransactionBodyChangeset): Fields to change.
        filters (BatchTransactionBodyFiltersType0 | BatchTransactionBodyFiltersType1 |
            BatchTransactionBodyFiltersType2): List of filters
    """

    changeset: BatchTransactionBodyChangeset
    filters: (
        BatchTransactionBodyFiltersType0
        | BatchTransactionBodyFiltersType1
        | BatchTransactionBodyFiltersType2
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_transaction_body_filters_type_0 import (
            BatchTransactionBodyFiltersType0,
        )
        from ..models.batch_transaction_body_filters_type_1 import (
            BatchTransactionBodyFiltersType1,
        )

        changeset = self.changeset.to_dict()

        filters: dict[str, Any]
        if isinstance(self.filters, BatchTransactionBodyFiltersType0):
            filters = self.filters.to_dict()
        elif isinstance(self.filters, BatchTransactionBodyFiltersType1):
            filters = self.filters.to_dict()
        else:
            filters = self.filters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changeset": changeset,
                "filters": filters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_transaction_body_changeset import (
            BatchTransactionBodyChangeset,
        )
        from ..models.batch_transaction_body_filters_type_0 import (
            BatchTransactionBodyFiltersType0,
        )
        from ..models.batch_transaction_body_filters_type_1 import (
            BatchTransactionBodyFiltersType1,
        )
        from ..models.batch_transaction_body_filters_type_2 import (
            BatchTransactionBodyFiltersType2,
        )

        d = dict(src_dict)
        changeset = BatchTransactionBodyChangeset.from_dict(d.pop("changeset"))

        def _parse_filters(
            data: object,
        ) -> (
            BatchTransactionBodyFiltersType0
            | BatchTransactionBodyFiltersType1
            | BatchTransactionBodyFiltersType2
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = BatchTransactionBodyFiltersType0.from_dict(data)

                return filters_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_1 = BatchTransactionBodyFiltersType1.from_dict(data)

                return filters_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            filters_type_2 = BatchTransactionBodyFiltersType2.from_dict(data)

            return filters_type_2

        filters = _parse_filters(d.pop("filters"))

        batch_transaction_body = cls(
            changeset=changeset,
            filters=filters,
        )

        batch_transaction_body.additional_properties = d
        return batch_transaction_body

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
