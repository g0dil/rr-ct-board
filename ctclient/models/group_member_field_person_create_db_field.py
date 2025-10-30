from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_member_field_person_create_db_field_field_category import (
        GroupMemberFieldPersonCreateDbFieldFieldCategory,
    )
    from ..models.group_member_field_person_create_db_field_field_type import (
        GroupMemberFieldPersonCreateDbFieldFieldType,
    )
    from ..models.group_member_field_person_create_db_field_options_item import (
        GroupMemberFieldPersonCreateDbFieldOptionsItem,
    )


T = TypeVar("T", bound="GroupMemberFieldPersonCreateDbField")


@_attrs_define
class GroupMemberFieldPersonCreateDbField:
    """
    Attributes:
        delete_on_archive (bool):
        is_active (bool):
        is_new_person_field (bool):
        line_ending (str):
        name (str):
        security_level (int):
        sort_key (int):
        use_as_placeholder (bool):
        column (str):
        created_by_church (bool):
        field_category (GroupMemberFieldPersonCreateDbFieldFieldCategory):
        field_type (GroupMemberFieldPersonCreateDbFieldFieldType):
        hide_in_frontend (bool):
        id (int):
        is_basic_info (bool):
        is_not_configurable (bool):
        is_nullable (bool):
        key (str):
        not_configurable (bool):
        nullable (bool):
        length (int | None | Unset):
        shorty (str | Unset):
        options (list[GroupMemberFieldPersonCreateDbFieldOptionsItem] | Unset):
    """

    delete_on_archive: bool
    is_active: bool
    is_new_person_field: bool
    line_ending: str
    name: str
    security_level: int
    sort_key: int
    use_as_placeholder: bool
    column: str
    created_by_church: bool
    field_category: GroupMemberFieldPersonCreateDbFieldFieldCategory
    field_type: GroupMemberFieldPersonCreateDbFieldFieldType
    hide_in_frontend: bool
    id: int
    is_basic_info: bool
    is_not_configurable: bool
    is_nullable: bool
    key: str
    not_configurable: bool
    nullable: bool
    length: int | None | Unset = UNSET
    shorty: str | Unset = UNSET
    options: list[GroupMemberFieldPersonCreateDbFieldOptionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_on_archive = self.delete_on_archive

        is_active = self.is_active

        is_new_person_field = self.is_new_person_field

        line_ending = self.line_ending

        name = self.name

        security_level = self.security_level

        sort_key = self.sort_key

        use_as_placeholder = self.use_as_placeholder

        column = self.column

        created_by_church = self.created_by_church

        field_category = self.field_category.to_dict()

        field_type = self.field_type.to_dict()

        hide_in_frontend = self.hide_in_frontend

        id = self.id

        is_basic_info = self.is_basic_info

        is_not_configurable = self.is_not_configurable

        is_nullable = self.is_nullable

        key = self.key

        not_configurable = self.not_configurable

        nullable = self.nullable

        length: int | None | Unset
        if isinstance(self.length, Unset):
            length = UNSET
        else:
            length = self.length

        shorty = self.shorty

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deleteOnArchive": delete_on_archive,
                "isActive": is_active,
                "isNewPersonField": is_new_person_field,
                "lineEnding": line_ending,
                "name": name,
                "securityLevel": security_level,
                "sortKey": sort_key,
                "useAsPlaceholder": use_as_placeholder,
                "column": column,
                "createdByChurch": created_by_church,
                "fieldCategory": field_category,
                "fieldType": field_type,
                "hideInFrontend": hide_in_frontend,
                "id": id,
                "isBasicInfo": is_basic_info,
                "isNotConfigurable": is_not_configurable,
                "isNullable": is_nullable,
                "key": key,
                "notConfigurable": not_configurable,
                "nullable": nullable,
            }
        )
        if length is not UNSET:
            field_dict["length"] = length
        if shorty is not UNSET:
            field_dict["shorty"] = shorty
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_member_field_person_create_db_field_field_category import (
            GroupMemberFieldPersonCreateDbFieldFieldCategory,
        )
        from ..models.group_member_field_person_create_db_field_field_type import (
            GroupMemberFieldPersonCreateDbFieldFieldType,
        )
        from ..models.group_member_field_person_create_db_field_options_item import (
            GroupMemberFieldPersonCreateDbFieldOptionsItem,
        )

        d = dict(src_dict)
        delete_on_archive = d.pop("deleteOnArchive")

        is_active = d.pop("isActive")

        is_new_person_field = d.pop("isNewPersonField")

        line_ending = d.pop("lineEnding")

        name = d.pop("name")

        security_level = d.pop("securityLevel")

        sort_key = d.pop("sortKey")

        use_as_placeholder = d.pop("useAsPlaceholder")

        column = d.pop("column")

        created_by_church = d.pop("createdByChurch")

        field_category = GroupMemberFieldPersonCreateDbFieldFieldCategory.from_dict(
            d.pop("fieldCategory")
        )

        field_type = GroupMemberFieldPersonCreateDbFieldFieldType.from_dict(
            d.pop("fieldType")
        )

        hide_in_frontend = d.pop("hideInFrontend")

        id = d.pop("id")

        is_basic_info = d.pop("isBasicInfo")

        is_not_configurable = d.pop("isNotConfigurable")

        is_nullable = d.pop("isNullable")

        key = d.pop("key")

        not_configurable = d.pop("notConfigurable")

        nullable = d.pop("nullable")

        def _parse_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        length = _parse_length(d.pop("length", UNSET))

        shorty = d.pop("shorty", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = GroupMemberFieldPersonCreateDbFieldOptionsItem.from_dict(
                options_item_data
            )

            options.append(options_item)

        group_member_field_person_create_db_field = cls(
            delete_on_archive=delete_on_archive,
            is_active=is_active,
            is_new_person_field=is_new_person_field,
            line_ending=line_ending,
            name=name,
            security_level=security_level,
            sort_key=sort_key,
            use_as_placeholder=use_as_placeholder,
            column=column,
            created_by_church=created_by_church,
            field_category=field_category,
            field_type=field_type,
            hide_in_frontend=hide_in_frontend,
            id=id,
            is_basic_info=is_basic_info,
            is_not_configurable=is_not_configurable,
            is_nullable=is_nullable,
            key=key,
            not_configurable=not_configurable,
            nullable=nullable,
            length=length,
            shorty=shorty,
            options=options,
        )

        group_member_field_person_create_db_field.additional_properties = d
        return group_member_field_person_create_db_field

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
