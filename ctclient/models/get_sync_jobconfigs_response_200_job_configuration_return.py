from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sync_jobconfigs_response_200_job_configuration_return_create_defaults_es import (
        GetSyncJobconfigsResponse200JobConfigurationReturnCreateDefaultsES,
    )
    from ..models.get_sync_jobconfigs_response_200_job_configuration_return_create_defaults_master import (
        GetSyncJobconfigsResponse200JobConfigurationReturnCreateDefaultsMaster,
    )
    from ..models.get_sync_jobconfigs_response_200_job_configuration_return_external_system import (
        GetSyncJobconfigsResponse200JobConfigurationReturnExternalSystem,
    )


T = TypeVar("T", bound="GetSyncJobconfigsResponse200JobConfigurationReturn")


@_attrs_define
class GetSyncJobconfigsResponse200JobConfigurationReturn:
    """
    Attributes:
        auto_schedule_enabled (bool):
        domain_type (str):
        name (str):
        create_behavior_es (str | Unset):
        create_behavior_master (str | Unset):
        create_defaults_es (GetSyncJobconfigsResponse200JobConfigurationReturnCreateDefaultsES | Unset):
        create_defaults_master (GetSyncJobconfigsResponse200JobConfigurationReturnCreateDefaultsMaster | Unset):
        delete_behavior_es (str | Unset):
        delete_behavior_master (str | Unset):
        external_system (GetSyncJobconfigsResponse200JobConfigurationReturnExternalSystem | Unset):
        id (int | Unset):
        link_behavior (str | Unset):
        link_data (str | Unset):
        update_behavior (str | Unset):
        update_data (str | Unset):
    """

    auto_schedule_enabled: bool
    domain_type: str
    name: str
    create_behavior_es: str | Unset = UNSET
    create_behavior_master: str | Unset = UNSET
    create_defaults_es: (
        GetSyncJobconfigsResponse200JobConfigurationReturnCreateDefaultsES | Unset
    ) = UNSET
    create_defaults_master: (
        GetSyncJobconfigsResponse200JobConfigurationReturnCreateDefaultsMaster | Unset
    ) = UNSET
    delete_behavior_es: str | Unset = UNSET
    delete_behavior_master: str | Unset = UNSET
    external_system: (
        GetSyncJobconfigsResponse200JobConfigurationReturnExternalSystem | Unset
    ) = UNSET
    id: int | Unset = UNSET
    link_behavior: str | Unset = UNSET
    link_data: str | Unset = UNSET
    update_behavior: str | Unset = UNSET
    update_data: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_schedule_enabled = self.auto_schedule_enabled

        domain_type = self.domain_type

        name = self.name

        create_behavior_es = self.create_behavior_es

        create_behavior_master = self.create_behavior_master

        create_defaults_es: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_defaults_es, Unset):
            create_defaults_es = self.create_defaults_es.to_dict()

        create_defaults_master: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_defaults_master, Unset):
            create_defaults_master = self.create_defaults_master.to_dict()

        delete_behavior_es = self.delete_behavior_es

        delete_behavior_master = self.delete_behavior_master

        external_system: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_system, Unset):
            external_system = self.external_system.to_dict()

        id = self.id

        link_behavior = self.link_behavior

        link_data = self.link_data

        update_behavior = self.update_behavior

        update_data = self.update_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoScheduleEnabled": auto_schedule_enabled,
                "domainType": domain_type,
                "name": name,
            }
        )
        if create_behavior_es is not UNSET:
            field_dict["createBehaviorES"] = create_behavior_es
        if create_behavior_master is not UNSET:
            field_dict["createBehaviorMaster"] = create_behavior_master
        if create_defaults_es is not UNSET:
            field_dict["createDefaultsES"] = create_defaults_es
        if create_defaults_master is not UNSET:
            field_dict["createDefaultsMaster"] = create_defaults_master
        if delete_behavior_es is not UNSET:
            field_dict["deleteBehaviorES"] = delete_behavior_es
        if delete_behavior_master is not UNSET:
            field_dict["deleteBehaviorMaster"] = delete_behavior_master
        if external_system is not UNSET:
            field_dict["externalSystem"] = external_system
        if id is not UNSET:
            field_dict["id"] = id
        if link_behavior is not UNSET:
            field_dict["linkBehavior"] = link_behavior
        if link_data is not UNSET:
            field_dict["linkData"] = link_data
        if update_behavior is not UNSET:
            field_dict["updateBehavior"] = update_behavior
        if update_data is not UNSET:
            field_dict["updateData"] = update_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sync_jobconfigs_response_200_job_configuration_return_create_defaults_es import (
            GetSyncJobconfigsResponse200JobConfigurationReturnCreateDefaultsES,
        )
        from ..models.get_sync_jobconfigs_response_200_job_configuration_return_create_defaults_master import (
            GetSyncJobconfigsResponse200JobConfigurationReturnCreateDefaultsMaster,
        )
        from ..models.get_sync_jobconfigs_response_200_job_configuration_return_external_system import (
            GetSyncJobconfigsResponse200JobConfigurationReturnExternalSystem,
        )

        d = dict(src_dict)
        auto_schedule_enabled = d.pop("autoScheduleEnabled")

        domain_type = d.pop("domainType")

        name = d.pop("name")

        create_behavior_es = d.pop("createBehaviorES", UNSET)

        create_behavior_master = d.pop("createBehaviorMaster", UNSET)

        _create_defaults_es = d.pop("createDefaultsES", UNSET)
        create_defaults_es: (
            GetSyncJobconfigsResponse200JobConfigurationReturnCreateDefaultsES | Unset
        )
        if isinstance(_create_defaults_es, Unset):
            create_defaults_es = UNSET
        else:
            create_defaults_es = GetSyncJobconfigsResponse200JobConfigurationReturnCreateDefaultsES.from_dict(
                _create_defaults_es
            )

        _create_defaults_master = d.pop("createDefaultsMaster", UNSET)
        create_defaults_master: (
            GetSyncJobconfigsResponse200JobConfigurationReturnCreateDefaultsMaster
            | Unset
        )
        if isinstance(_create_defaults_master, Unset):
            create_defaults_master = UNSET
        else:
            create_defaults_master = GetSyncJobconfigsResponse200JobConfigurationReturnCreateDefaultsMaster.from_dict(
                _create_defaults_master
            )

        delete_behavior_es = d.pop("deleteBehaviorES", UNSET)

        delete_behavior_master = d.pop("deleteBehaviorMaster", UNSET)

        _external_system = d.pop("externalSystem", UNSET)
        external_system: (
            GetSyncJobconfigsResponse200JobConfigurationReturnExternalSystem | Unset
        )
        if isinstance(_external_system, Unset):
            external_system = UNSET
        else:
            external_system = GetSyncJobconfigsResponse200JobConfigurationReturnExternalSystem.from_dict(
                _external_system
            )

        id = d.pop("id", UNSET)

        link_behavior = d.pop("linkBehavior", UNSET)

        link_data = d.pop("linkData", UNSET)

        update_behavior = d.pop("updateBehavior", UNSET)

        update_data = d.pop("updateData", UNSET)

        get_sync_jobconfigs_response_200_job_configuration_return = cls(
            auto_schedule_enabled=auto_schedule_enabled,
            domain_type=domain_type,
            name=name,
            create_behavior_es=create_behavior_es,
            create_behavior_master=create_behavior_master,
            create_defaults_es=create_defaults_es,
            create_defaults_master=create_defaults_master,
            delete_behavior_es=delete_behavior_es,
            delete_behavior_master=delete_behavior_master,
            external_system=external_system,
            id=id,
            link_behavior=link_behavior,
            link_data=link_data,
            update_behavior=update_behavior,
            update_data=update_data,
        )

        get_sync_jobconfigs_response_200_job_configuration_return.additional_properties = d
        return get_sync_jobconfigs_response_200_job_configuration_return

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
