from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.patch_group_response_200_data_settings_default_post_notification_scope_type_1 import (
    PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType1,
)
from ..models.patch_group_response_200_data_settings_default_post_notification_scope_type_2_type_1 import (
    PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType2Type1,
)
from ..models.patch_group_response_200_data_settings_default_post_notification_scope_type_3_type_1 import (
    PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType3Type1,
)
from ..models.patch_group_response_200_data_settings_default_post_visibility import (
    PatchGroupResponse200DataSettingsDefaultPostVisibility,
)
from ..models.patch_group_response_200_data_settings_dynamic_group_status_type_1 import (
    PatchGroupResponse200DataSettingsDynamicGroupStatusType1,
)
from ..models.patch_group_response_200_data_settings_dynamic_group_status_type_2_type_1 import (
    PatchGroupResponse200DataSettingsDynamicGroupStatusType2Type1,
)
from ..models.patch_group_response_200_data_settings_dynamic_group_status_type_3_type_1 import (
    PatchGroupResponse200DataSettingsDynamicGroupStatusType3Type1,
)
from ..models.patch_group_response_200_data_settings_visibility import (
    PatchGroupResponse200DataSettingsVisibility,
)

if TYPE_CHECKING:
    from ..models.patch_group_response_200_data_settings_dynamic_group_rule_set_type_0_item import (
        PatchGroupResponse200DataSettingsDynamicGroupRuleSetType0Item,
    )
    from ..models.patch_group_response_200_data_settings_group_meeting import (
        PatchGroupResponse200DataSettingsGroupMeeting,
    )
    from ..models.patch_group_response_200_data_settings_new_member import (
        PatchGroupResponse200DataSettingsNewMember,
    )


T = TypeVar("T", bound="PatchGroupResponse200DataSettings")


