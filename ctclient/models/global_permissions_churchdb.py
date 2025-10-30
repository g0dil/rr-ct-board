from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GlobalPermissionsChurchdb")


@_attrs_define
class GlobalPermissionsChurchdb:
    """
    Attributes:
        administer_global_filters (bool):
        administer_groups (bool):
        complex_filter (bool):
        create_groups_of_grouptype (list[float]):
        create_person (bool):
        create_print_labels (bool):
        delete_group (list[float]):
        delete_groups_of_grouptype (list[float]):
        delete_persons (bool):
        edit_bulkletter (bool):
        edit_group (list[float]):
        edit_group_memberships (bool):
        edit_group_memberships_of_group (list[float]):
        edit_group_memberships_of_grouptype (list[float]):
        edit_groups_of_grouptype (list[float]):
        edit_masterdata (bool):
        edit_relations (bool):
        export_data (bool):
        pushpull_archive (bool):
        security_level_edit_own_data (list[float]):
        security_level_group (list[float]):
        security_level_person (list[float]):
        security_level_view_own_data (list[float]):
        send_sms (bool):
        view (bool):
        view_alldata (list[float]):
        view_archive (bool):
        view_birthdaylist (bool):
        view_comments (list[float]):
        view_group (list[float]):
        view_groups_of_grouptype (list[float]):
        view_memberliste (bool):
        view_person_history (bool):
        view_person_tags (bool):
        view_station (list[float]):
        view_statistics (bool):
        view_tags (bool):
        write_access (bool):
    """

    administer_global_filters: bool
    administer_groups: bool
    complex_filter: bool
    create_groups_of_grouptype: list[float]
    create_person: bool
    create_print_labels: bool
    delete_group: list[float]
    delete_groups_of_grouptype: list[float]
    delete_persons: bool
    edit_bulkletter: bool
    edit_group: list[float]
    edit_group_memberships: bool
    edit_group_memberships_of_group: list[float]
    edit_group_memberships_of_grouptype: list[float]
    edit_groups_of_grouptype: list[float]
    edit_masterdata: bool
    edit_relations: bool
    export_data: bool
    pushpull_archive: bool
    security_level_edit_own_data: list[float]
    security_level_group: list[float]
    security_level_person: list[float]
    security_level_view_own_data: list[float]
    send_sms: bool
    view: bool
    view_alldata: list[float]
    view_archive: bool
    view_birthdaylist: bool
    view_comments: list[float]
    view_group: list[float]
    view_groups_of_grouptype: list[float]
    view_memberliste: bool
    view_person_history: bool
    view_person_tags: bool
    view_station: list[float]
    view_statistics: bool
    view_tags: bool
    write_access: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        administer_global_filters = self.administer_global_filters

        administer_groups = self.administer_groups

        complex_filter = self.complex_filter

        create_groups_of_grouptype = self.create_groups_of_grouptype

        create_person = self.create_person

        create_print_labels = self.create_print_labels

        delete_group = self.delete_group

        delete_groups_of_grouptype = self.delete_groups_of_grouptype

        delete_persons = self.delete_persons

        edit_bulkletter = self.edit_bulkletter

        edit_group = self.edit_group

        edit_group_memberships = self.edit_group_memberships

        edit_group_memberships_of_group = self.edit_group_memberships_of_group

        edit_group_memberships_of_grouptype = self.edit_group_memberships_of_grouptype

        edit_groups_of_grouptype = self.edit_groups_of_grouptype

        edit_masterdata = self.edit_masterdata

        edit_relations = self.edit_relations

        export_data = self.export_data

        pushpull_archive = self.pushpull_archive

        security_level_edit_own_data = self.security_level_edit_own_data

        security_level_group = self.security_level_group

        security_level_person = self.security_level_person

        security_level_view_own_data = self.security_level_view_own_data

        send_sms = self.send_sms

        view = self.view

        view_alldata = self.view_alldata

        view_archive = self.view_archive

        view_birthdaylist = self.view_birthdaylist

        view_comments = self.view_comments

        view_group = self.view_group

        view_groups_of_grouptype = self.view_groups_of_grouptype

        view_memberliste = self.view_memberliste

        view_person_history = self.view_person_history

        view_person_tags = self.view_person_tags

        view_station = self.view_station

        view_statistics = self.view_statistics

        view_tags = self.view_tags

        write_access = self.write_access

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "administer global filters": administer_global_filters,
                "administer groups": administer_groups,
                "complex filter": complex_filter,
                "create groups of grouptype": create_groups_of_grouptype,
                "create person": create_person,
                "create print labels": create_print_labels,
                "delete group": delete_group,
                "delete groups of grouptype": delete_groups_of_grouptype,
                "delete persons": delete_persons,
                "edit bulkletter": edit_bulkletter,
                "edit group": edit_group,
                "edit group memberships": edit_group_memberships,
                "edit group memberships of group": edit_group_memberships_of_group,
                "edit group memberships of grouptype": edit_group_memberships_of_grouptype,
                "edit groups of grouptype": edit_groups_of_grouptype,
                "edit masterdata": edit_masterdata,
                "edit relations": edit_relations,
                "export data": export_data,
                "push/pull archive": pushpull_archive,
                "security level edit own data": security_level_edit_own_data,
                "security level group": security_level_group,
                "security level person": security_level_person,
                "security level view own data": security_level_view_own_data,
                "send sms": send_sms,
                "view": view,
                "view alldata": view_alldata,
                "view archive": view_archive,
                "view birthdaylist": view_birthdaylist,
                "view comments": view_comments,
                "view group": view_group,
                "view groups of grouptype": view_groups_of_grouptype,
                "view memberliste": view_memberliste,
                "view person history": view_person_history,
                "view person tags": view_person_tags,
                "view station": view_station,
                "view statistics": view_statistics,
                "view tags": view_tags,
                "write access": write_access,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        administer_global_filters = d.pop("administer global filters")

        administer_groups = d.pop("administer groups")

        complex_filter = d.pop("complex filter")

        create_groups_of_grouptype = cast(
            list[float], d.pop("create groups of grouptype")
        )

        create_person = d.pop("create person")

        create_print_labels = d.pop("create print labels")

        delete_group = cast(list[float], d.pop("delete group"))

        delete_groups_of_grouptype = cast(
            list[float], d.pop("delete groups of grouptype")
        )

        delete_persons = d.pop("delete persons")

        edit_bulkletter = d.pop("edit bulkletter")

        edit_group = cast(list[float], d.pop("edit group"))

        edit_group_memberships = d.pop("edit group memberships")

        edit_group_memberships_of_group = cast(
            list[float], d.pop("edit group memberships of group")
        )

        edit_group_memberships_of_grouptype = cast(
            list[float], d.pop("edit group memberships of grouptype")
        )

        edit_groups_of_grouptype = cast(list[float], d.pop("edit groups of grouptype"))

        edit_masterdata = d.pop("edit masterdata")

        edit_relations = d.pop("edit relations")

        export_data = d.pop("export data")

        pushpull_archive = d.pop("push/pull archive")

        security_level_edit_own_data = cast(
            list[float], d.pop("security level edit own data")
        )

        security_level_group = cast(list[float], d.pop("security level group"))

        security_level_person = cast(list[float], d.pop("security level person"))

        security_level_view_own_data = cast(
            list[float], d.pop("security level view own data")
        )

        send_sms = d.pop("send sms")

        view = d.pop("view")

        view_alldata = cast(list[float], d.pop("view alldata"))

        view_archive = d.pop("view archive")

        view_birthdaylist = d.pop("view birthdaylist")

        view_comments = cast(list[float], d.pop("view comments"))

        view_group = cast(list[float], d.pop("view group"))

        view_groups_of_grouptype = cast(list[float], d.pop("view groups of grouptype"))

        view_memberliste = d.pop("view memberliste")

        view_person_history = d.pop("view person history")

        view_person_tags = d.pop("view person tags")

        view_station = cast(list[float], d.pop("view station"))

        view_statistics = d.pop("view statistics")

        view_tags = d.pop("view tags")

        write_access = d.pop("write access")

        global_permissions_churchdb = cls(
            administer_global_filters=administer_global_filters,
            administer_groups=administer_groups,
            complex_filter=complex_filter,
            create_groups_of_grouptype=create_groups_of_grouptype,
            create_person=create_person,
            create_print_labels=create_print_labels,
            delete_group=delete_group,
            delete_groups_of_grouptype=delete_groups_of_grouptype,
            delete_persons=delete_persons,
            edit_bulkletter=edit_bulkletter,
            edit_group=edit_group,
            edit_group_memberships=edit_group_memberships,
            edit_group_memberships_of_group=edit_group_memberships_of_group,
            edit_group_memberships_of_grouptype=edit_group_memberships_of_grouptype,
            edit_groups_of_grouptype=edit_groups_of_grouptype,
            edit_masterdata=edit_masterdata,
            edit_relations=edit_relations,
            export_data=export_data,
            pushpull_archive=pushpull_archive,
            security_level_edit_own_data=security_level_edit_own_data,
            security_level_group=security_level_group,
            security_level_person=security_level_person,
            security_level_view_own_data=security_level_view_own_data,
            send_sms=send_sms,
            view=view,
            view_alldata=view_alldata,
            view_archive=view_archive,
            view_birthdaylist=view_birthdaylist,
            view_comments=view_comments,
            view_group=view_group,
            view_groups_of_grouptype=view_groups_of_grouptype,
            view_memberliste=view_memberliste,
            view_person_history=view_person_history,
            view_person_tags=view_person_tags,
            view_station=view_station,
            view_statistics=view_statistics,
            view_tags=view_tags,
            write_access=write_access,
        )

        global_permissions_churchdb.additional_properties = d
        return global_permissions_churchdb

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
