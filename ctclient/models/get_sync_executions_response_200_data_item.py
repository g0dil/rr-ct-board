from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sync_executions_response_200_data_item_both import (
        GetSyncExecutionsResponse200DataItemBoth,
    )
    from ..models.get_sync_executions_response_200_data_item_es import (
        GetSyncExecutionsResponse200DataItemEs,
    )
    from ..models.get_sync_executions_response_200_data_item_master import (
        GetSyncExecutionsResponse200DataItemMaster,
    )


T = TypeVar("T", bound="GetSyncExecutionsResponse200DataItem")


@_attrs_define
class GetSyncExecutionsResponse200DataItem:
    """
    Attributes:
        end_date (str):
        execution_id (str):
        job_id (int):
        start_date (str):
        status (str):
        both (GetSyncExecutionsResponse200DataItemBoth | Unset):
        error_count (int | None | Unset):
        es (GetSyncExecutionsResponse200DataItemEs | Unset):
        is_dry_run (bool | Unset):
        master (GetSyncExecutionsResponse200DataItemMaster | Unset):
    """

    end_date: str
    execution_id: str
    job_id: int
    start_date: str
    status: str
    both: GetSyncExecutionsResponse200DataItemBoth | Unset = UNSET
    error_count: int | None | Unset = UNSET
    es: GetSyncExecutionsResponse200DataItemEs | Unset = UNSET
    is_dry_run: bool | Unset = UNSET
    master: GetSyncExecutionsResponse200DataItemMaster | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date

        execution_id = self.execution_id

        job_id = self.job_id

        start_date = self.start_date

        status = self.status

        both: dict[str, Any] | Unset = UNSET
        if not isinstance(self.both, Unset):
            both = self.both.to_dict()

        error_count: int | None | Unset
        if isinstance(self.error_count, Unset):
            error_count = UNSET
        else:
            error_count = self.error_count

        es: dict[str, Any] | Unset = UNSET
        if not isinstance(self.es, Unset):
            es = self.es.to_dict()

        is_dry_run = self.is_dry_run

        master: dict[str, Any] | Unset = UNSET
        if not isinstance(self.master, Unset):
            master = self.master.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endDate": end_date,
                "executionId": execution_id,
                "jobId": job_id,
                "startDate": start_date,
                "status": status,
            }
        )
        if both is not UNSET:
            field_dict["both"] = both
        if error_count is not UNSET:
            field_dict["errorCount"] = error_count
        if es is not UNSET:
            field_dict["es"] = es
        if is_dry_run is not UNSET:
            field_dict["isDryRun"] = is_dry_run
        if master is not UNSET:
            field_dict["master"] = master

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sync_executions_response_200_data_item_both import (
            GetSyncExecutionsResponse200DataItemBoth,
        )
        from ..models.get_sync_executions_response_200_data_item_es import (
            GetSyncExecutionsResponse200DataItemEs,
        )
        from ..models.get_sync_executions_response_200_data_item_master import (
            GetSyncExecutionsResponse200DataItemMaster,
        )

        d = dict(src_dict)
        end_date = d.pop("endDate")

        execution_id = d.pop("executionId")

        job_id = d.pop("jobId")

        start_date = d.pop("startDate")

        status = d.pop("status")

        _both = d.pop("both", UNSET)
        both: GetSyncExecutionsResponse200DataItemBoth | Unset
        if isinstance(_both, Unset):
            both = UNSET
        else:
            both = GetSyncExecutionsResponse200DataItemBoth.from_dict(_both)

        def _parse_error_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        error_count = _parse_error_count(d.pop("errorCount", UNSET))

        _es = d.pop("es", UNSET)
        es: GetSyncExecutionsResponse200DataItemEs | Unset
        if isinstance(_es, Unset):
            es = UNSET
        else:
            es = GetSyncExecutionsResponse200DataItemEs.from_dict(_es)

        is_dry_run = d.pop("isDryRun", UNSET)

        _master = d.pop("master", UNSET)
        master: GetSyncExecutionsResponse200DataItemMaster | Unset
        if isinstance(_master, Unset):
            master = UNSET
        else:
            master = GetSyncExecutionsResponse200DataItemMaster.from_dict(_master)

        get_sync_executions_response_200_data_item = cls(
            end_date=end_date,
            execution_id=execution_id,
            job_id=job_id,
            start_date=start_date,
            status=status,
            both=both,
            error_count=error_count,
            es=es,
            is_dry_run=is_dry_run,
            master=master,
        )

        get_sync_executions_response_200_data_item.additional_properties = d
        return get_sync_executions_response_200_data_item

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
