from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPermissionsInternalGroupsGroupIdResponse200DataChurchdb")


@_attrs_define
class GetPermissionsInternalGroupsGroupIdResponse200DataChurchdb:
    """Group Internal Permission, which Affect a Person

    Attributes:
        add_person (bool | Unset):
        admin_automatic_emails (bool | Unset):
        admin_followup (bool | Unset):
        admin_group_chat (bool | Unset):
        admin_group_fields (bool | Unset):
        admin_group_member_fields (bool | Unset):
        admin_meetings (bool | Unset):
        admin_posts (bool | Unset):
        admin_routines (bool | Unset):
        create_group (bool | Unset):
        create_notes (bool | Unset):
        create_post_group_intern (bool | Unset):
        create_post_group_visible (bool | Unset):
        do_followup (bool | Unset):
        do_group_meeting (bool | Unset):
        edit_basic_group_memberships (bool | Unset):
        edit_group_basic_settings (bool | Unset):
        edit_group_hierarchy (bool | Unset):
        edit_group_infos (bool | Unset):
        edit_group_member_fields (float | Unset):
        edit_group_memberships (bool | Unset):
        edit_own_group_member_fields (float | Unset):
        edit_own_groupmemberfields (bool | Unset):
        edit_person_fields_of_group_members (float | Unset):
        edit_persons (bool | Unset):
        export_group_members (bool | Unset):
        get_emails (bool | Unset):
        invite_person (bool | Unset):
        mail_group_members (bool | Unset):
        remove_from_group (bool | Unset):
        see_group (float | Unset):
        see_group_member_fields (float | Unset):
        see_group_tags (bool | Unset):
        see_groupmemberfields (float | Unset):
        see_hidden_group (bool | Unset):
        see_own_group_member_fields (float | Unset):
        see_persons (float | Unset):
        see_tags (bool | Unset):
        view_history (bool | Unset):
    """

    add_person: bool | Unset = UNSET
    admin_automatic_emails: bool | Unset = UNSET
    admin_followup: bool | Unset = UNSET
    admin_group_chat: bool | Unset = UNSET
    admin_group_fields: bool | Unset = UNSET
    admin_group_member_fields: bool | Unset = UNSET
    admin_meetings: bool | Unset = UNSET
    admin_posts: bool | Unset = UNSET
    admin_routines: bool | Unset = UNSET
    create_group: bool | Unset = UNSET
    create_notes: bool | Unset = UNSET
    create_post_group_intern: bool | Unset = UNSET
    create_post_group_visible: bool | Unset = UNSET
    do_followup: bool | Unset = UNSET
    do_group_meeting: bool | Unset = UNSET
    edit_basic_group_memberships: bool | Unset = UNSET
    edit_group_basic_settings: bool | Unset = UNSET
    edit_group_hierarchy: bool | Unset = UNSET
    edit_group_infos: bool | Unset = UNSET
    edit_group_member_fields: float | Unset = UNSET
    edit_group_memberships: bool | Unset = UNSET
    edit_own_group_member_fields: float | Unset = UNSET
    edit_own_groupmemberfields: bool | Unset = UNSET
    edit_person_fields_of_group_members: float | Unset = UNSET
    edit_persons: bool | Unset = UNSET
    export_group_members: bool | Unset = UNSET
    get_emails: bool | Unset = UNSET
    invite_person: bool | Unset = UNSET
    mail_group_members: bool | Unset = UNSET
    remove_from_group: bool | Unset = UNSET
    see_group: float | Unset = UNSET
    see_group_member_fields: float | Unset = UNSET
    see_group_tags: bool | Unset = UNSET
    see_groupmemberfields: float | Unset = UNSET
    see_hidden_group: bool | Unset = UNSET
    see_own_group_member_fields: float | Unset = UNSET
    see_persons: float | Unset = UNSET
    see_tags: bool | Unset = UNSET
    view_history: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_person = self.add_person

        admin_automatic_emails = self.admin_automatic_emails

        admin_followup = self.admin_followup

        admin_group_chat = self.admin_group_chat

        admin_group_fields = self.admin_group_fields

        admin_group_member_fields = self.admin_group_member_fields

        admin_meetings = self.admin_meetings

        admin_posts = self.admin_posts

        admin_routines = self.admin_routines

        create_group = self.create_group

        create_notes = self.create_notes

        create_post_group_intern = self.create_post_group_intern

        create_post_group_visible = self.create_post_group_visible

        do_followup = self.do_followup

        do_group_meeting = self.do_group_meeting

        edit_basic_group_memberships = self.edit_basic_group_memberships

        edit_group_basic_settings = self.edit_group_basic_settings

        edit_group_hierarchy = self.edit_group_hierarchy

        edit_group_infos = self.edit_group_infos

        edit_group_member_fields = self.edit_group_member_fields

        edit_group_memberships = self.edit_group_memberships

        edit_own_group_member_fields = self.edit_own_group_member_fields

        edit_own_groupmemberfields = self.edit_own_groupmemberfields

        edit_person_fields_of_group_members = self.edit_person_fields_of_group_members

        edit_persons = self.edit_persons

        export_group_members = self.export_group_members

        get_emails = self.get_emails

        invite_person = self.invite_person

        mail_group_members = self.mail_group_members

        remove_from_group = self.remove_from_group

        see_group = self.see_group

        see_group_member_fields = self.see_group_member_fields

        see_group_tags = self.see_group_tags

        see_groupmemberfields = self.see_groupmemberfields

        see_hidden_group = self.see_hidden_group

        see_own_group_member_fields = self.see_own_group_member_fields

        see_persons = self.see_persons

        see_tags = self.see_tags

        view_history = self.view_history

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_person is not UNSET:
            field_dict["+add person"] = add_person
        if admin_automatic_emails is not UNSET:
            field_dict["+admin automatic emails"] = admin_automatic_emails
        if admin_followup is not UNSET:
            field_dict["+admin followup"] = admin_followup
        if admin_group_chat is not UNSET:
            field_dict["+admin group chat"] = admin_group_chat
        if admin_group_fields is not UNSET:
            field_dict["+admin group fields"] = admin_group_fields
        if admin_group_member_fields is not UNSET:
            field_dict["+admin group member fields"] = admin_group_member_fields
        if admin_meetings is not UNSET:
            field_dict["+admin meetings"] = admin_meetings
        if admin_posts is not UNSET:
            field_dict["+admin posts"] = admin_posts
        if admin_routines is not UNSET:
            field_dict["+admin routines"] = admin_routines
        if create_group is not UNSET:
            field_dict["+create group"] = create_group
        if create_notes is not UNSET:
            field_dict["+create notes"] = create_notes
        if create_post_group_intern is not UNSET:
            field_dict["+create post group intern"] = create_post_group_intern
        if create_post_group_visible is not UNSET:
            field_dict["+create post group visible"] = create_post_group_visible
        if do_followup is not UNSET:
            field_dict["+do followup"] = do_followup
        if do_group_meeting is not UNSET:
            field_dict["+do group meeting"] = do_group_meeting
        if edit_basic_group_memberships is not UNSET:
            field_dict["+edit basic group memberships"] = edit_basic_group_memberships
        if edit_group_basic_settings is not UNSET:
            field_dict["+edit group basic settings"] = edit_group_basic_settings
        if edit_group_hierarchy is not UNSET:
            field_dict["+edit group hierarchy"] = edit_group_hierarchy
        if edit_group_infos is not UNSET:
            field_dict["+edit group infos"] = edit_group_infos
        if edit_group_member_fields is not UNSET:
            field_dict["+edit group member fields"] = edit_group_member_fields
        if edit_group_memberships is not UNSET:
            field_dict["+edit group memberships"] = edit_group_memberships
        if edit_own_group_member_fields is not UNSET:
            field_dict["+edit own group member fields"] = edit_own_group_member_fields
        if edit_own_groupmemberfields is not UNSET:
            field_dict["+edit own groupmemberfields"] = edit_own_groupmemberfields
        if edit_person_fields_of_group_members is not UNSET:
            field_dict["+edit person fields of group members"] = (
                edit_person_fields_of_group_members
            )
        if edit_persons is not UNSET:
            field_dict["+edit persons"] = edit_persons
        if export_group_members is not UNSET:
            field_dict["+export group members"] = export_group_members
        if get_emails is not UNSET:
            field_dict["+get emails"] = get_emails
        if invite_person is not UNSET:
            field_dict["+invite person"] = invite_person
        if mail_group_members is not UNSET:
            field_dict["+mail group members"] = mail_group_members
        if remove_from_group is not UNSET:
            field_dict["+remove from group"] = remove_from_group
        if see_group is not UNSET:
            field_dict["+see group"] = see_group
        if see_group_member_fields is not UNSET:
            field_dict["+see group member fields"] = see_group_member_fields
        if see_group_tags is not UNSET:
            field_dict["+see group tags"] = see_group_tags
        if see_groupmemberfields is not UNSET:
            field_dict["+see groupmemberfields"] = see_groupmemberfields
        if see_hidden_group is not UNSET:
            field_dict["+see hidden group"] = see_hidden_group
        if see_own_group_member_fields is not UNSET:
            field_dict["+see own group member fields"] = see_own_group_member_fields
        if see_persons is not UNSET:
            field_dict["+see persons"] = see_persons
        if see_tags is not UNSET:
            field_dict["+see tags"] = see_tags
        if view_history is not UNSET:
            field_dict["+view history"] = view_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        add_person = d.pop("+add person", UNSET)

        admin_automatic_emails = d.pop("+admin automatic emails", UNSET)

        admin_followup = d.pop("+admin followup", UNSET)

        admin_group_chat = d.pop("+admin group chat", UNSET)

        admin_group_fields = d.pop("+admin group fields", UNSET)

        admin_group_member_fields = d.pop("+admin group member fields", UNSET)

        admin_meetings = d.pop("+admin meetings", UNSET)

        admin_posts = d.pop("+admin posts", UNSET)

        admin_routines = d.pop("+admin routines", UNSET)

        create_group = d.pop("+create group", UNSET)

        create_notes = d.pop("+create notes", UNSET)

        create_post_group_intern = d.pop("+create post group intern", UNSET)

        create_post_group_visible = d.pop("+create post group visible", UNSET)

        do_followup = d.pop("+do followup", UNSET)

        do_group_meeting = d.pop("+do group meeting", UNSET)

        edit_basic_group_memberships = d.pop("+edit basic group memberships", UNSET)

        edit_group_basic_settings = d.pop("+edit group basic settings", UNSET)

        edit_group_hierarchy = d.pop("+edit group hierarchy", UNSET)

        edit_group_infos = d.pop("+edit group infos", UNSET)

        edit_group_member_fields = d.pop("+edit group member fields", UNSET)

        edit_group_memberships = d.pop("+edit group memberships", UNSET)

        edit_own_group_member_fields = d.pop("+edit own group member fields", UNSET)

        edit_own_groupmemberfields = d.pop("+edit own groupmemberfields", UNSET)

        edit_person_fields_of_group_members = d.pop(
            "+edit person fields of group members", UNSET
        )

        edit_persons = d.pop("+edit persons", UNSET)

        export_group_members = d.pop("+export group members", UNSET)

        get_emails = d.pop("+get emails", UNSET)

        invite_person = d.pop("+invite person", UNSET)

        mail_group_members = d.pop("+mail group members", UNSET)

        remove_from_group = d.pop("+remove from group", UNSET)

        see_group = d.pop("+see group", UNSET)

        see_group_member_fields = d.pop("+see group member fields", UNSET)

        see_group_tags = d.pop("+see group tags", UNSET)

        see_groupmemberfields = d.pop("+see groupmemberfields", UNSET)

        see_hidden_group = d.pop("+see hidden group", UNSET)

        see_own_group_member_fields = d.pop("+see own group member fields", UNSET)

        see_persons = d.pop("+see persons", UNSET)

        see_tags = d.pop("+see tags", UNSET)

        view_history = d.pop("+view history", UNSET)

        get_permissions_internal_groups_group_id_response_200_data_churchdb = cls(
            add_person=add_person,
            admin_automatic_emails=admin_automatic_emails,
            admin_followup=admin_followup,
            admin_group_chat=admin_group_chat,
            admin_group_fields=admin_group_fields,
            admin_group_member_fields=admin_group_member_fields,
            admin_meetings=admin_meetings,
            admin_posts=admin_posts,
            admin_routines=admin_routines,
            create_group=create_group,
            create_notes=create_notes,
            create_post_group_intern=create_post_group_intern,
            create_post_group_visible=create_post_group_visible,
            do_followup=do_followup,
            do_group_meeting=do_group_meeting,
            edit_basic_group_memberships=edit_basic_group_memberships,
            edit_group_basic_settings=edit_group_basic_settings,
            edit_group_hierarchy=edit_group_hierarchy,
            edit_group_infos=edit_group_infos,
            edit_group_member_fields=edit_group_member_fields,
            edit_group_memberships=edit_group_memberships,
            edit_own_group_member_fields=edit_own_group_member_fields,
            edit_own_groupmemberfields=edit_own_groupmemberfields,
            edit_person_fields_of_group_members=edit_person_fields_of_group_members,
            edit_persons=edit_persons,
            export_group_members=export_group_members,
            get_emails=get_emails,
            invite_person=invite_person,
            mail_group_members=mail_group_members,
            remove_from_group=remove_from_group,
            see_group=see_group,
            see_group_member_fields=see_group_member_fields,
            see_group_tags=see_group_tags,
            see_groupmemberfields=see_groupmemberfields,
            see_hidden_group=see_hidden_group,
            see_own_group_member_fields=see_own_group_member_fields,
            see_persons=see_persons,
            see_tags=see_tags,
            view_history=view_history,
        )

        get_permissions_internal_groups_group_id_response_200_data_churchdb.additional_properties = d
        return get_permissions_internal_groups_group_id_response_200_data_churchdb

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
