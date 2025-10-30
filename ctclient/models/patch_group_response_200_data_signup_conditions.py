from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_group_response_200_data_signup_conditions_group_visibility import (
    PatchGroupResponse200DataSignupConditionsGroupVisibility,
)

T = TypeVar("T", bound="PatchGroupResponse200DataSignupConditions")


@_attrs_define
class PatchGroupResponse200DataSignupConditions:
    """
    Attributes:
        can_contact_leader (bool):
        can_sign_up (bool):
        can_sign_up_as_new_person (bool):
        default_role_set_in_group (bool):
        end_date_not_passed (bool):
        group_allows_waitinglist (bool):
        group_has_leader (bool):
        group_has_space_for_requests (bool):
        group_has_space_on_waitinglist (bool):
        group_is_active (bool):
        group_is_not_full (bool):
        group_is_not_hidden (bool):
        group_is_open_for_members (bool):
        group_is_public (bool):
        group_visibility (PatchGroupResponse200DataSignupConditionsGroupVisibility): The visibility of a group.
        new_person_department_is_set (bool):
        new_person_station_is_set (bool):
        new_person_status_is_set (bool):
        sign_up_role_set_in_group (bool):
    """

    can_contact_leader: bool
    can_sign_up: bool
    can_sign_up_as_new_person: bool
    default_role_set_in_group: bool
    end_date_not_passed: bool
    group_allows_waitinglist: bool
    group_has_leader: bool
    group_has_space_for_requests: bool
    group_has_space_on_waitinglist: bool
    group_is_active: bool
    group_is_not_full: bool
    group_is_not_hidden: bool
    group_is_open_for_members: bool
    group_is_public: bool
    group_visibility: PatchGroupResponse200DataSignupConditionsGroupVisibility
    new_person_department_is_set: bool
    new_person_station_is_set: bool
    new_person_status_is_set: bool
    sign_up_role_set_in_group: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_contact_leader = self.can_contact_leader

        can_sign_up = self.can_sign_up

        can_sign_up_as_new_person = self.can_sign_up_as_new_person

        default_role_set_in_group = self.default_role_set_in_group

        end_date_not_passed = self.end_date_not_passed

        group_allows_waitinglist = self.group_allows_waitinglist

        group_has_leader = self.group_has_leader

        group_has_space_for_requests = self.group_has_space_for_requests

        group_has_space_on_waitinglist = self.group_has_space_on_waitinglist

        group_is_active = self.group_is_active

        group_is_not_full = self.group_is_not_full

        group_is_not_hidden = self.group_is_not_hidden

        group_is_open_for_members = self.group_is_open_for_members

        group_is_public = self.group_is_public

        group_visibility = self.group_visibility.value

        new_person_department_is_set = self.new_person_department_is_set

        new_person_station_is_set = self.new_person_station_is_set

        new_person_status_is_set = self.new_person_status_is_set

        sign_up_role_set_in_group = self.sign_up_role_set_in_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canContactLeader": can_contact_leader,
                "canSignUp": can_sign_up,
                "canSignUpAsNewPerson": can_sign_up_as_new_person,
                "defaultRoleSetInGroup": default_role_set_in_group,
                "endDateNotPassed": end_date_not_passed,
                "groupAllowsWaitinglist": group_allows_waitinglist,
                "groupHasLeader": group_has_leader,
                "groupHasSpaceForRequests": group_has_space_for_requests,
                "groupHasSpaceOnWaitinglist": group_has_space_on_waitinglist,
                "groupIsActive": group_is_active,
                "groupIsNotFull": group_is_not_full,
                "groupIsNotHidden": group_is_not_hidden,
                "groupIsOpenForMembers": group_is_open_for_members,
                "groupIsPublic": group_is_public,
                "groupVisibility": group_visibility,
                "newPersonDepartmentIsSet": new_person_department_is_set,
                "newPersonStationIsSet": new_person_station_is_set,
                "newPersonStatusIsSet": new_person_status_is_set,
                "signUpRoleSetInGroup": sign_up_role_set_in_group,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_contact_leader = d.pop("canContactLeader")

        can_sign_up = d.pop("canSignUp")

        can_sign_up_as_new_person = d.pop("canSignUpAsNewPerson")

        default_role_set_in_group = d.pop("defaultRoleSetInGroup")

        end_date_not_passed = d.pop("endDateNotPassed")

        group_allows_waitinglist = d.pop("groupAllowsWaitinglist")

        group_has_leader = d.pop("groupHasLeader")

        group_has_space_for_requests = d.pop("groupHasSpaceForRequests")

        group_has_space_on_waitinglist = d.pop("groupHasSpaceOnWaitinglist")

        group_is_active = d.pop("groupIsActive")

        group_is_not_full = d.pop("groupIsNotFull")

        group_is_not_hidden = d.pop("groupIsNotHidden")

        group_is_open_for_members = d.pop("groupIsOpenForMembers")

        group_is_public = d.pop("groupIsPublic")

        group_visibility = PatchGroupResponse200DataSignupConditionsGroupVisibility(
            d.pop("groupVisibility")
        )

        new_person_department_is_set = d.pop("newPersonDepartmentIsSet")

        new_person_station_is_set = d.pop("newPersonStationIsSet")

        new_person_status_is_set = d.pop("newPersonStatusIsSet")

        sign_up_role_set_in_group = d.pop("signUpRoleSetInGroup")

        patch_group_response_200_data_signup_conditions = cls(
            can_contact_leader=can_contact_leader,
            can_sign_up=can_sign_up,
            can_sign_up_as_new_person=can_sign_up_as_new_person,
            default_role_set_in_group=default_role_set_in_group,
            end_date_not_passed=end_date_not_passed,
            group_allows_waitinglist=group_allows_waitinglist,
            group_has_leader=group_has_leader,
            group_has_space_for_requests=group_has_space_for_requests,
            group_has_space_on_waitinglist=group_has_space_on_waitinglist,
            group_is_active=group_is_active,
            group_is_not_full=group_is_not_full,
            group_is_not_hidden=group_is_not_hidden,
            group_is_open_for_members=group_is_open_for_members,
            group_is_public=group_is_public,
            group_visibility=group_visibility,
            new_person_department_is_set=new_person_department_is_set,
            new_person_station_is_set=new_person_station_is_set,
            new_person_status_is_set=new_person_status_is_set,
            sign_up_role_set_in_group=sign_up_role_set_in_group,
        )

        patch_group_response_200_data_signup_conditions.additional_properties = d
        return patch_group_response_200_data_signup_conditions

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