@_attrs_define
class PatchGroupResponse200DataSettings:
    """
    Attributes:
        allow_child_registration (bool): Own children are listed as option during group sign up.
        allow_other_registration (bool): It is allowed to sign up other people uring group sign up.
        allow_same_email_registration (bool): People with same eMail address are listed as option during group sign up.
        allow_spouse_registration (bool): Spouse is listed as option during group sign up.
        allow_waitinglist (bool): Waiting list is in-/active for this group.
        appointment_id (int | None): If set (together with appointmentStartDate), the group is a signup group for the
            specified appointment
        appointment_start_date (datetime.datetime | None): If set (together with appointmentId), the group is a signup
            group for the specified appointment Example: 2022-10-19T12:00:00Z.
        auto_accept (bool): Indicator if applications are accepted automatically.
        automatic_move_up (bool): In combination with waiting list: People automatically move up in waiting list.
        default_post_comments_active (bool): Default value for whether posts can be commented on.
        default_post_notification_scope (None | PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType1 |
            PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType2Type1 |
            PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType3Type1): Default value for post notification
            scope.
        default_post_placeholder_text (None | str): Default placeholder text for entering post content.
        default_post_visibility (PatchGroupResponse200DataSettingsDefaultPostVisibility):
        dynamic_group_rule_set (list[PatchGroupResponse200DataSettingsDynamicGroupRuleSetType0Item] | None): Rule set
            for dynamic group update.
        dynamic_group_status (None | PatchGroupResponse200DataSettingsDynamicGroupStatusType1 |
            PatchGroupResponse200DataSettingsDynamicGroupStatusType2Type1 |
            PatchGroupResponse200DataSettingsDynamicGroupStatusType3Type1): Status of dynamic group update.
        dynamic_group_update_finished (datetime.datetime | None): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        dynamic_group_update_started (datetime.datetime | None): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        external_post_subscriptions_enabled (bool): Indicator if posts of this groups are featured to subscribe
        group_meeting (PatchGroupResponse200DataSettingsGroupMeeting):
        in_statistic (bool):
        inform_leader (bool): Inform leader via e-mail about changes.
        is_hidden (bool):
        is_open_for_members (bool): Indicator if people can sign up for group membership.
        is_public (bool):
        max_members (int | None): The maximum number of group members in counted roles.
        new_member (PatchGroupResponse200DataSettingsNewMember): Campus, status, and department for newly created
            persons.
        posts_enabled (bool):
        qr_code_checkin (bool): QR Codes are sent to participants, which can be used during check-in
        qr_code_checkin_automatic_email (bool): QR Codes are not automatically sent via email
        show_street (bool):
        sign_up_closing_date (datetime.datetime | None): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z'
            Example: 2022-10-19T12:00:00Z.
        sign_up_headline (None | str): Headline for group sign up.
        sign_up_notification_sent_date (datetime.datetime | None): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        sign_up_opening_date (datetime.datetime | None): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z'
            Example: 2022-10-19T12:00:00Z.
        visibility (PatchGroupResponse200DataSettingsVisibility): The visibility of a group.
        waitinglist_max_persons (int | None): Maximum number of persons on waiting list.
    """

    allow_child_registration: bool
    allow_other_registration: bool
    allow_same_email_registration: bool
    allow_spouse_registration: bool
    allow_waitinglist: bool
    appointment_id: int | None
    appointment_start_date: datetime.datetime | None
    auto_accept: bool
    automatic_move_up: bool
    default_post_comments_active: bool
    default_post_notification_scope: (
        None
        | PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType1
        | PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType2Type1
        | PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType3Type1
    )
    default_post_placeholder_text: None | str
    default_post_visibility: PatchGroupResponse200DataSettingsDefaultPostVisibility
    dynamic_group_rule_set: (
        list[PatchGroupResponse200DataSettingsDynamicGroupRuleSetType0Item] | None
    )
    dynamic_group_status: (
        None
        | PatchGroupResponse200DataSettingsDynamicGroupStatusType1
        | PatchGroupResponse200DataSettingsDynamicGroupStatusType2Type1
        | PatchGroupResponse200DataSettingsDynamicGroupStatusType3Type1
    )
    dynamic_group_update_finished: datetime.datetime | None
    dynamic_group_update_started: datetime.datetime | None
    external_post_subscriptions_enabled: bool
    group_meeting: PatchGroupResponse200DataSettingsGroupMeeting
    in_statistic: bool
    inform_leader: bool
    is_hidden: bool
    is_open_for_members: bool
    is_public: bool
    max_members: int | None
    new_member: PatchGroupResponse200DataSettingsNewMember
    posts_enabled: bool
    qr_code_checkin: bool
    qr_code_checkin_automatic_email: bool
    show_street: bool
    sign_up_closing_date: datetime.datetime | None
    sign_up_headline: None | str
    sign_up_notification_sent_date: datetime.datetime | None
    sign_up_opening_date: datetime.datetime | None
    visibility: PatchGroupResponse200DataSettingsVisibility
    waitinglist_max_persons: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_child_registration = self.allow_child_registration

        allow_other_registration = self.allow_other_registration

        allow_same_email_registration = self.allow_same_email_registration

        allow_spouse_registration = self.allow_spouse_registration

        allow_waitinglist = self.allow_waitinglist

        appointment_id: int | None
        appointment_id = self.appointment_id

        appointment_start_date: None | str
        if isinstance(self.appointment_start_date, datetime.datetime):
            appointment_start_date = self.appointment_start_date.isoformat()
        else:
            appointment_start_date = self.appointment_start_date

        auto_accept = self.auto_accept

        automatic_move_up = self.automatic_move_up

        default_post_comments_active = self.default_post_comments_active

        default_post_notification_scope: None | str
        if isinstance(
            self.default_post_notification_scope,
            PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType1,
        ):
            default_post_notification_scope = self.default_post_notification_scope.value
        elif isinstance(
            self.default_post_notification_scope,
            PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType2Type1,
        ):
            default_post_notification_scope = self.default_post_notification_scope.value
        elif isinstance(
            self.default_post_notification_scope,
            PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType3Type1,
        ):
            default_post_notification_scope = self.default_post_notification_scope.value
        else:
            default_post_notification_scope = self.default_post_notification_scope

        default_post_placeholder_text: None | str
        default_post_placeholder_text = self.default_post_placeholder_text

        default_post_visibility = self.default_post_visibility.value

        dynamic_group_rule_set: list[dict[str, Any]] | None
        if isinstance(self.dynamic_group_rule_set, list):
            dynamic_group_rule_set = []
            for dynamic_group_rule_set_type_0_item_data in self.dynamic_group_rule_set:
                dynamic_group_rule_set_type_0_item = (
                    dynamic_group_rule_set_type_0_item_data.to_dict()
                )
                dynamic_group_rule_set.append(dynamic_group_rule_set_type_0_item)

        else:
            dynamic_group_rule_set = self.dynamic_group_rule_set

        dynamic_group_status: None | str
        if isinstance(
            self.dynamic_group_status,
            PatchGroupResponse200DataSettingsDynamicGroupStatusType1,
        ):
            dynamic_group_status = self.dynamic_group_status.value
        elif isinstance(
            self.dynamic_group_status,
            PatchGroupResponse200DataSettingsDynamicGroupStatusType2Type1,
        ):
            dynamic_group_status = self.dynamic_group_status.value
        elif isinstance(
            self.dynamic_group_status,
            PatchGroupResponse200DataSettingsDynamicGroupStatusType3Type1,
        ):
            dynamic_group_status = self.dynamic_group_status.value
        else:
            dynamic_group_status = self.dynamic_group_status

        dynamic_group_update_finished: None | str
        if isinstance(self.dynamic_group_update_finished, datetime.datetime):
            dynamic_group_update_finished = (
                self.dynamic_group_update_finished.isoformat()
            )
        else:
            dynamic_group_update_finished = self.dynamic_group_update_finished

        dynamic_group_update_started: None | str
        if isinstance(self.dynamic_group_update_started, datetime.datetime):
            dynamic_group_update_started = self.dynamic_group_update_started.isoformat()
        else:
            dynamic_group_update_started = self.dynamic_group_update_started

        external_post_subscriptions_enabled = self.external_post_subscriptions_enabled

        group_meeting = self.group_meeting.to_dict()

        in_statistic = self.in_statistic

        inform_leader = self.inform_leader

        is_hidden = self.is_hidden

        is_open_for_members = self.is_open_for_members

        is_public = self.is_public

        max_members: int | None
        max_members = self.max_members

        new_member = self.new_member.to_dict()

        posts_enabled = self.posts_enabled

        qr_code_checkin = self.qr_code_checkin

        qr_code_checkin_automatic_email = self.qr_code_checkin_automatic_email

        show_street = self.show_street

        sign_up_closing_date: None | str
        if isinstance(self.sign_up_closing_date, datetime.datetime):
            sign_up_closing_date = self.sign_up_closing_date.isoformat()
        else:
            sign_up_closing_date = self.sign_up_closing_date

        sign_up_headline: None | str
        sign_up_headline = self.sign_up_headline

        sign_up_notification_sent_date: None | str
        if isinstance(self.sign_up_notification_sent_date, datetime.datetime):
            sign_up_notification_sent_date = (
                self.sign_up_notification_sent_date.isoformat()
            )
        else:
            sign_up_notification_sent_date = self.sign_up_notification_sent_date

        sign_up_opening_date: None | str
        if isinstance(self.sign_up_opening_date, datetime.datetime):
            sign_up_opening_date = self.sign_up_opening_date.isoformat()
        else:
            sign_up_opening_date = self.sign_up_opening_date

        visibility = self.visibility.value

        waitinglist_max_persons: int | None
        waitinglist_max_persons = self.waitinglist_max_persons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowChildRegistration": allow_child_registration,
                "allowOtherRegistration": allow_other_registration,
                "allowSameEmailRegistration": allow_same_email_registration,
                "allowSpouseRegistration": allow_spouse_registration,
                "allowWaitinglist": allow_waitinglist,
                "appointmentId": appointment_id,
                "appointmentStartDate": appointment_start_date,
                "autoAccept": auto_accept,
                "automaticMoveUp": automatic_move_up,
                "defaultPostCommentsActive": default_post_comments_active,
                "defaultPostNotificationScope": default_post_notification_scope,
                "defaultPostPlaceholderText": default_post_placeholder_text,
                "defaultPostVisibility": default_post_visibility,
                "dynamicGroupRuleSet": dynamic_group_rule_set,
                "dynamicGroupStatus": dynamic_group_status,
                "dynamicGroupUpdateFinished": dynamic_group_update_finished,
                "dynamicGroupUpdateStarted": dynamic_group_update_started,
                "externalPostSubscriptionsEnabled": external_post_subscriptions_enabled,
                "groupMeeting": group_meeting,
                "inStatistic": in_statistic,
                "informLeader": inform_leader,
                "isHidden": is_hidden,
                "isOpenForMembers": is_open_for_members,
                "isPublic": is_public,
                "maxMembers": max_members,
                "newMember": new_member,
                "postsEnabled": posts_enabled,
                "qrCodeCheckin": qr_code_checkin,
                "qrCodeCheckinAutomaticEmail": qr_code_checkin_automatic_email,
                "showStreet": show_street,
                "signUpClosingDate": sign_up_closing_date,
                "signUpHeadline": sign_up_headline,
                "signUpNotificationSentDate": sign_up_notification_sent_date,
                "signUpOpeningDate": sign_up_opening_date,
                "visibility": visibility,
                "waitinglistMaxPersons": waitinglist_max_persons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_group_response_200_data_settings_dynamic_group_rule_set_type_0_item import (
            PatchGroupResponse200DataSettingsDynamicGroupRuleSetType0Item,
        )
        from ..models.patch_group_response_200_data_settings_group_meeting import (
            PatchGroupResponse200DataSettingsGroupMeeting,
        )
        from ..models.patch_group_response_200_data_settings_new_member import (
            PatchGroupResponse200DataSettingsNewMember,
        )

        d = dict(src_dict)
        allow_child_registration = d.pop("allowChildRegistration")

        allow_other_registration = d.pop("allowOtherRegistration")

        allow_same_email_registration = d.pop("allowSameEmailRegistration")

        allow_spouse_registration = d.pop("allowSpouseRegistration")

        allow_waitinglist = d.pop("allowWaitinglist")

        def _parse_appointment_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        appointment_id = _parse_appointment_id(d.pop("appointmentId"))

        def _parse_appointment_start_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                appointment_start_date_type_0 = isoparse(data)

                return appointment_start_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None, data)

        appointment_start_date = _parse_appointment_start_date(
            d.pop("appointmentStartDate")
        )

        auto_accept = d.pop("autoAccept")

        automatic_move_up = d.pop("automaticMoveUp")

        default_post_comments_active = d.pop("defaultPostCommentsActive")

        def _parse_default_post_notification_scope(
            data: object,
        ) -> (
            None
            | PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType1
            | PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType2Type1
            | PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_post_notification_scope_type_1 = (
                    PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType1(
                        data
                    )
                )

                return default_post_notification_scope_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_post_notification_scope_type_2_type_1 = PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType2Type1(
                    data
                )

                return default_post_notification_scope_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_post_notification_scope_type_3_type_1 = PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType3Type1(
                    data
                )

                return default_post_notification_scope_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                None
                | PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType1
                | PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType2Type1
                | PatchGroupResponse200DataSettingsDefaultPostNotificationScopeType3Type1,
                data,
            )

        default_post_notification_scope = _parse_default_post_notification_scope(
            d.pop("defaultPostNotificationScope")
        )

        def _parse_default_post_placeholder_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        default_post_placeholder_text = _parse_default_post_placeholder_text(
            d.pop("defaultPostPlaceholderText")
        )

        default_post_visibility = (
            PatchGroupResponse200DataSettingsDefaultPostVisibility(
                d.pop("defaultPostVisibility")
            )
        )

        def _parse_dynamic_group_rule_set(
            data: object,
        ) -> list[PatchGroupResponse200DataSettingsDynamicGroupRuleSetType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dynamic_group_rule_set_type_0 = []
                _dynamic_group_rule_set_type_0 = data
                for (
                    dynamic_group_rule_set_type_0_item_data
                ) in _dynamic_group_rule_set_type_0:
                    dynamic_group_rule_set_type_0_item = PatchGroupResponse200DataSettingsDynamicGroupRuleSetType0Item.from_dict(
                        dynamic_group_rule_set_type_0_item_data
                    )

                    dynamic_group_rule_set_type_0.append(
                        dynamic_group_rule_set_type_0_item
                    )

                return dynamic_group_rule_set_type_0
            except:  # noqa: E722
                pass
            return cast(
                list[PatchGroupResponse200DataSettingsDynamicGroupRuleSetType0Item]
                | None,
                data,
            )

        dynamic_group_rule_set = _parse_dynamic_group_rule_set(
            d.pop("dynamicGroupRuleSet")
        )

        def _parse_dynamic_group_status(
            data: object,
        ) -> (
            None
            | PatchGroupResponse200DataSettingsDynamicGroupStatusType1
            | PatchGroupResponse200DataSettingsDynamicGroupStatusType2Type1
            | PatchGroupResponse200DataSettingsDynamicGroupStatusType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dynamic_group_status_type_1 = (
                    PatchGroupResponse200DataSettingsDynamicGroupStatusType1(data)
                )

                return dynamic_group_status_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dynamic_group_status_type_2_type_1 = (
                    PatchGroupResponse200DataSettingsDynamicGroupStatusType2Type1(data)
                )

                return dynamic_group_status_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dynamic_group_status_type_3_type_1 = (
                    PatchGroupResponse200DataSettingsDynamicGroupStatusType3Type1(data)
                )

                return dynamic_group_status_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                None
                | PatchGroupResponse200DataSettingsDynamicGroupStatusType1
                | PatchGroupResponse200DataSettingsDynamicGroupStatusType2Type1
                | PatchGroupResponse200DataSettingsDynamicGroupStatusType3Type1,
                data,
            )

        dynamic_group_status = _parse_dynamic_group_status(d.pop("dynamicGroupStatus"))

        def _parse_dynamic_group_update_finished(
            data: object,
        ) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dynamic_group_update_finished_type_0 = isoparse(data)

                return dynamic_group_update_finished_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None, data)

        dynamic_group_update_finished = _parse_dynamic_group_update_finished(
            d.pop("dynamicGroupUpdateFinished")
        )

        def _parse_dynamic_group_update_started(
            data: object,
        ) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dynamic_group_update_started_type_0 = isoparse(data)

                return dynamic_group_update_started_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None, data)

        dynamic_group_update_started = _parse_dynamic_group_update_started(
            d.pop("dynamicGroupUpdateStarted")
        )

        external_post_subscriptions_enabled = d.pop("externalPostSubscriptionsEnabled")

        group_meeting = PatchGroupResponse200DataSettingsGroupMeeting.from_dict(
            d.pop("groupMeeting")
        )

        in_statistic = d.pop("inStatistic")

        inform_leader = d.pop("informLeader")

        is_hidden = d.pop("isHidden")

        is_open_for_members = d.pop("isOpenForMembers")

        is_public = d.pop("isPublic")

        def _parse_max_members(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_members = _parse_max_members(d.pop("maxMembers"))

        new_member = PatchGroupResponse200DataSettingsNewMember.from_dict(
            d.pop("newMember")
        )

        posts_enabled = d.pop("postsEnabled")

        qr_code_checkin = d.pop("qrCodeCheckin")

        qr_code_checkin_automatic_email = d.pop("qrCodeCheckinAutomaticEmail")

        show_street = d.pop("showStreet")

        def _parse_sign_up_closing_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sign_up_closing_date_type_0 = isoparse(data)

                return sign_up_closing_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None, data)

        sign_up_closing_date = _parse_sign_up_closing_date(d.pop("signUpClosingDate"))

        def _parse_sign_up_headline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sign_up_headline = _parse_sign_up_headline(d.pop("signUpHeadline"))

        def _parse_sign_up_notification_sent_date(
            data: object,
        ) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sign_up_notification_sent_date_type_0 = isoparse(data)

                return sign_up_notification_sent_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None, data)

        sign_up_notification_sent_date = _parse_sign_up_notification_sent_date(
            d.pop("signUpNotificationSentDate")
        )

        def _parse_sign_up_opening_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sign_up_opening_date_type_0 = isoparse(data)

                return sign_up_opening_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None, data)

        sign_up_opening_date = _parse_sign_up_opening_date(d.pop("signUpOpeningDate"))

        visibility = PatchGroupResponse200DataSettingsVisibility(d.pop("visibility"))

        def _parse_waitinglist_max_persons(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        waitinglist_max_persons = _parse_waitinglist_max_persons(
            d.pop("waitinglistMaxPersons")
        )

        patch_group_response_200_data_settings = cls(
            allow_child_registration=allow_child_registration,
            allow_other_registration=allow_other_registration,
            allow_same_email_registration=allow_same_email_registration,
            allow_spouse_registration=allow_spouse_registration,
            allow_waitinglist=allow_waitinglist,
            appointment_id=appointment_id,
            appointment_start_date=appointment_start_date,
            auto_accept=auto_accept,
            automatic_move_up=automatic_move_up,
            default_post_comments_active=default_post_comments_active,
            default_post_notification_scope=default_post_notification_scope,
            default_post_placeholder_text=default_post_placeholder_text,
            default_post_visibility=default_post_visibility,
            dynamic_group_rule_set=dynamic_group_rule_set,
            dynamic_group_status=dynamic_group_status,
            dynamic_group_update_finished=dynamic_group_update_finished,
            dynamic_group_update_started=dynamic_group_update_started,
            external_post_subscriptions_enabled=external_post_subscriptions_enabled,
            group_meeting=group_meeting,
            in_statistic=in_statistic,
            inform_leader=inform_leader,
            is_hidden=is_hidden,
            is_open_for_members=is_open_for_members,
            is_public=is_public,
            max_members=max_members,
            new_member=new_member,
            posts_enabled=posts_enabled,
            qr_code_checkin=qr_code_checkin,
            qr_code_checkin_automatic_email=qr_code_checkin_automatic_email,
            show_street=show_street,
            sign_up_closing_date=sign_up_closing_date,
            sign_up_headline=sign_up_headline,
            sign_up_notification_sent_date=sign_up_notification_sent_date,
            sign_up_opening_date=sign_up_opening_date,
            visibility=visibility,
            waitinglist_max_persons=waitinglist_max_persons,
        )

        patch_group_response_200_data_settings.additional_properties = d
        return patch_group_response_200_data_settings

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
