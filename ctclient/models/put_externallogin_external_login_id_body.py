from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutExternalloginExternalLoginIdBody")


@_attrs_define
class PutExternalloginExternalLoginIdBody:
    """
    Attributes:
        name (str):  Example: Nextcloud.
        new_person_campus_id (int):
        new_person_department_id (int):
        new_person_status_id (int):
        type_ (str):  Example: oauth.
        id (int):  Example: 3.
        config (Any | Unset): config options for the external login type
        create_new_person (bool | Unset):
        update_data_on_login (bool | Unset):
    """

    name: str
    new_person_campus_id: int
    new_person_department_id: int
    new_person_status_id: int
    type_: str
    id: int
    config: Any | Unset = UNSET
    create_new_person: bool | Unset = UNSET
    update_data_on_login: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        new_person_campus_id = self.new_person_campus_id

        new_person_department_id = self.new_person_department_id

        new_person_status_id = self.new_person_status_id

        type_ = self.type_

        id = self.id

        config = self.config

        create_new_person = self.create_new_person

        update_data_on_login = self.update_data_on_login

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "newPersonCampusId": new_person_campus_id,
                "newPersonDepartmentId": new_person_department_id,
                "newPersonStatusId": new_person_status_id,
                "type": type_,
                "id": id,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if create_new_person is not UNSET:
            field_dict["createNewPerson"] = create_new_person
        if update_data_on_login is not UNSET:
            field_dict["updateDataOnLogin"] = update_data_on_login

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        new_person_campus_id = d.pop("newPersonCampusId")

        new_person_department_id = d.pop("newPersonDepartmentId")

        new_person_status_id = d.pop("newPersonStatusId")

        type_ = d.pop("type")

        id = d.pop("id")

        config = d.pop("config", UNSET)

        create_new_person = d.pop("createNewPerson", UNSET)

        update_data_on_login = d.pop("updateDataOnLogin", UNSET)

        put_externallogin_external_login_id_body = cls(
            name=name,
            new_person_campus_id=new_person_campus_id,
            new_person_department_id=new_person_department_id,
            new_person_status_id=new_person_status_id,
            type_=type_,
            id=id,
            config=config,
            create_new_person=create_new_person,
            update_data_on_login=update_data_on_login,
        )

        put_externallogin_external_login_id_body.additional_properties = d
        return put_externallogin_external_login_id_body

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
