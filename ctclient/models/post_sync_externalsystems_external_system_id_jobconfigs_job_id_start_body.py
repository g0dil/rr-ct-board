from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="PostSyncExternalsystemsExternalSystemIdJobconfigsJobIdStartBody"
)


@_attrs_define
class PostSyncExternalsystemsExternalSystemIdJobconfigsJobIdStartBody:
    """
    Attributes:
        is_dry_run (bool | Unset): If `true` no records will be changed, deleted, linked, created. Default: `false`
        is_validation_only (bool | Unset): If `true` configuration is validated. Default: `false`
    """

    is_dry_run: bool | Unset = UNSET
    is_validation_only: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_dry_run = self.is_dry_run

        is_validation_only = self.is_validation_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_dry_run is not UNSET:
            field_dict["isDryRun"] = is_dry_run
        if is_validation_only is not UNSET:
            field_dict["isValidationOnly"] = is_validation_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_dry_run = d.pop("isDryRun", UNSET)

        is_validation_only = d.pop("isValidationOnly", UNSET)

        post_sync_externalsystems_external_system_id_jobconfigs_job_id_start_body = cls(
            is_dry_run=is_dry_run,
            is_validation_only=is_validation_only,
        )

        post_sync_externalsystems_external_system_id_jobconfigs_job_id_start_body.additional_properties = d
        return post_sync_externalsystems_external_system_id_jobconfigs_job_id_start_body

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
