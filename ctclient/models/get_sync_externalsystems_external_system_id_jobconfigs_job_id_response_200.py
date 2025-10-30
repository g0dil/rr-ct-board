from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sync_externalsystems_external_system_id_jobconfigs_job_id_response_200_job_configuration_return import (
        GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdResponse200JobConfigurationReturn,
    )


T = TypeVar(
    "T", bound="GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdResponse200"
)


@_attrs_define
class GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdResponse200:
    """
    Attributes:
        data (GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdResponse200JobConfigurationReturn | Unset):
    """

    data: (
        GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdResponse200JobConfigurationReturn
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sync_externalsystems_external_system_id_jobconfigs_job_id_response_200_job_configuration_return import (
            GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdResponse200JobConfigurationReturn,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: (
            GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdResponse200JobConfigurationReturn
            | Unset
        )
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GetSyncExternalsystemsExternalSystemIdJobconfigsJobIdResponse200JobConfigurationReturn.from_dict(
                _data
            )

        get_sync_externalsystems_external_system_id_jobconfigs_job_id_response_200 = (
            cls(
                data=data,
            )
        )

        get_sync_externalsystems_external_system_id_jobconfigs_job_id_response_200.additional_properties = d
        return (
            get_sync_externalsystems_external_system_id_jobconfigs_job_id_response_200
        )

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
