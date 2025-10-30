from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.service_exchange_request_requested_person_invitation_status_type_0 import (
    ServiceExchangeRequestRequestedPersonInvitationStatusType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_exchange_request_requested_person_emails_item import (
        ServiceExchangeRequestRequestedPersonEmailsItem,
    )
    from ..models.service_exchange_request_requested_person_meta import (
        ServiceExchangeRequestRequestedPersonMeta,
    )
    from ..models.service_exchange_request_requested_person_privacy_policy_agreement import (
        ServiceExchangeRequestRequestedPersonPrivacyPolicyAgreement,
    )
    from ..models.service_exchange_request_requested_person_tags_item import (
        ServiceExchangeRequestRequestedPersonTagsItem,
    )


T = TypeVar("T", bound="ServiceExchangeRequestRequestedPerson")


@_attrs_define
class ServiceExchangeRequestRequestedPerson:
    """A person object includes all fields the logged in user may see depending on the security level. Additional DB
    fields, created by the admin, are also part of the response. Those fields have the same name as the column name.

        Attributes:
            edit_security_level_for_person (int): Edit security level of the current person. The user can edit fields upto
                this level.
            guid (str):
            id (int):
            security_level_for_person (int): Security level of the current person. The user sees fields upto this level.
            acceptedsecurity (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
                2022-10-19.
            address_addition (str | Unset):
            age (int | Unset): This computed field contains the age of this person if the date of birth is visible. If this
                person already dead, the age is calculated until the date of death.
            baptised_by (str | Unset):
            birth_name (str | Unset):
            birthday (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
            birthplace (str | Unset):
            campus_id (int | Unset):
            can_chat (bool | Unset):
            chat_active (bool | Unset):
            city (str | Unset):
            cms_user_id (str | Unset):
            country (str | Unset):
            date_of_baptism (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
                2022-10-19.
            date_of_belonging (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
                2022-10-19.
            date_of_death (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example:
                2022-10-19.
            date_of_entry (None | str | Unset): A simple timestamp in ISO format, e.g. '2022-10-19 12:00:00' Example:
                2022-10-19 12:00:00.
            date_of_resign (None | str | Unset): A simple timestamp in ISO format, e.g. '2022-10-19 12:00:00' Example:
                2022-10-19 12:00:00.
            department_ids (list[int] | Unset): List of department IDs
            email (str | Unset): Primary email address of the person.
            emails (list[ServiceExchangeRequestRequestedPersonEmailsItem] | Unset):
            family_image_url (None | str | Unset):
            family_status_id (int | None | Unset):
            fax (str | Unset):
            first_contact (None | str | Unset): A simple timestamp in ISO format, e.g. '2022-10-19 12:00:00' Example:
                2022-10-19 12:00:00.
            first_name (str | Unset):
            grow_path_id (int | Unset):
            image_url (None | str | Unset):
            invitation_status (None | ServiceExchangeRequestRequestedPersonInvitationStatusType0 | Unset):
            is_archived (bool | Unset):
            is_dead (bool | Unset): This computed field is true iff a date of death is set for this person.
            job (str | Unset):
            last_edited_date (datetime.datetime | None | Unset): A timestamp in Zulu time format, e.g.
                '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
            last_login (datetime.datetime | None | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z'
                Example: 2022-10-19T12:00:00Z.
            last_name (str | Unset):
            latitude (float | None | Unset):
            latitude_loose (float | None | Unset):
            longitude (float | None | Unset):
            longitude_loose (float | None | Unset):
            meta (ServiceExchangeRequestRequestedPersonMeta | Unset):  Example: {'createdDate': '2020-01-01T00:00:00Z',
                'createdPerson': {'id': 1}, 'modifiedDate': '2020-01-01T00:00:00Z', 'modifiedPerson': {'id': 1}}.
            mobile (str | Unset):
            nationality_id (int | None | Unset):
            nickname (str | Unset):
            optigem_id (str | Unset): String with Optigem ID or empty string if no ID is set.
            phone_private (str | Unset):
            phone_work (str | Unset):
            place_of_baptism (str | Unset):
            privacy_policy_agreement (ServiceExchangeRequestRequestedPersonPrivacyPolicyAgreement | Unset):
            privacy_policy_agreement_date (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19'
                Example: 2022-10-19.
            privacy_policy_agreement_type_id (int | None | Unset):
            privacy_policy_agreement_who_id (int | None | Unset):
            referred_by (str | Unset):
            referred_to (str | Unset):
            sex_id (int | None | Unset):
            status_id (int | Unset):
            street (str | Unset):
            tags (list[ServiceExchangeRequestRequestedPersonTagsItem] | Unset):
            title (str | Unset):
            wedding_date (datetime.date | None | Unset): A simple date in ISO format, e.g. '2022-10-19' Example: 2022-10-19.
            zip_ (str | Unset):
    """

    edit_security_level_for_person: int
    guid: str
    id: int
    security_level_for_person: int
    acceptedsecurity: datetime.date | None | Unset = UNSET
    address_addition: str | Unset = UNSET
    age: int | Unset = UNSET
    baptised_by: str | Unset = UNSET
    birth_name: str | Unset = UNSET
    birthday: datetime.date | None | Unset = UNSET
    birthplace: str | Unset = UNSET
    campus_id: int | Unset = UNSET
    can_chat: bool | Unset = UNSET
    chat_active: bool | Unset = UNSET
    city: str | Unset = UNSET
    cms_user_id: str | Unset = UNSET
    country: str | Unset = UNSET
    date_of_baptism: datetime.date | None | Unset = UNSET
    date_of_belonging: datetime.date | None | Unset = UNSET
    date_of_death: datetime.date | None | Unset = UNSET
    date_of_entry: None | str | Unset = UNSET
    date_of_resign: None | str | Unset = UNSET
    department_ids: list[int] | Unset = UNSET
    email: str | Unset = UNSET
    emails: list[ServiceExchangeRequestRequestedPersonEmailsItem] | Unset = UNSET
    family_image_url: None | str | Unset = UNSET
    family_status_id: int | None | Unset = UNSET
    fax: str | Unset = UNSET
    first_contact: None | str | Unset = UNSET
    first_name: str | Unset = UNSET
    grow_path_id: int | Unset = UNSET
    image_url: None | str | Unset = UNSET
    invitation_status: (
        None | ServiceExchangeRequestRequestedPersonInvitationStatusType0 | Unset
    ) = UNSET
    is_archived: bool | Unset = UNSET
    is_dead: bool | Unset = UNSET
    job: str | Unset = UNSET
    last_edited_date: datetime.datetime | None | Unset = UNSET
    last_login: datetime.datetime | None | Unset = UNSET
    last_name: str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    latitude_loose: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    longitude_loose: float | None | Unset = UNSET
    meta: ServiceExchangeRequestRequestedPersonMeta | Unset = UNSET
    mobile: str | Unset = UNSET
    nationality_id: int | None | Unset = UNSET
    nickname: str | Unset = UNSET
    optigem_id: str | Unset = UNSET
    phone_private: str | Unset = UNSET
    phone_work: str | Unset = UNSET
    place_of_baptism: str | Unset = UNSET
    privacy_policy_agreement: (
        ServiceExchangeRequestRequestedPersonPrivacyPolicyAgreement | Unset
    ) = UNSET
    privacy_policy_agreement_date: datetime.date | None | Unset = UNSET
    privacy_policy_agreement_type_id: int | None | Unset = UNSET
    privacy_policy_agreement_who_id: int | None | Unset = UNSET
    referred_by: str | Unset = UNSET
    referred_to: str | Unset = UNSET
    sex_id: int | None | Unset = UNSET
    status_id: int | Unset = UNSET
    street: str | Unset = UNSET
    tags: list[ServiceExchangeRequestRequestedPersonTagsItem] | Unset = UNSET
    title: str | Unset = UNSET
    wedding_date: datetime.date | None | Unset = UNSET
    zip_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edit_security_level_for_person = self.edit_security_level_for_person

        guid = self.guid

        id = self.id

        security_level_for_person = self.security_level_for_person

        acceptedsecurity: None | str | Unset
        if isinstance(self.acceptedsecurity, Unset):
            acceptedsecurity = UNSET
        elif isinstance(self.acceptedsecurity, datetime.date):
            acceptedsecurity = self.acceptedsecurity.isoformat()
        else:
            acceptedsecurity = self.acceptedsecurity

        address_addition = self.address_addition

        age = self.age

        baptised_by = self.baptised_by

        birth_name = self.birth_name

        birthday: None | str | Unset
        if isinstance(self.birthday, Unset):
            birthday = UNSET
        elif isinstance(self.birthday, datetime.date):
            birthday = self.birthday.isoformat()
        else:
            birthday = self.birthday

        birthplace = self.birthplace

        campus_id = self.campus_id

        can_chat = self.can_chat

        chat_active = self.chat_active

        city = self.city

        cms_user_id = self.cms_user_id

        country = self.country

        date_of_baptism: None | str | Unset
        if isinstance(self.date_of_baptism, Unset):
            date_of_baptism = UNSET
        elif isinstance(self.date_of_baptism, datetime.date):
            date_of_baptism = self.date_of_baptism.isoformat()
        else:
            date_of_baptism = self.date_of_baptism

        date_of_belonging: None | str | Unset
        if isinstance(self.date_of_belonging, Unset):
            date_of_belonging = UNSET
        elif isinstance(self.date_of_belonging, datetime.date):
            date_of_belonging = self.date_of_belonging.isoformat()
        else:
            date_of_belonging = self.date_of_belonging

        date_of_death: None | str | Unset
        if isinstance(self.date_of_death, Unset):
            date_of_death = UNSET
        elif isinstance(self.date_of_death, datetime.date):
            date_of_death = self.date_of_death.isoformat()
        else:
            date_of_death = self.date_of_death

        date_of_entry: None | str | Unset
        if isinstance(self.date_of_entry, Unset):
            date_of_entry = UNSET
        else:
            date_of_entry = self.date_of_entry

        date_of_resign: None | str | Unset
        if isinstance(self.date_of_resign, Unset):
            date_of_resign = UNSET
        else:
            date_of_resign = self.date_of_resign

        department_ids: list[int] | Unset = UNSET
        if not isinstance(self.department_ids, Unset):
            department_ids = self.department_ids

        email = self.email

        emails: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()
                emails.append(emails_item)

        family_image_url: None | str | Unset
        if isinstance(self.family_image_url, Unset):
            family_image_url = UNSET
        else:
            family_image_url = self.family_image_url

        family_status_id: int | None | Unset
        if isinstance(self.family_status_id, Unset):
            family_status_id = UNSET
        else:
            family_status_id = self.family_status_id

        fax = self.fax

        first_contact: None | str | Unset
        if isinstance(self.first_contact, Unset):
            first_contact = UNSET
        else:
            first_contact = self.first_contact

        first_name = self.first_name

        grow_path_id = self.grow_path_id

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        invitation_status: None | str | Unset
        if isinstance(self.invitation_status, Unset):
            invitation_status = UNSET
        elif isinstance(
            self.invitation_status,
            ServiceExchangeRequestRequestedPersonInvitationStatusType0,
        ):
            invitation_status = self.invitation_status.value
        else:
            invitation_status = self.invitation_status

        is_archived = self.is_archived

        is_dead = self.is_dead

        job = self.job

        last_edited_date: None | str | Unset
        if isinstance(self.last_edited_date, Unset):
            last_edited_date = UNSET
        elif isinstance(self.last_edited_date, datetime.datetime):
            last_edited_date = self.last_edited_date.isoformat()
        else:
            last_edited_date = self.last_edited_date

        last_login: None | str | Unset
        if isinstance(self.last_login, Unset):
            last_login = UNSET
        elif isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.isoformat()
        else:
            last_login = self.last_login

        last_name = self.last_name

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        latitude_loose: float | None | Unset
        if isinstance(self.latitude_loose, Unset):
            latitude_loose = UNSET
        else:
            latitude_loose = self.latitude_loose

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        longitude_loose: float | None | Unset
        if isinstance(self.longitude_loose, Unset):
            longitude_loose = UNSET
        else:
            longitude_loose = self.longitude_loose

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        mobile = self.mobile

        nationality_id: int | None | Unset
        if isinstance(self.nationality_id, Unset):
            nationality_id = UNSET
        else:
            nationality_id = self.nationality_id

        nickname = self.nickname

        optigem_id = self.optigem_id

        phone_private = self.phone_private

        phone_work = self.phone_work

        place_of_baptism = self.place_of_baptism

        privacy_policy_agreement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.privacy_policy_agreement, Unset):
            privacy_policy_agreement = self.privacy_policy_agreement.to_dict()

        privacy_policy_agreement_date: None | str | Unset
        if isinstance(self.privacy_policy_agreement_date, Unset):
            privacy_policy_agreement_date = UNSET
        elif isinstance(self.privacy_policy_agreement_date, datetime.date):
            privacy_policy_agreement_date = (
                self.privacy_policy_agreement_date.isoformat()
            )
        else:
            privacy_policy_agreement_date = self.privacy_policy_agreement_date

        privacy_policy_agreement_type_id: int | None | Unset
        if isinstance(self.privacy_policy_agreement_type_id, Unset):
            privacy_policy_agreement_type_id = UNSET
        else:
            privacy_policy_agreement_type_id = self.privacy_policy_agreement_type_id

        privacy_policy_agreement_who_id: int | None | Unset
        if isinstance(self.privacy_policy_agreement_who_id, Unset):
            privacy_policy_agreement_who_id = UNSET
        else:
            privacy_policy_agreement_who_id = self.privacy_policy_agreement_who_id

        referred_by = self.referred_by

        referred_to = self.referred_to

        sex_id: int | None | Unset
        if isinstance(self.sex_id, Unset):
            sex_id = UNSET
        else:
            sex_id = self.sex_id

        status_id = self.status_id

        street = self.street

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        title = self.title

        wedding_date: None | str | Unset
        if isinstance(self.wedding_date, Unset):
            wedding_date = UNSET
        elif isinstance(self.wedding_date, datetime.date):
            wedding_date = self.wedding_date.isoformat()
        else:
            wedding_date = self.wedding_date

        zip_ = self.zip_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "editSecurityLevelForPerson": edit_security_level_for_person,
                "guid": guid,
                "id": id,
                "securityLevelForPerson": security_level_for_person,
            }
        )
        if acceptedsecurity is not UNSET:
            field_dict["acceptedsecurity"] = acceptedsecurity
        if address_addition is not UNSET:
            field_dict["addressAddition"] = address_addition
        if age is not UNSET:
            field_dict["age"] = age
        if baptised_by is not UNSET:
            field_dict["baptisedBy"] = baptised_by
        if birth_name is not UNSET:
            field_dict["birthName"] = birth_name
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if birthplace is not UNSET:
            field_dict["birthplace"] = birthplace
        if campus_id is not UNSET:
            field_dict["campusId"] = campus_id
        if can_chat is not UNSET:
            field_dict["canChat"] = can_chat
        if chat_active is not UNSET:
            field_dict["chatActive"] = chat_active
        if city is not UNSET:
            field_dict["city"] = city
        if cms_user_id is not UNSET:
            field_dict["cmsUserId"] = cms_user_id
        if country is not UNSET:
            field_dict["country"] = country
        if date_of_baptism is not UNSET:
            field_dict["dateOfBaptism"] = date_of_baptism
        if date_of_belonging is not UNSET:
            field_dict["dateOfBelonging"] = date_of_belonging
        if date_of_death is not UNSET:
            field_dict["dateOfDeath"] = date_of_death
        if date_of_entry is not UNSET:
            field_dict["dateOfEntry"] = date_of_entry
        if date_of_resign is not UNSET:
            field_dict["dateOfResign"] = date_of_resign
        if department_ids is not UNSET:
            field_dict["departmentIds"] = department_ids
        if email is not UNSET:
            field_dict["email"] = email
        if emails is not UNSET:
            field_dict["emails"] = emails
        if family_image_url is not UNSET:
            field_dict["familyImageUrl"] = family_image_url
        if family_status_id is not UNSET:
            field_dict["familyStatusId"] = family_status_id
        if fax is not UNSET:
            field_dict["fax"] = fax
        if first_contact is not UNSET:
            field_dict["firstContact"] = first_contact
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if grow_path_id is not UNSET:
            field_dict["growPathId"] = grow_path_id
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if invitation_status is not UNSET:
            field_dict["invitationStatus"] = invitation_status
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_dead is not UNSET:
            field_dict["isDead"] = is_dead
        if job is not UNSET:
            field_dict["job"] = job
        if last_edited_date is not UNSET:
            field_dict["lastEditedDate"] = last_edited_date
        if last_login is not UNSET:
            field_dict["lastLogin"] = last_login
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if latitude_loose is not UNSET:
            field_dict["latitudeLoose"] = latitude_loose
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if longitude_loose is not UNSET:
            field_dict["longitudeLoose"] = longitude_loose
        if meta is not UNSET:
            field_dict["meta"] = meta
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if nationality_id is not UNSET:
            field_dict["nationalityId"] = nationality_id
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if optigem_id is not UNSET:
            field_dict["optigemId"] = optigem_id
        if phone_private is not UNSET:
            field_dict["phonePrivate"] = phone_private
        if phone_work is not UNSET:
            field_dict["phoneWork"] = phone_work
        if place_of_baptism is not UNSET:
            field_dict["placeOfBaptism"] = place_of_baptism
        if privacy_policy_agreement is not UNSET:
            field_dict["privacyPolicyAgreement"] = privacy_policy_agreement
        if privacy_policy_agreement_date is not UNSET:
            field_dict["privacyPolicyAgreementDate"] = privacy_policy_agreement_date
        if privacy_policy_agreement_type_id is not UNSET:
            field_dict["privacyPolicyAgreementTypeId"] = (
                privacy_policy_agreement_type_id
            )
        if privacy_policy_agreement_who_id is not UNSET:
            field_dict["privacyPolicyAgreementWhoId"] = privacy_policy_agreement_who_id
        if referred_by is not UNSET:
            field_dict["referredBy"] = referred_by
        if referred_to is not UNSET:
            field_dict["referredTo"] = referred_to
        if sex_id is not UNSET:
            field_dict["sexId"] = sex_id
        if status_id is not UNSET:
            field_dict["statusId"] = status_id
        if street is not UNSET:
            field_dict["street"] = street
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title
        if wedding_date is not UNSET:
            field_dict["weddingDate"] = wedding_date
        if zip_ is not UNSET:
            field_dict["zip"] = zip_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_exchange_request_requested_person_emails_item import (
            ServiceExchangeRequestRequestedPersonEmailsItem,
        )
        from ..models.service_exchange_request_requested_person_meta import (
            ServiceExchangeRequestRequestedPersonMeta,
        )
        from ..models.service_exchange_request_requested_person_privacy_policy_agreement import (
            ServiceExchangeRequestRequestedPersonPrivacyPolicyAgreement,
        )
        from ..models.service_exchange_request_requested_person_tags_item import (
            ServiceExchangeRequestRequestedPersonTagsItem,
        )

        d = dict(src_dict)
        edit_security_level_for_person = d.pop("editSecurityLevelForPerson")

        guid = d.pop("guid")

        id = d.pop("id")

        security_level_for_person = d.pop("securityLevelForPerson")

        def _parse_acceptedsecurity(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acceptedsecurity_type_0 = isoparse(data).date()

                return acceptedsecurity_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        acceptedsecurity = _parse_acceptedsecurity(d.pop("acceptedsecurity", UNSET))

        address_addition = d.pop("addressAddition", UNSET)

        age = d.pop("age", UNSET)

        baptised_by = d.pop("baptisedBy", UNSET)

        birth_name = d.pop("birthName", UNSET)

        def _parse_birthday(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birthday_type_0 = isoparse(data).date()

                return birthday_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        birthday = _parse_birthday(d.pop("birthday", UNSET))

        birthplace = d.pop("birthplace", UNSET)

        campus_id = d.pop("campusId", UNSET)

        can_chat = d.pop("canChat", UNSET)

        chat_active = d.pop("chatActive", UNSET)

        city = d.pop("city", UNSET)

        cms_user_id = d.pop("cmsUserId", UNSET)

        country = d.pop("country", UNSET)

        def _parse_date_of_baptism(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_baptism_type_0 = isoparse(data).date()

                return date_of_baptism_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_baptism = _parse_date_of_baptism(d.pop("dateOfBaptism", UNSET))

        def _parse_date_of_belonging(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_belonging_type_0 = isoparse(data).date()

                return date_of_belonging_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_belonging = _parse_date_of_belonging(d.pop("dateOfBelonging", UNSET))

        def _parse_date_of_death(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_death_type_0 = isoparse(data).date()

                return date_of_death_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_death = _parse_date_of_death(d.pop("dateOfDeath", UNSET))

        def _parse_date_of_entry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_entry = _parse_date_of_entry(d.pop("dateOfEntry", UNSET))

        def _parse_date_of_resign(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_resign = _parse_date_of_resign(d.pop("dateOfResign", UNSET))

        department_ids = cast(list[int], d.pop("departmentIds", UNSET))

        email = d.pop("email", UNSET)

        emails = []
        _emails = d.pop("emails", UNSET)
        for emails_item_data in _emails or []:
            emails_item = ServiceExchangeRequestRequestedPersonEmailsItem.from_dict(
                emails_item_data
            )

            emails.append(emails_item)

        def _parse_family_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family_image_url = _parse_family_image_url(d.pop("familyImageUrl", UNSET))

        def _parse_family_status_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        family_status_id = _parse_family_status_id(d.pop("familyStatusId", UNSET))

        fax = d.pop("fax", UNSET)

        def _parse_first_contact(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_contact = _parse_first_contact(d.pop("firstContact", UNSET))

        first_name = d.pop("firstName", UNSET)

        grow_path_id = d.pop("growPathId", UNSET)

        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("imageUrl", UNSET))

        def _parse_invitation_status(
            data: object,
        ) -> None | ServiceExchangeRequestRequestedPersonInvitationStatusType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invitation_status_type_0 = (
                    ServiceExchangeRequestRequestedPersonInvitationStatusType0(data)
                )

                return invitation_status_type_0
            except:  # noqa: E722
                pass
            return cast(
                None
                | ServiceExchangeRequestRequestedPersonInvitationStatusType0
                | Unset,
                data,
            )

        invitation_status = _parse_invitation_status(d.pop("invitationStatus", UNSET))

        is_archived = d.pop("isArchived", UNSET)

        is_dead = d.pop("isDead", UNSET)

        job = d.pop("job", UNSET)

        def _parse_last_edited_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_edited_date_type_0 = isoparse(data)

                return last_edited_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_edited_date = _parse_last_edited_date(d.pop("lastEditedDate", UNSET))

        def _parse_last_login(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_type_0 = isoparse(data)

                return last_login_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_login = _parse_last_login(d.pop("lastLogin", UNSET))

        last_name = d.pop("lastName", UNSET)

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_latitude_loose(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude_loose = _parse_latitude_loose(d.pop("latitudeLoose", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_longitude_loose(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude_loose = _parse_longitude_loose(d.pop("longitudeLoose", UNSET))

        _meta = d.pop("meta", UNSET)
        meta: ServiceExchangeRequestRequestedPersonMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ServiceExchangeRequestRequestedPersonMeta.from_dict(_meta)

        mobile = d.pop("mobile", UNSET)

        def _parse_nationality_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        nationality_id = _parse_nationality_id(d.pop("nationalityId", UNSET))

        nickname = d.pop("nickname", UNSET)

        optigem_id = d.pop("optigemId", UNSET)

        phone_private = d.pop("phonePrivate", UNSET)

        phone_work = d.pop("phoneWork", UNSET)

        place_of_baptism = d.pop("placeOfBaptism", UNSET)

        _privacy_policy_agreement = d.pop("privacyPolicyAgreement", UNSET)
        privacy_policy_agreement: (
            ServiceExchangeRequestRequestedPersonPrivacyPolicyAgreement | Unset
        )
        if isinstance(_privacy_policy_agreement, Unset):
            privacy_policy_agreement = UNSET
        else:
            privacy_policy_agreement = (
                ServiceExchangeRequestRequestedPersonPrivacyPolicyAgreement.from_dict(
                    _privacy_policy_agreement
                )
            )

        def _parse_privacy_policy_agreement_date(
            data: object,
        ) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                privacy_policy_agreement_date_type_0 = isoparse(data).date()

                return privacy_policy_agreement_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        privacy_policy_agreement_date = _parse_privacy_policy_agreement_date(
            d.pop("privacyPolicyAgreementDate", UNSET)
        )

        def _parse_privacy_policy_agreement_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        privacy_policy_agreement_type_id = _parse_privacy_policy_agreement_type_id(
            d.pop("privacyPolicyAgreementTypeId", UNSET)
        )

        def _parse_privacy_policy_agreement_who_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        privacy_policy_agreement_who_id = _parse_privacy_policy_agreement_who_id(
            d.pop("privacyPolicyAgreementWhoId", UNSET)
        )

        referred_by = d.pop("referredBy", UNSET)

        referred_to = d.pop("referredTo", UNSET)

        def _parse_sex_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sex_id = _parse_sex_id(d.pop("sexId", UNSET))

        status_id = d.pop("statusId", UNSET)

        street = d.pop("street", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = ServiceExchangeRequestRequestedPersonTagsItem.from_dict(
                tags_item_data
            )

            tags.append(tags_item)

        title = d.pop("title", UNSET)

        def _parse_wedding_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wedding_date_type_0 = isoparse(data).date()

                return wedding_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        wedding_date = _parse_wedding_date(d.pop("weddingDate", UNSET))

        zip_ = d.pop("zip", UNSET)

        service_exchange_request_requested_person = cls(
            edit_security_level_for_person=edit_security_level_for_person,
            guid=guid,
            id=id,
            security_level_for_person=security_level_for_person,
            acceptedsecurity=acceptedsecurity,
            address_addition=address_addition,
            age=age,
            baptised_by=baptised_by,
            birth_name=birth_name,
            birthday=birthday,
            birthplace=birthplace,
            campus_id=campus_id,
            can_chat=can_chat,
            chat_active=chat_active,
            city=city,
            cms_user_id=cms_user_id,
            country=country,
            date_of_baptism=date_of_baptism,
            date_of_belonging=date_of_belonging,
            date_of_death=date_of_death,
            date_of_entry=date_of_entry,
            date_of_resign=date_of_resign,
            department_ids=department_ids,
            email=email,
            emails=emails,
            family_image_url=family_image_url,
            family_status_id=family_status_id,
            fax=fax,
            first_contact=first_contact,
            first_name=first_name,
            grow_path_id=grow_path_id,
            image_url=image_url,
            invitation_status=invitation_status,
            is_archived=is_archived,
            is_dead=is_dead,
            job=job,
            last_edited_date=last_edited_date,
            last_login=last_login,
            last_name=last_name,
            latitude=latitude,
            latitude_loose=latitude_loose,
            longitude=longitude,
            longitude_loose=longitude_loose,
            meta=meta,
            mobile=mobile,
            nationality_id=nationality_id,
            nickname=nickname,
            optigem_id=optigem_id,
            phone_private=phone_private,
            phone_work=phone_work,
            place_of_baptism=place_of_baptism,
            privacy_policy_agreement=privacy_policy_agreement,
            privacy_policy_agreement_date=privacy_policy_agreement_date,
            privacy_policy_agreement_type_id=privacy_policy_agreement_type_id,
            privacy_policy_agreement_who_id=privacy_policy_agreement_who_id,
            referred_by=referred_by,
            referred_to=referred_to,
            sex_id=sex_id,
            status_id=status_id,
            street=street,
            tags=tags,
            title=title,
            wedding_date=wedding_date,
            zip_=zip_,
        )

        service_exchange_request_requested_person.additional_properties = d
        return service_exchange_request_requested_person

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
