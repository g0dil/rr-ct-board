from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_person_body_person_email import PatchPersonBodyPersonEmail
    from ..models.patch_person_body_privacy_policy_agreement import (
        PatchPersonBodyPrivacyPolicyAgreement,
    )


T = TypeVar("T", bound="PatchPersonBody")


@_attrs_define
class PatchPersonBody:
    """
    Attributes:
        address_addition (str | Unset):
        age (int | Unset):
        baptised_by (str | Unset):
        birth_name (str | Unset):
        birthday (datetime.date | None | Unset):
        birthplace (str | Unset):
        campus_id (int | Unset):
        city (str | Unset):
        cms_user_id (str | Unset):
        country (str | Unset):
        date_of_baptism (datetime.date | None | Unset):
        date_of_belonging (datetime.date | None | Unset):
        date_of_death (datetime.date | None | Unset):
        date_of_entry (datetime.datetime | None | Unset):
        date_of_resign (datetime.datetime | None | Unset):
        department_ids (list[int] | Unset): Department IDs. At least one department MUST be set for a person. The last
            department ID cannot be deleted.
        email (str | Unset):
        emails (list[PatchPersonBodyPersonEmail] | Unset): Save many eMail addresses for person. If `emails` is present
            in request `email` is ignored.
        family_status_id (int | None | Unset):
        fax (str | Unset):
        first_contact (datetime.datetime | None | Unset):
        first_name (str | Unset):  Example: Alfred.
        grow_path_id (int | Unset):
        job (str | Unset):
        last_name (str | Unset):  Example: API Tester.
        mobile (str | Unset):
        nationality_id (int | None | Unset):  Example: 3.
        nickname (str | Unset):
        optigem_id (str | Unset):
        phone_private (str | Unset):
        phone_work (str | Unset):
        place_of_baptism (str | Unset):
        privacy_policy_agreement (PatchPersonBodyPrivacyPolicyAgreement | Unset): This object can be optional or
            required. Depending on your ChurchTools data security settings.
        referred_by (str | Unset):
        referred_to (str | Unset):
        sex_id (int | None | Unset):  Example: 1.
        status_id (int | Unset):  Example: 5.
        street (str | Unset):
        title (str | Unset):
        wedding_date (datetime.date | None | Unset):
        zip_ (str | Unset):
    """

    address_addition: str | Unset = UNSET
    age: int | Unset = UNSET
    baptised_by: str | Unset = UNSET
    birth_name: str | Unset = UNSET
    birthday: datetime.date | None | Unset = UNSET
    birthplace: str | Unset = UNSET
    campus_id: int | Unset = UNSET
    city: str | Unset = UNSET
    cms_user_id: str | Unset = UNSET
    country: str | Unset = UNSET
    date_of_baptism: datetime.date | None | Unset = UNSET
    date_of_belonging: datetime.date | None | Unset = UNSET
    date_of_death: datetime.date | None | Unset = UNSET
    date_of_entry: datetime.datetime | None | Unset = UNSET
    date_of_resign: datetime.datetime | None | Unset = UNSET
    department_ids: list[int] | Unset = UNSET
    email: str | Unset = UNSET
    emails: list[PatchPersonBodyPersonEmail] | Unset = UNSET
    family_status_id: int | None | Unset = UNSET
    fax: str | Unset = UNSET
    first_contact: datetime.datetime | None | Unset = UNSET
    first_name: str | Unset = UNSET
    grow_path_id: int | Unset = UNSET
    job: str | Unset = UNSET
    last_name: str | Unset = UNSET
    mobile: str | Unset = UNSET
    nationality_id: int | None | Unset = UNSET
    nickname: str | Unset = UNSET
    optigem_id: str | Unset = UNSET
    phone_private: str | Unset = UNSET
    phone_work: str | Unset = UNSET
    place_of_baptism: str | Unset = UNSET
    privacy_policy_agreement: PatchPersonBodyPrivacyPolicyAgreement | Unset = UNSET
    referred_by: str | Unset = UNSET
    referred_to: str | Unset = UNSET
    sex_id: int | None | Unset = UNSET
    status_id: int | Unset = UNSET
    street: str | Unset = UNSET
    title: str | Unset = UNSET
    wedding_date: datetime.date | None | Unset = UNSET
    zip_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        elif isinstance(self.date_of_entry, datetime.datetime):
            date_of_entry = self.date_of_entry.isoformat()
        else:
            date_of_entry = self.date_of_entry

        date_of_resign: None | str | Unset
        if isinstance(self.date_of_resign, Unset):
            date_of_resign = UNSET
        elif isinstance(self.date_of_resign, datetime.datetime):
            date_of_resign = self.date_of_resign.isoformat()
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

        family_status_id: int | None | Unset
        if isinstance(self.family_status_id, Unset):
            family_status_id = UNSET
        else:
            family_status_id = self.family_status_id

        fax = self.fax

        first_contact: None | str | Unset
        if isinstance(self.first_contact, Unset):
            first_contact = UNSET
        elif isinstance(self.first_contact, datetime.datetime):
            first_contact = self.first_contact.isoformat()
        else:
            first_contact = self.first_contact

        first_name = self.first_name

        grow_path_id = self.grow_path_id

        job = self.job

        last_name = self.last_name

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

        referred_by = self.referred_by

        referred_to = self.referred_to

        sex_id: int | None | Unset
        if isinstance(self.sex_id, Unset):
            sex_id = UNSET
        else:
            sex_id = self.sex_id

        status_id = self.status_id

        street = self.street

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
        field_dict.update({})
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
        if job is not UNSET:
            field_dict["job"] = job
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
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
        if title is not UNSET:
            field_dict["title"] = title
        if wedding_date is not UNSET:
            field_dict["weddingDate"] = wedding_date
        if zip_ is not UNSET:
            field_dict["zip"] = zip_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_person_body_person_email import PatchPersonBodyPersonEmail
        from ..models.patch_person_body_privacy_policy_agreement import (
            PatchPersonBodyPrivacyPolicyAgreement,
        )

        d = dict(src_dict)
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

        def _parse_date_of_entry(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_entry_type_0 = isoparse(data)

                return date_of_entry_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_of_entry = _parse_date_of_entry(d.pop("dateOfEntry", UNSET))

        def _parse_date_of_resign(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_resign_type_0 = isoparse(data)

                return date_of_resign_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_of_resign = _parse_date_of_resign(d.pop("dateOfResign", UNSET))

        department_ids = cast(list[int], d.pop("departmentIds", UNSET))

        email = d.pop("email", UNSET)

        emails = []
        _emails = d.pop("emails", UNSET)
        for emails_item_data in _emails or []:
            emails_item = PatchPersonBodyPersonEmail.from_dict(emails_item_data)

            emails.append(emails_item)

        def _parse_family_status_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        family_status_id = _parse_family_status_id(d.pop("familyStatusId", UNSET))

        fax = d.pop("fax", UNSET)

        def _parse_first_contact(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_contact_type_0 = isoparse(data)

                return first_contact_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_contact = _parse_first_contact(d.pop("firstContact", UNSET))

        first_name = d.pop("firstName", UNSET)

        grow_path_id = d.pop("growPathId", UNSET)

        job = d.pop("job", UNSET)

        last_name = d.pop("lastName", UNSET)

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
        privacy_policy_agreement: PatchPersonBodyPrivacyPolicyAgreement | Unset
        if isinstance(_privacy_policy_agreement, Unset):
            privacy_policy_agreement = UNSET
        else:
            privacy_policy_agreement = PatchPersonBodyPrivacyPolicyAgreement.from_dict(
                _privacy_policy_agreement
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

        patch_person_body = cls(
            address_addition=address_addition,
            age=age,
            baptised_by=baptised_by,
            birth_name=birth_name,
            birthday=birthday,
            birthplace=birthplace,
            campus_id=campus_id,
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
            family_status_id=family_status_id,
            fax=fax,
            first_contact=first_contact,
            first_name=first_name,
            grow_path_id=grow_path_id,
            job=job,
            last_name=last_name,
            mobile=mobile,
            nationality_id=nationality_id,
            nickname=nickname,
            optigem_id=optigem_id,
            phone_private=phone_private,
            phone_work=phone_work,
            place_of_baptism=place_of_baptism,
            privacy_policy_agreement=privacy_policy_agreement,
            referred_by=referred_by,
            referred_to=referred_to,
            sex_id=sex_id,
            status_id=status_id,
            street=street,
            title=title,
            wedding_date=wedding_date,
            zip_=zip_,
        )

        patch_person_body.additional_properties = d
        return patch_person_body

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
