from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_dynamicgrouop_status_response_200_data_process_group_only_active import (
        PutDynamicgrouopStatusResponse200DataProcessGroupOnlyActive,
    )
    from ..models.put_dynamicgrouop_status_response_200_data_process_group_only_none import (
        PutDynamicgrouopStatusResponse200DataProcessGroupOnlyNone,
    )
    from ..models.put_dynamicgrouop_status_response_200_data_process_group_only_requested import (
        PutDynamicgrouopStatusResponse200DataProcessGroupOnlyRequested,
    )
    from ..models.put_dynamicgrouop_status_response_200_data_process_group_only_to_delete import (
        PutDynamicgrouopStatusResponse200DataProcessGroupOnlyToDelete,
    )
    from ..models.put_dynamicgrouop_status_response_200_data_process_group_only_waiting import (
        PutDynamicgrouopStatusResponse200DataProcessGroupOnlyWaiting,
    )


T = TypeVar("T", bound="PutDynamicgrouopStatusResponse200DataProcessGroupOnly")


@_attrs_define
class PutDynamicgrouopStatusResponse200DataProcessGroupOnly:
    """
    Attributes:
        active (PutDynamicgrouopStatusResponse200DataProcessGroupOnlyActive | Unset):
        none (PutDynamicgrouopStatusResponse200DataProcessGroupOnlyNone | Unset):
        requested (PutDynamicgrouopStatusResponse200DataProcessGroupOnlyRequested | Unset):
        to_delete (PutDynamicgrouopStatusResponse200DataProcessGroupOnlyToDelete | Unset):
        waiting (PutDynamicgrouopStatusResponse200DataProcessGroupOnlyWaiting | Unset):
    """

    active: PutDynamicgrouopStatusResponse200DataProcessGroupOnlyActive | Unset = UNSET
    none: PutDynamicgrouopStatusResponse200DataProcessGroupOnlyNone | Unset = UNSET
    requested: (
        PutDynamicgrouopStatusResponse200DataProcessGroupOnlyRequested | Unset
    ) = UNSET
    to_delete: PutDynamicgrouopStatusResponse200DataProcessGroupOnlyToDelete | Unset = (
        UNSET
    )
    waiting: PutDynamicgrouopStatusResponse200DataProcessGroupOnlyWaiting | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active, Unset):
            active = self.active.to_dict()

        none: dict[str, Any] | Unset = UNSET
        if not isinstance(self.none, Unset):
            none = self.none.to_dict()

        requested: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requested, Unset):
            requested = self.requested.to_dict()

        to_delete: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_delete, Unset):
            to_delete = self.to_delete.to_dict()

        waiting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.waiting, Unset):
            waiting = self.waiting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if none is not UNSET:
            field_dict["none"] = none
        if requested is not UNSET:
            field_dict["requested"] = requested
        if to_delete is not UNSET:
            field_dict["to_delete"] = to_delete
        if waiting is not UNSET:
            field_dict["waiting"] = waiting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_dynamicgrouop_status_response_200_data_process_group_only_active import (
            PutDynamicgrouopStatusResponse200DataProcessGroupOnlyActive,
        )
        from ..models.put_dynamicgrouop_status_response_200_data_process_group_only_none import (
            PutDynamicgrouopStatusResponse200DataProcessGroupOnlyNone,
        )
        from ..models.put_dynamicgrouop_status_response_200_data_process_group_only_requested import (
            PutDynamicgrouopStatusResponse200DataProcessGroupOnlyRequested,
        )
        from ..models.put_dynamicgrouop_status_response_200_data_process_group_only_to_delete import (
            PutDynamicgrouopStatusResponse200DataProcessGroupOnlyToDelete,
        )
        from ..models.put_dynamicgrouop_status_response_200_data_process_group_only_waiting import (
            PutDynamicgrouopStatusResponse200DataProcessGroupOnlyWaiting,
        )

        d = dict(src_dict)
        _active = d.pop("active", UNSET)
        active: PutDynamicgrouopStatusResponse200DataProcessGroupOnlyActive | Unset
        if isinstance(_active, Unset):
            active = UNSET
        else:
            active = (
                PutDynamicgrouopStatusResponse200DataProcessGroupOnlyActive.from_dict(
                    _active
                )
            )

        _none = d.pop("none", UNSET)
        none: PutDynamicgrouopStatusResponse200DataProcessGroupOnlyNone | Unset
        if isinstance(_none, Unset):
            none = UNSET
        else:
            none = PutDynamicgrouopStatusResponse200DataProcessGroupOnlyNone.from_dict(
                _none
            )

        _requested = d.pop("requested", UNSET)
        requested: (
            PutDynamicgrouopStatusResponse200DataProcessGroupOnlyRequested | Unset
        )
        if isinstance(_requested, Unset):
            requested = UNSET
        else:
            requested = PutDynamicgrouopStatusResponse200DataProcessGroupOnlyRequested.from_dict(
                _requested
            )

        _to_delete = d.pop("to_delete", UNSET)
        to_delete: PutDynamicgrouopStatusResponse200DataProcessGroupOnlyToDelete | Unset
        if isinstance(_to_delete, Unset):
            to_delete = UNSET
        else:
            to_delete = (
                PutDynamicgrouopStatusResponse200DataProcessGroupOnlyToDelete.from_dict(
                    _to_delete
                )
            )

        _waiting = d.pop("waiting", UNSET)
        waiting: PutDynamicgrouopStatusResponse200DataProcessGroupOnlyWaiting | Unset
        if isinstance(_waiting, Unset):
            waiting = UNSET
        else:
            waiting = (
                PutDynamicgrouopStatusResponse200DataProcessGroupOnlyWaiting.from_dict(
                    _waiting
                )
            )

        put_dynamicgrouop_status_response_200_data_process_group_only = cls(
            active=active,
            none=none,
            requested=requested,
            to_delete=to_delete,
            waiting=waiting,
        )

        put_dynamicgrouop_status_response_200_data_process_group_only.additional_properties = d
        return put_dynamicgrouop_status_response_200_data_process_group_only

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
