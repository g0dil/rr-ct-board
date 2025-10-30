from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.put_config_response_200_allowcheckin import (
    PutConfigResponse200Allowcheckin,
)
from ..models.put_config_response_200_allowfinance import (
    PutConfigResponse200Allowfinance,
)
from ..models.put_config_response_200_allowldap import PutConfigResponse200Allowldap
from ..models.put_config_response_200_allowoptigemsync import (
    PutConfigResponse200Allowoptigemsync,
)
from ..models.put_config_response_200_allowsync import PutConfigResponse200Allowsync
from ..models.put_config_response_200_brand import PutConfigResponse200Brand
from ..models.put_config_response_200_chrome_active import (
    PutConfigResponse200ChromeActive,
)
from ..models.put_config_response_200_churchcustommodule_active import (
    PutConfigResponse200ChurchcustommoduleActive,
)
from ..models.put_config_response_200_currently_mail_sending import (
    PutConfigResponse200CurrentlyMailSending,
)
from ..models.put_config_response_200_email_server import (
    PutConfigResponse200EmailServer,
)
from ..models.put_config_response_200_feature_custommodule import (
    PutConfigResponse200FeatureCustommodule,
)
from ..models.put_config_response_200_finance_inmenu import (
    PutConfigResponse200FinanceInmenu,
)
from ..models.put_config_response_200_hostingservice import (
    PutConfigResponse200Hostingservice,
)
from ..models.put_config_response_200_https_only import PutConfigResponse200HttpsOnly
from ..models.put_config_response_200_language import PutConfigResponse200Language
from ..models.put_config_response_200_log_debug import PutConfigResponse200LogDebug
from ..models.put_config_response_200_mail_sending_in_background import (
    PutConfigResponse200MailSendingInBackground,
)
from ..models.put_config_response_200_memberlist_birthday_full import (
    PutConfigResponse200MemberlistBirthdayFull,
)
from ..models.put_config_response_200_memberlist_email import (
    PutConfigResponse200MemberlistEmail,
)
from ..models.put_config_response_200_memberlist_fax import (
    PutConfigResponse200MemberlistFax,
)
from ..models.put_config_response_200_memberlist_group_couples import (
    PutConfigResponse200MemberlistGroupCouples,
)
from ..models.put_config_response_200_memberlist_picture import (
    PutConfigResponse200MemberlistPicture,
)
from ..models.put_config_response_200_memberlist_salutation import (
    PutConfigResponse200MemberlistSalutation,
)
from ..models.put_config_response_200_memberlist_telefongeschaeftlich import (
    PutConfigResponse200MemberlistTelefongeschaeftlich,
)
from ..models.put_config_response_200_memberlist_telefonhandy import (
    PutConfigResponse200MemberlistTelefonhandy,
)
from ..models.put_config_response_200_memberlist_telefonprivat import (
    PutConfigResponse200MemberlistTelefonprivat,
)
from ..models.put_config_response_200_orderstatus import PutConfigResponse200Orderstatus
from ..models.put_config_response_200_prevent_change_security_settings import (
    PutConfigResponse200PreventChangeSecuritySettings,
)
from ..models.put_config_response_200_safe_mode_enable_authorized_persons import (
    PutConfigResponse200SafeModeEnableAuthorizedPersons,
)
from ..models.put_config_response_200_safe_mode_enable_chat_sync import (
    PutConfigResponse200SafeModeEnableChatSync,
)
from ..models.put_config_response_200_safe_mode_enable_consolidation import (
    PutConfigResponse200SafeModeEnableConsolidation,
)
from ..models.put_config_response_200_safe_mode_enable_guid_sync import (
    PutConfigResponse200SafeModeEnableGuidSync,
)
from ..models.put_config_response_200_safe_mode_enable_job_queueing import (
    PutConfigResponse200SafeModeEnableJobQueueing,
)
from ..models.put_config_response_200_safe_mode_enable_mail import (
    PutConfigResponse200SafeModeEnableMail,
)
from ..models.put_config_response_200_safe_mode_enable_newsletter import (
    PutConfigResponse200SafeModeEnableNewsletter,
)
from ..models.put_config_response_200_safe_mode_enable_notification import (
    PutConfigResponse200SafeModeEnableNotification,
)
from ..models.put_config_response_200_test import PutConfigResponse200Test
from ..models.put_config_response_200_verification_status import (
    PutConfigResponse200VerificationStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_config_response_200_license_settings import (
        PutConfigResponse200LicenseSettings,
    )


T = TypeVar("T", bound="PutConfigResponse200")


@_attrs_define
class PutConfigResponse200:
    """
    Attributes:
        brand (PutConfigResponse200Brand):
        chat_server (str):
        finder_url (str):
        is_posts_active (bool):
        verification_status (PutConfigResponse200VerificationStatus):
        webchat_link (str):
        field_current_config_file (str | Unset):
        accept_datasecurity (bool | Unset):
        access_control_allow_credentials (bool | Unset):
        access_control_allow_origins (str | Unset):
        admin_ids (list[str] | Unset):
        admin_mail (str | Unset):
        admin_message (str | Unset):
        ai_assistant_available (bool | Unset):
        ai_description_available_generation_count (float | Unset):
        ai_description_available_generation_tests (float | Unset):
        ai_description_generation_count (float | Unset):
        ai_description_generation_enabled (bool | Unset):
        ai_description_total_generation_count (float | Unset):
        allowaiassistant (bool | Unset):
        allowcheckin (PutConfigResponse200Allowcheckin | Unset): This is a string that can only be true or false.
        allowedcals (str | Unset):
        allowedclients (str | Unset):
        allowedcwbusers (str | Unset):
        allowedresources (str | Unset):
        allowedservices (str | Unset):
        allowedstations (str | Unset):
        allowedsyncconnections (str | Unset):
        allowedsyncjobs (str | Unset):
        alloweduser (str | Unset):
        allowfinance (PutConfigResponse200Allowfinance | Unset): This is a string that can only be true or false.
        allowldap (PutConfigResponse200Allowldap | Unset): This is a string that can only be true or false.
        allowoptigemsync (PutConfigResponse200Allowoptigemsync | Unset): This is a string that can only be true or
            false.
        allowsync (PutConfigResponse200Allowsync | Unset): This is a string that can only be true or false.
        alpha_book_affiliate_id (str | Unset):
        alpha_book_enabled (bool | Unset):
        app_security_request (bool | Unset):
        authorized_persons (str | Unset):
        build (str | Unset):
        ccli_access_token (str | Unset):
        ccli_auto_reporting_enabled (bool | Unset):
        ccli_last_token_refresh (str | Unset):
        ccli_refresh_token (str | Unset):
        chrome_active (PutConfigResponse200ChromeActive | Unset): This is a string that can only be true or false.
        chrome_binary (str | Unset):
        churchcal_active (bool | Unset):
        churchcal_css (str | Unset):
        churchcal_entries_last_days (int | Unset):
        churchcal_firstdayinweek (int | Unset):
        churchcal_maincalname (str | Unset):
        churchcal_name (str | Unset):
        churchcal_name_default (str | Unset):
        churchcal_sortcode (int | Unset):
        churchchat_allow_event_chat (bool | Unset):
        churchchat_allow_group_chat (bool | Unset):
        churchchat_allow_person_chat (bool | Unset):
        churchchat_delete_event_chat_after_x_days (int | Unset):
        churchchat_invite_ct_event_chat (bool | Unset):
        churchchat_invite_ct_group_chat (bool | Unset):
        churchchat_name (str | Unset):
        churchchat_name_default (str | Unset):
        churchchat_sortcode (int | Unset):
        churchchat_start_event_chat_before_x_days (int | Unset):
        churchchat_start_event_chat_for_calendars (str | Unset): A stringified array of calendar ids
        churchchat_sync_user_id (int | Unset):
        churchcheckin_active (bool | Unset):
        churchcheckin_label_child (str | Unset):
        churchcheckin_label_parent (str | Unset):
        churchcheckin_label_standard (str | Unset):
        churchcheckin_name (str | Unset):
        churchcheckin_name_default (str | Unset):
        churchcheckin_sortcode (int | Unset):
        churchcheckin_tags (str | Unset):
        churchcustommodule_active (PutConfigResponse200ChurchcustommoduleActive | Unset): This is a string that can only
            be true or false.
        churchcustommodule_name (str | Unset):
        churchcustommodule_name_default (str | Unset):
        churchdb_active (bool | Unset):
        churchdb_archivedeletehistory (bool | Unset):
        churchdb_birthdaylist_station (str | Unset):
        churchdb_birthdaylist_status (str | Unset):
        churchdb_cleverreach_client_id (str | Unset):
        churchdb_cleverreach_client_secret (str | Unset):
        churchdb_cleverreach_connected (bool | Unset):
        churchdb_emailseparator (str | Unset):
        churchdb_groupnotchoosable (int | Unset):
        churchdb_home_lat (str | Unset):
        churchdb_home_lng (str | Unset):
        churchdb_mailchimp_apikey (str | Unset):
        churchdb_mailchimp_connected (bool | Unset):
        churchdb_mailjet_apikey (str | Unset):
        churchdb_mailjet_apisecret (str | Unset):
        churchdb_mailjet_connected (bool | Unset):
        churchdb_memberlist_station (str | Unset):
        churchdb_memberlist_status (str | Unset):
        churchdb_name (str | Unset):
        churchdb_name_default (str | Unset):
        churchdb_sendgroupmails (bool | Unset):
        churchdb_smscmtelecom_apikey (str | Unset):
        churchdb_smspromote_apikey (str | Unset):
        churchdb_sortcode (int | Unset):
        churchfinance_active (bool | Unset):
        churchfinance_name (str | Unset):
        churchfinance_name_default (str | Unset):
        churchfinance_sortcode (int | Unset):
        churchgroup_active (bool | Unset):
        churchgroup_inmenu (bool | Unset):
        churchgroup_name (str | Unset):
        churchgroup_name_default (str | Unset):
        churchgroup_sortcode (str | Unset):
        churchreport_active (bool | Unset):
        churchreport_name (str | Unset):
        churchreport_name_default (str | Unset):
        churchreport_sortcode (int | Unset):
        churchresource_active (bool | Unset):
        churchresource_anonymize_for_public_user (bool | Unset):
        churchresource_entries_last_days (int | Unset):
        churchresource_name (str | Unset):
        churchresource_name_default (str | Unset):
        churchresource_send_emails (bool | Unset):
        churchresource_sortcode (int | Unset):
        churchservice_active (bool | Unset):
        churchservice_agendashowenumeration (bool | Unset):
        churchservice_ccli_token (str | Unset):
        churchservice_ccli_token_secret (str | Unset):
        churchservice_entries_last_days (int | Unset):
        churchservice_invite_persons (bool | Unset):
        churchservice_name (str | Unset):
        churchservice_name_default (str | Unset):
        churchservice_openservice_rememberdays (int | Unset):
        churchservice_reminderhours (int | Unset):
        churchservice_songwithcategoryasdir (bool | Unset):
        churchservice_sortcode (int | Unset):
        churchsync_active (bool | Unset):
        churchsync_inmenu (bool | Unset):
        churchsync_name (str | Unset):
        churchsync_name_default (str | Unset):
        churchsync_sortcode (str | Unset):
        churchwiki_active (bool | Unset):
        churchwiki_name (str | Unset):
        churchwiki_name_default (str | Unset):
        churchwiki_sortcode (int | Unset):
        cron_daily (datetime.datetime | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        cron_hour_8 (datetime.datetime | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z' Example:
            2022-10-19T12:00:00Z.
        cronjob_delay (int | Unset):
        csrf_enabled (bool | Unset):
        currently_mail_sending (PutConfigResponse200CurrentlyMailSending | Unset): This is a string that can only be
            true or false.
        datasecurity_privacy_declaration_wiki_link (str | Unset):
        datasecurity_banner_enabled (bool | Unset):
        datasecurity_privacy_agreement_hint (str | Unset): Only in extended config
        datasecurity_privacy_agreement_text (str | Unset): Only in extended config
        datasecurity_privacy_agreement_text_for_children (str | Unset): Only in extended config
        db_name (str | Unset):
        db_password (str | Unset):
        db_server (str | Unset):
        db_user (str | Unset):
        default_phone_area_code (str | Unset):
        email_server (PutConfigResponse200EmailServer | Unset):
        encryptionkey (str | Unset):
        env (str | Unset):
        evangelische_termine_api_key (str | Unset):
        evangelische_termine_enabled (bool | Unset):
        evangelische_termine_name (str | Unset):
        evangelische_termine_url (str | Unset):
        evangelische_termine_vid (str | Unset):
        feature_custommodule (PutConfigResponse200FeatureCustommodule | Unset): This is a string that can only be true
            or false.
        finance_active (bool | Unset):
        finance_inmenu (PutConfigResponse200FinanceInmenu | Unset): This is a string that can only be true or false.
        finance_name (str | Unset):
        finance_name_default (str | Unset):
        finance_sortcode (str | Unset):
        first_sync_job (datetime.datetime | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z'
            Example: 2022-10-19T12:00:00Z.
        first_transaction (datetime.datetime | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z'
            Example: 2022-10-19T12:00:00Z.
        hide_beta_states (bool | Unset):
        hide_all_hints (bool | Unset):
        hostingservice (PutConfigResponse200Hostingservice | Unset): This is a string that can only be true or false.
        https_only (PutConfigResponse200HttpsOnly | Unset): This is a string that can only be true or false.
        image_extension (str | Unset):
        impressum_external (bool | Unset):
        impressum_external_link (str | Unset):
        impressum_internal (bool | Unset):
        imprint_wiki_link (str | Unset):
        installation_verification_code (str | Unset):
        invite_email_text (str | Unset):
        is_saml_active (bool | Unset):
        is_churchtools_blog_widget_active (bool | Unset):
        is_churchtools_onboarding_widget_active (bool | Unset):
        is_pr_widget_active (bool | Unset):
        is_rss_widget_active (bool | Unset):
        language (PutConfigResponse200Language | Unset): The language code is a two-letter code that represents the
            language. For example, "en" for English, "de" for German, and "fr" for French.
        last_cron (str | Unset):
        last_cron_finished (str | Unset):
        last_import_clear (str | Unset):
        last_translation_update (str | Unset):
        ldap_otp_enabled (bool | Unset):
        license_settings (PutConfigResponse200LicenseSettings | Unset):
        log_debug (PutConfigResponse200LogDebug | Unset): This is a string that can only be true or false.
        login_message (str | Unset):
        mail_enabled (bool | Unset):
        mail_sending_in_background (PutConfigResponse200MailSendingInBackground | Unset): This is a string that can only
            be true or false.
        mail_sending_starttime (str | Unset):
        mail_smtp_args_host (str | Unset):
        mail_smtp_args_password (str | Unset):
        mail_smtp_args_port (str | Unset):
        mail_smtp_args_smtpsecure (str | Unset):
        mail_smtp_args_username (str | Unset):
        max_uploadfile_size_kb (int | Unset):
        memberlist_birthday_full (PutConfigResponse200MemberlistBirthdayFull | Unset): This is a string that can only be
            true or false.
        memberlist_email (PutConfigResponse200MemberlistEmail | Unset): This is a string that can only be true or false.
        memberlist_fax (PutConfigResponse200MemberlistFax | Unset): This is a string that can only be true or false.
        memberlist_group_couples (PutConfigResponse200MemberlistGroupCouples | Unset): This is a string that can only be
            true or false.
        memberlist_picture (PutConfigResponse200MemberlistPicture | Unset): This is a string that can only be true or
            false.
        memberlist_salutation (PutConfigResponse200MemberlistSalutation | Unset): This is a string that can only be true
            or false.
        memberlist_telefongeschaeftlich (PutConfigResponse200MemberlistTelefongeschaeftlich | Unset): This is a string
            that can only be true or false.
        memberlist_telefonhandy (PutConfigResponse200MemberlistTelefonhandy | Unset): This is a string that can only be
            true or false.
        memberlist_telefonprivat (PutConfigResponse200MemberlistTelefonprivat | Unset): This is a string that can only
            be true or false.
        onboarding_start (datetime.datetime | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z'
            Example: 2022-10-19T12:00:00Z.
        openstreetmaps_enabled (bool | Unset):
        orderstatus (PutConfigResponse200Orderstatus | Unset):
        orderstatus_since_date (datetime.datetime | Unset): A timestamp in Zulu time format, e.g. '2022-10-19T12:00:00Z'
            Example: 2022-10-19T12:00:00Z.
        package (str | Unset):
        post_active (bool | Unset):
        post_edit_time_limited (bool | Unset):
        post_email_summary_default_enabled (bool | Unset):
        post_featured_groups (str | Unset):
        post_name (str | Unset):
        post_sortcode (int | Unset):
        post_wizard_completed (bool | Unset):
        post_wizard_groups (str | Unset):
        prevent_change_security_settings (PutConfigResponse200PreventChangeSecuritySettings | Unset):
        prevent_export (bool | Unset):
        prevent_manual_finance_account_creation (bool | Unset):
        privacy_policy_external (bool | Unset):
        privacy_policy_external_link (str | Unset):
        privacy_policy_fields_mandatory (bool | Unset):
        privacy_policy_fields_mandatory_api (bool | Unset):
        privacy_policy_internal (bool | Unset):
        privacy_policy_relationships (str | Unset):
        profile (str | Unset):
        public_channel_registry_url (str | Unset):
        rabbitmq_config_host (str | Unset):
        rabbitmq_config_password (str | Unset):
        rabbitmq_config_port (str | Unset):
        rabbitmq_config_user (str | Unset):
        rss_widget_link (str | Unset):
        safe_mode_enable_authorized_persons (PutConfigResponse200SafeModeEnableAuthorizedPersons | Unset): This is a
            string that can only be true or false.
        safe_mode_enable_chat_sync (PutConfigResponse200SafeModeEnableChatSync | Unset): This is a string that can only
            be true or false.
        safe_mode_enable_consolidation (PutConfigResponse200SafeModeEnableConsolidation | Unset): This is a string that
            can only be true or false.
        safe_mode_enable_guid_sync (PutConfigResponse200SafeModeEnableGuidSync | Unset): This is a string that can only
            be true or false.
        safe_mode_enable_job_queueing (PutConfigResponse200SafeModeEnableJobQueueing | Unset): This is a string that can
            only be true or false.
        safe_mode_enable_mail (PutConfigResponse200SafeModeEnableMail | Unset): This is a string that can only be true
            or false.
        safe_mode_enable_newsletter (PutConfigResponse200SafeModeEnableNewsletter | Unset): This is a string that can
            only be true or false.
        safe_mode_enable_notification (PutConfigResponse200SafeModeEnableNotification | Unset): This is a string that
            can only be true or false.
        send_data_security_mails (bool | Unset):
        short_name (str | Unset):
        show_ai_assistant (bool | Unset):
        show_remember_me (bool | Unset):
        site_language (str | Unset):
        site_licensekey (str | Unset):
        site_logo (str | Unset):
        site_mail (str | Unset):
        site_name (str | Unset):
        site_offline (bool | Unset):
        site_startpage (str | Unset):
        site_url (str | Unset):
        support_user_active_since (datetime.datetime | Unset): A timestamp in Zulu time format, e.g.
            '2022-10-19T12:00:00Z' Example: 2022-10-19T12:00:00Z.
        test (PutConfigResponse200Test | Unset): This is a string that can only be true or false.
        timezone (str | Unset):
        version (str | Unset):
        website_order_status (str | Unset):
        website_sync_user_id (str | Unset):
        website_testphase_date (str | Unset):
        website_trial_user_id (int | Unset):
        website_url (str | Unset):
        welcome (str | Unset):
        welcome_subtext (str | Unset):
    """

    brand: PutConfigResponse200Brand
    chat_server: str
    finder_url: str
    is_posts_active: bool
    verification_status: PutConfigResponse200VerificationStatus
    webchat_link: str
    field_current_config_file: str | Unset = UNSET
    accept_datasecurity: bool | Unset = UNSET
    access_control_allow_credentials: bool | Unset = UNSET
    access_control_allow_origins: str | Unset = UNSET
    admin_ids: list[str] | Unset = UNSET
    admin_mail: str | Unset = UNSET
    admin_message: str | Unset = UNSET
    ai_assistant_available: bool | Unset = UNSET
    ai_description_available_generation_count: float | Unset = UNSET
    ai_description_available_generation_tests: float | Unset = UNSET
    ai_description_generation_count: float | Unset = UNSET
    ai_description_generation_enabled: bool | Unset = UNSET
    ai_description_total_generation_count: float | Unset = UNSET
    allowaiassistant: bool | Unset = UNSET
    allowcheckin: PutConfigResponse200Allowcheckin | Unset = UNSET
    allowedcals: str | Unset = UNSET
    allowedclients: str | Unset = UNSET
    allowedcwbusers: str | Unset = UNSET
    allowedresources: str | Unset = UNSET
    allowedservices: str | Unset = UNSET
    allowedstations: str | Unset = UNSET
    allowedsyncconnections: str | Unset = UNSET
    allowedsyncjobs: str | Unset = UNSET
    alloweduser: str | Unset = UNSET
    allowfinance: PutConfigResponse200Allowfinance | Unset = UNSET
    allowldap: PutConfigResponse200Allowldap | Unset = UNSET
    allowoptigemsync: PutConfigResponse200Allowoptigemsync | Unset = UNSET
    allowsync: PutConfigResponse200Allowsync | Unset = UNSET
    alpha_book_affiliate_id: str | Unset = UNSET
    alpha_book_enabled: bool | Unset = UNSET
    app_security_request: bool | Unset = UNSET
    authorized_persons: str | Unset = UNSET
    build: str | Unset = UNSET
    ccli_access_token: str | Unset = UNSET
    ccli_auto_reporting_enabled: bool | Unset = UNSET
    ccli_last_token_refresh: str | Unset = UNSET
    ccli_refresh_token: str | Unset = UNSET
    chrome_active: PutConfigResponse200ChromeActive | Unset = UNSET
    chrome_binary: str | Unset = UNSET
    churchcal_active: bool | Unset = UNSET
    churchcal_css: str | Unset = UNSET
    churchcal_entries_last_days: int | Unset = UNSET
    churchcal_firstdayinweek: int | Unset = UNSET
    churchcal_maincalname: str | Unset = UNSET
    churchcal_name: str | Unset = UNSET
    churchcal_name_default: str | Unset = UNSET
    churchcal_sortcode: int | Unset = UNSET
    churchchat_allow_event_chat: bool | Unset = UNSET
    churchchat_allow_group_chat: bool | Unset = UNSET
    churchchat_allow_person_chat: bool | Unset = UNSET
    churchchat_delete_event_chat_after_x_days: int | Unset = UNSET
    churchchat_invite_ct_event_chat: bool | Unset = UNSET
    churchchat_invite_ct_group_chat: bool | Unset = UNSET
    churchchat_name: str | Unset = UNSET
    churchchat_name_default: str | Unset = UNSET
    churchchat_sortcode: int | Unset = UNSET
    churchchat_start_event_chat_before_x_days: int | Unset = UNSET
    churchchat_start_event_chat_for_calendars: str | Unset = UNSET
    churchchat_sync_user_id: int | Unset = UNSET
    churchcheckin_active: bool | Unset = UNSET
    churchcheckin_label_child: str | Unset = UNSET
    churchcheckin_label_parent: str | Unset = UNSET
    churchcheckin_label_standard: str | Unset = UNSET
    churchcheckin_name: str | Unset = UNSET
    churchcheckin_name_default: str | Unset = UNSET
    churchcheckin_sortcode: int | Unset = UNSET
    churchcheckin_tags: str | Unset = UNSET
    churchcustommodule_active: PutConfigResponse200ChurchcustommoduleActive | Unset = (
        UNSET
    )
    churchcustommodule_name: str | Unset = UNSET
    churchcustommodule_name_default: str | Unset = UNSET
    churchdb_active: bool | Unset = UNSET
    churchdb_archivedeletehistory: bool | Unset = UNSET
    churchdb_birthdaylist_station: str | Unset = UNSET
    churchdb_birthdaylist_status: str | Unset = UNSET
    churchdb_cleverreach_client_id: str | Unset = UNSET
    churchdb_cleverreach_client_secret: str | Unset = UNSET
    churchdb_cleverreach_connected: bool | Unset = UNSET
    churchdb_emailseparator: str | Unset = UNSET
    churchdb_groupnotchoosable: int | Unset = UNSET
    churchdb_home_lat: str | Unset = UNSET
    churchdb_home_lng: str | Unset = UNSET
    churchdb_mailchimp_apikey: str | Unset = UNSET
    churchdb_mailchimp_connected: bool | Unset = UNSET
    churchdb_mailjet_apikey: str | Unset = UNSET
    churchdb_mailjet_apisecret: str | Unset = UNSET
    churchdb_mailjet_connected: bool | Unset = UNSET
    churchdb_memberlist_station: str | Unset = UNSET
    churchdb_memberlist_status: str | Unset = UNSET
    churchdb_name: str | Unset = UNSET
    churchdb_name_default: str | Unset = UNSET
    churchdb_sendgroupmails: bool | Unset = UNSET
    churchdb_smscmtelecom_apikey: str | Unset = UNSET
    churchdb_smspromote_apikey: str | Unset = UNSET
    churchdb_sortcode: int | Unset = UNSET
    churchfinance_active: bool | Unset = UNSET
    churchfinance_name: str | Unset = UNSET
    churchfinance_name_default: str | Unset = UNSET
    churchfinance_sortcode: int | Unset = UNSET
    churchgroup_active: bool | Unset = UNSET
    churchgroup_inmenu: bool | Unset = UNSET
    churchgroup_name: str | Unset = UNSET
    churchgroup_name_default: str | Unset = UNSET
    churchgroup_sortcode: str | Unset = UNSET
    churchreport_active: bool | Unset = UNSET
    churchreport_name: str | Unset = UNSET
    churchreport_name_default: str | Unset = UNSET
    churchreport_sortcode: int | Unset = UNSET
    churchresource_active: bool | Unset = UNSET
    churchresource_anonymize_for_public_user: bool | Unset = UNSET
    churchresource_entries_last_days: int | Unset = UNSET
    churchresource_name: str | Unset = UNSET
    churchresource_name_default: str | Unset = UNSET
    churchresource_send_emails: bool | Unset = UNSET
    churchresource_sortcode: int | Unset = UNSET
    churchservice_active: bool | Unset = UNSET
    churchservice_agendashowenumeration: bool | Unset = UNSET
    churchservice_ccli_token: str | Unset = UNSET
    churchservice_ccli_token_secret: str | Unset = UNSET
    churchservice_entries_last_days: int | Unset = UNSET
    churchservice_invite_persons: bool | Unset = UNSET
    churchservice_name: str | Unset = UNSET
    churchservice_name_default: str | Unset = UNSET
    churchservice_openservice_rememberdays: int | Unset = UNSET
    churchservice_reminderhours: int | Unset = UNSET
    churchservice_songwithcategoryasdir: bool | Unset = UNSET
    churchservice_sortcode: int | Unset = UNSET
    churchsync_active: bool | Unset = UNSET
    churchsync_inmenu: bool | Unset = UNSET
    churchsync_name: str | Unset = UNSET
    churchsync_name_default: str | Unset = UNSET
    churchsync_sortcode: str | Unset = UNSET
    churchwiki_active: bool | Unset = UNSET
    churchwiki_name: str | Unset = UNSET
    churchwiki_name_default: str | Unset = UNSET
    churchwiki_sortcode: int | Unset = UNSET
    cron_daily: datetime.datetime | Unset = UNSET
    cron_hour_8: datetime.datetime | Unset = UNSET
    cronjob_delay: int | Unset = UNSET
    csrf_enabled: bool | Unset = UNSET
    currently_mail_sending: PutConfigResponse200CurrentlyMailSending | Unset = UNSET
    datasecurity_privacy_declaration_wiki_link: str | Unset = UNSET
    datasecurity_banner_enabled: bool | Unset = UNSET
    datasecurity_privacy_agreement_hint: str | Unset = UNSET
    datasecurity_privacy_agreement_text: str | Unset = UNSET
    datasecurity_privacy_agreement_text_for_children: str | Unset = UNSET
    db_name: str | Unset = UNSET
    db_password: str | Unset = UNSET
    db_server: str | Unset = UNSET
    db_user: str | Unset = UNSET
    default_phone_area_code: str | Unset = UNSET
    email_server: PutConfigResponse200EmailServer | Unset = UNSET
    encryptionkey: str | Unset = UNSET
    env: str | Unset = UNSET
    evangelische_termine_api_key: str | Unset = UNSET
    evangelische_termine_enabled: bool | Unset = UNSET
    evangelische_termine_name: str | Unset = UNSET
    evangelische_termine_url: str | Unset = UNSET
    evangelische_termine_vid: str | Unset = UNSET
    feature_custommodule: PutConfigResponse200FeatureCustommodule | Unset = UNSET
    finance_active: bool | Unset = UNSET
    finance_inmenu: PutConfigResponse200FinanceInmenu | Unset = UNSET
    finance_name: str | Unset = UNSET
    finance_name_default: str | Unset = UNSET
    finance_sortcode: str | Unset = UNSET
    first_sync_job: datetime.datetime | Unset = UNSET
    first_transaction: datetime.datetime | Unset = UNSET
    hide_beta_states: bool | Unset = UNSET
    hide_all_hints: bool | Unset = UNSET
    hostingservice: PutConfigResponse200Hostingservice | Unset = UNSET
    https_only: PutConfigResponse200HttpsOnly | Unset = UNSET
    image_extension: str | Unset = UNSET
    impressum_external: bool | Unset = UNSET
    impressum_external_link: str | Unset = UNSET
    impressum_internal: bool | Unset = UNSET
    imprint_wiki_link: str | Unset = UNSET
    installation_verification_code: str | Unset = UNSET
    invite_email_text: str | Unset = UNSET
    is_saml_active: bool | Unset = UNSET
    is_churchtools_blog_widget_active: bool | Unset = UNSET
    is_churchtools_onboarding_widget_active: bool | Unset = UNSET
    is_pr_widget_active: bool | Unset = UNSET
    is_rss_widget_active: bool | Unset = UNSET
    language: PutConfigResponse200Language | Unset = UNSET
    last_cron: str | Unset = UNSET
    last_cron_finished: str | Unset = UNSET
    last_import_clear: str | Unset = UNSET
    last_translation_update: str | Unset = UNSET
    ldap_otp_enabled: bool | Unset = UNSET
    license_settings: PutConfigResponse200LicenseSettings | Unset = UNSET
    log_debug: PutConfigResponse200LogDebug | Unset = UNSET
    login_message: str | Unset = UNSET
    mail_enabled: bool | Unset = UNSET
    mail_sending_in_background: PutConfigResponse200MailSendingInBackground | Unset = (
        UNSET
    )
    mail_sending_starttime: str | Unset = UNSET
    mail_smtp_args_host: str | Unset = UNSET
    mail_smtp_args_password: str | Unset = UNSET
    mail_smtp_args_port: str | Unset = UNSET
    mail_smtp_args_smtpsecure: str | Unset = UNSET
    mail_smtp_args_username: str | Unset = UNSET
    max_uploadfile_size_kb: int | Unset = UNSET
    memberlist_birthday_full: PutConfigResponse200MemberlistBirthdayFull | Unset = UNSET
    memberlist_email: PutConfigResponse200MemberlistEmail | Unset = UNSET
    memberlist_fax: PutConfigResponse200MemberlistFax | Unset = UNSET
    memberlist_group_couples: PutConfigResponse200MemberlistGroupCouples | Unset = UNSET
    memberlist_picture: PutConfigResponse200MemberlistPicture | Unset = UNSET
    memberlist_salutation: PutConfigResponse200MemberlistSalutation | Unset = UNSET
    memberlist_telefongeschaeftlich: (
        PutConfigResponse200MemberlistTelefongeschaeftlich | Unset
    ) = UNSET
    memberlist_telefonhandy: PutConfigResponse200MemberlistTelefonhandy | Unset = UNSET
    memberlist_telefonprivat: PutConfigResponse200MemberlistTelefonprivat | Unset = (
        UNSET
    )
    onboarding_start: datetime.datetime | Unset = UNSET
    openstreetmaps_enabled: bool | Unset = UNSET
    orderstatus: PutConfigResponse200Orderstatus | Unset = UNSET
    orderstatus_since_date: datetime.datetime | Unset = UNSET
    package: str | Unset = UNSET
    post_active: bool | Unset = UNSET
    post_edit_time_limited: bool | Unset = UNSET
    post_email_summary_default_enabled: bool | Unset = UNSET
    post_featured_groups: str | Unset = UNSET
    post_name: str | Unset = UNSET
    post_sortcode: int | Unset = UNSET
    post_wizard_completed: bool | Unset = UNSET
    post_wizard_groups: str | Unset = UNSET
    prevent_change_security_settings: (
        PutConfigResponse200PreventChangeSecuritySettings | Unset
    ) = UNSET
    prevent_export: bool | Unset = UNSET
    prevent_manual_finance_account_creation: bool | Unset = UNSET
    privacy_policy_external: bool | Unset = UNSET
    privacy_policy_external_link: str | Unset = UNSET
    privacy_policy_fields_mandatory: bool | Unset = UNSET
    privacy_policy_fields_mandatory_api: bool | Unset = UNSET
    privacy_policy_internal: bool | Unset = UNSET
    privacy_policy_relationships: str | Unset = UNSET
    profile: str | Unset = UNSET
    public_channel_registry_url: str | Unset = UNSET
    rabbitmq_config_host: str | Unset = UNSET
    rabbitmq_config_password: str | Unset = UNSET
    rabbitmq_config_port: str | Unset = UNSET
    rabbitmq_config_user: str | Unset = UNSET
    rss_widget_link: str | Unset = UNSET
    safe_mode_enable_authorized_persons: (
        PutConfigResponse200SafeModeEnableAuthorizedPersons | Unset
    ) = UNSET
    safe_mode_enable_chat_sync: PutConfigResponse200SafeModeEnableChatSync | Unset = (
        UNSET
    )
    safe_mode_enable_consolidation: (
        PutConfigResponse200SafeModeEnableConsolidation | Unset
    ) = UNSET
    safe_mode_enable_guid_sync: PutConfigResponse200SafeModeEnableGuidSync | Unset = (
        UNSET
    )
    safe_mode_enable_job_queueing: (
        PutConfigResponse200SafeModeEnableJobQueueing | Unset
    ) = UNSET
    safe_mode_enable_mail: PutConfigResponse200SafeModeEnableMail | Unset = UNSET
    safe_mode_enable_newsletter: (
        PutConfigResponse200SafeModeEnableNewsletter | Unset
    ) = UNSET
    safe_mode_enable_notification: (
        PutConfigResponse200SafeModeEnableNotification | Unset
    ) = UNSET
    send_data_security_mails: bool | Unset = UNSET
    short_name: str | Unset = UNSET
    show_ai_assistant: bool | Unset = UNSET
    show_remember_me: bool | Unset = UNSET
    site_language: str | Unset = UNSET
    site_licensekey: str | Unset = UNSET
    site_logo: str | Unset = UNSET
    site_mail: str | Unset = UNSET
    site_name: str | Unset = UNSET
    site_offline: bool | Unset = UNSET
    site_startpage: str | Unset = UNSET
    site_url: str | Unset = UNSET
    support_user_active_since: datetime.datetime | Unset = UNSET
    test: PutConfigResponse200Test | Unset = UNSET
    timezone: str | Unset = UNSET
    version: str | Unset = UNSET
    website_order_status: str | Unset = UNSET
    website_sync_user_id: str | Unset = UNSET
    website_testphase_date: str | Unset = UNSET
    website_trial_user_id: int | Unset = UNSET
    website_url: str | Unset = UNSET
    welcome: str | Unset = UNSET
    welcome_subtext: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand = self.brand.value

        chat_server = self.chat_server

        finder_url = self.finder_url

        is_posts_active = self.is_posts_active

        verification_status = self.verification_status.value

        webchat_link = self.webchat_link

        field_current_config_file = self.field_current_config_file

        accept_datasecurity = self.accept_datasecurity

        access_control_allow_credentials = self.access_control_allow_credentials

        access_control_allow_origins = self.access_control_allow_origins

        admin_ids: list[str] | Unset = UNSET
        if not isinstance(self.admin_ids, Unset):
            admin_ids = self.admin_ids

        admin_mail = self.admin_mail

        admin_message = self.admin_message

        ai_assistant_available = self.ai_assistant_available

        ai_description_available_generation_count = (
            self.ai_description_available_generation_count
        )

        ai_description_available_generation_tests = (
            self.ai_description_available_generation_tests
        )

        ai_description_generation_count = self.ai_description_generation_count

        ai_description_generation_enabled = self.ai_description_generation_enabled

        ai_description_total_generation_count = (
            self.ai_description_total_generation_count
        )

        allowaiassistant = self.allowaiassistant

        allowcheckin: str | Unset = UNSET
        if not isinstance(self.allowcheckin, Unset):
            allowcheckin = self.allowcheckin.value

        allowedcals = self.allowedcals

        allowedclients = self.allowedclients

        allowedcwbusers = self.allowedcwbusers

        allowedresources = self.allowedresources

        allowedservices = self.allowedservices

        allowedstations = self.allowedstations

        allowedsyncconnections = self.allowedsyncconnections

        allowedsyncjobs = self.allowedsyncjobs

        alloweduser = self.alloweduser

        allowfinance: str | Unset = UNSET
        if not isinstance(self.allowfinance, Unset):
            allowfinance = self.allowfinance.value

        allowldap: str | Unset = UNSET
        if not isinstance(self.allowldap, Unset):
            allowldap = self.allowldap.value

        allowoptigemsync: str | Unset = UNSET
        if not isinstance(self.allowoptigemsync, Unset):
            allowoptigemsync = self.allowoptigemsync.value

        allowsync: str | Unset = UNSET
        if not isinstance(self.allowsync, Unset):
            allowsync = self.allowsync.value

        alpha_book_affiliate_id = self.alpha_book_affiliate_id

        alpha_book_enabled = self.alpha_book_enabled

        app_security_request = self.app_security_request

        authorized_persons = self.authorized_persons

        build = self.build

        ccli_access_token = self.ccli_access_token

        ccli_auto_reporting_enabled = self.ccli_auto_reporting_enabled

        ccli_last_token_refresh = self.ccli_last_token_refresh

        ccli_refresh_token = self.ccli_refresh_token

        chrome_active: str | Unset = UNSET
        if not isinstance(self.chrome_active, Unset):
            chrome_active = self.chrome_active.value

        chrome_binary = self.chrome_binary

        churchcal_active = self.churchcal_active

        churchcal_css = self.churchcal_css

        churchcal_entries_last_days = self.churchcal_entries_last_days

        churchcal_firstdayinweek = self.churchcal_firstdayinweek

        churchcal_maincalname = self.churchcal_maincalname

        churchcal_name = self.churchcal_name

        churchcal_name_default = self.churchcal_name_default

        churchcal_sortcode = self.churchcal_sortcode

        churchchat_allow_event_chat = self.churchchat_allow_event_chat

        churchchat_allow_group_chat = self.churchchat_allow_group_chat

        churchchat_allow_person_chat = self.churchchat_allow_person_chat

        churchchat_delete_event_chat_after_x_days = (
            self.churchchat_delete_event_chat_after_x_days
        )

        churchchat_invite_ct_event_chat = self.churchchat_invite_ct_event_chat

        churchchat_invite_ct_group_chat = self.churchchat_invite_ct_group_chat

        churchchat_name = self.churchchat_name

        churchchat_name_default = self.churchchat_name_default

        churchchat_sortcode = self.churchchat_sortcode

        churchchat_start_event_chat_before_x_days = (
            self.churchchat_start_event_chat_before_x_days
        )

        churchchat_start_event_chat_for_calendars = (
            self.churchchat_start_event_chat_for_calendars
        )

        churchchat_sync_user_id = self.churchchat_sync_user_id

        churchcheckin_active = self.churchcheckin_active

        churchcheckin_label_child = self.churchcheckin_label_child

        churchcheckin_label_parent = self.churchcheckin_label_parent

        churchcheckin_label_standard = self.churchcheckin_label_standard

        churchcheckin_name = self.churchcheckin_name

        churchcheckin_name_default = self.churchcheckin_name_default

        churchcheckin_sortcode = self.churchcheckin_sortcode

        churchcheckin_tags = self.churchcheckin_tags

        churchcustommodule_active: str | Unset = UNSET
        if not isinstance(self.churchcustommodule_active, Unset):
            churchcustommodule_active = self.churchcustommodule_active.value

        churchcustommodule_name = self.churchcustommodule_name

        churchcustommodule_name_default = self.churchcustommodule_name_default

        churchdb_active = self.churchdb_active

        churchdb_archivedeletehistory = self.churchdb_archivedeletehistory

        churchdb_birthdaylist_station = self.churchdb_birthdaylist_station

        churchdb_birthdaylist_status = self.churchdb_birthdaylist_status

        churchdb_cleverreach_client_id = self.churchdb_cleverreach_client_id

        churchdb_cleverreach_client_secret = self.churchdb_cleverreach_client_secret

        churchdb_cleverreach_connected = self.churchdb_cleverreach_connected

        churchdb_emailseparator = self.churchdb_emailseparator

        churchdb_groupnotchoosable = self.churchdb_groupnotchoosable

        churchdb_home_lat = self.churchdb_home_lat

        churchdb_home_lng = self.churchdb_home_lng

        churchdb_mailchimp_apikey = self.churchdb_mailchimp_apikey

        churchdb_mailchimp_connected = self.churchdb_mailchimp_connected

        churchdb_mailjet_apikey = self.churchdb_mailjet_apikey

        churchdb_mailjet_apisecret = self.churchdb_mailjet_apisecret

        churchdb_mailjet_connected = self.churchdb_mailjet_connected

        churchdb_memberlist_station = self.churchdb_memberlist_station

        churchdb_memberlist_status = self.churchdb_memberlist_status

        churchdb_name = self.churchdb_name

        churchdb_name_default = self.churchdb_name_default

        churchdb_sendgroupmails = self.churchdb_sendgroupmails

        churchdb_smscmtelecom_apikey = self.churchdb_smscmtelecom_apikey

        churchdb_smspromote_apikey = self.churchdb_smspromote_apikey

        churchdb_sortcode = self.churchdb_sortcode

        churchfinance_active = self.churchfinance_active

        churchfinance_name = self.churchfinance_name

        churchfinance_name_default = self.churchfinance_name_default

        churchfinance_sortcode = self.churchfinance_sortcode

        churchgroup_active = self.churchgroup_active

        churchgroup_inmenu = self.churchgroup_inmenu

        churchgroup_name = self.churchgroup_name

        churchgroup_name_default = self.churchgroup_name_default

        churchgroup_sortcode = self.churchgroup_sortcode

        churchreport_active = self.churchreport_active

        churchreport_name = self.churchreport_name

        churchreport_name_default = self.churchreport_name_default

        churchreport_sortcode = self.churchreport_sortcode

        churchresource_active = self.churchresource_active

        churchresource_anonymize_for_public_user = (
            self.churchresource_anonymize_for_public_user
        )

        churchresource_entries_last_days = self.churchresource_entries_last_days

        churchresource_name = self.churchresource_name

        churchresource_name_default = self.churchresource_name_default

        churchresource_send_emails = self.churchresource_send_emails

        churchresource_sortcode = self.churchresource_sortcode

        churchservice_active = self.churchservice_active

        churchservice_agendashowenumeration = self.churchservice_agendashowenumeration

        churchservice_ccli_token = self.churchservice_ccli_token

        churchservice_ccli_token_secret = self.churchservice_ccli_token_secret

        churchservice_entries_last_days = self.churchservice_entries_last_days

        churchservice_invite_persons = self.churchservice_invite_persons

        churchservice_name = self.churchservice_name

        churchservice_name_default = self.churchservice_name_default

        churchservice_openservice_rememberdays = (
            self.churchservice_openservice_rememberdays
        )

        churchservice_reminderhours = self.churchservice_reminderhours

        churchservice_songwithcategoryasdir = self.churchservice_songwithcategoryasdir

        churchservice_sortcode = self.churchservice_sortcode

        churchsync_active = self.churchsync_active

        churchsync_inmenu = self.churchsync_inmenu

        churchsync_name = self.churchsync_name

        churchsync_name_default = self.churchsync_name_default

        churchsync_sortcode = self.churchsync_sortcode

        churchwiki_active = self.churchwiki_active

        churchwiki_name = self.churchwiki_name

        churchwiki_name_default = self.churchwiki_name_default

        churchwiki_sortcode = self.churchwiki_sortcode

        cron_daily: str | Unset = UNSET
        if not isinstance(self.cron_daily, Unset):
            cron_daily = self.cron_daily.isoformat()

        cron_hour_8: str | Unset = UNSET
        if not isinstance(self.cron_hour_8, Unset):
            cron_hour_8 = self.cron_hour_8.isoformat()

        cronjob_delay = self.cronjob_delay

        csrf_enabled = self.csrf_enabled

        currently_mail_sending: str | Unset = UNSET
        if not isinstance(self.currently_mail_sending, Unset):
            currently_mail_sending = self.currently_mail_sending.value

        datasecurity_privacy_declaration_wiki_link = (
            self.datasecurity_privacy_declaration_wiki_link
        )

        datasecurity_banner_enabled = self.datasecurity_banner_enabled

        datasecurity_privacy_agreement_hint = self.datasecurity_privacy_agreement_hint

        datasecurity_privacy_agreement_text = self.datasecurity_privacy_agreement_text

        datasecurity_privacy_agreement_text_for_children = (
            self.datasecurity_privacy_agreement_text_for_children
        )

        db_name = self.db_name

        db_password = self.db_password

        db_server = self.db_server

        db_user = self.db_user

        default_phone_area_code = self.default_phone_area_code

        email_server: str | Unset = UNSET
        if not isinstance(self.email_server, Unset):
            email_server = self.email_server.value

        encryptionkey = self.encryptionkey

        env = self.env

        evangelische_termine_api_key = self.evangelische_termine_api_key

        evangelische_termine_enabled = self.evangelische_termine_enabled

        evangelische_termine_name = self.evangelische_termine_name

        evangelische_termine_url = self.evangelische_termine_url

        evangelische_termine_vid = self.evangelische_termine_vid

        feature_custommodule: str | Unset = UNSET
        if not isinstance(self.feature_custommodule, Unset):
            feature_custommodule = self.feature_custommodule.value

        finance_active = self.finance_active

        finance_inmenu: str | Unset = UNSET
        if not isinstance(self.finance_inmenu, Unset):
            finance_inmenu = self.finance_inmenu.value

        finance_name = self.finance_name

        finance_name_default = self.finance_name_default

        finance_sortcode = self.finance_sortcode

        first_sync_job: str | Unset = UNSET
        if not isinstance(self.first_sync_job, Unset):
            first_sync_job = self.first_sync_job.isoformat()

        first_transaction: str | Unset = UNSET
        if not isinstance(self.first_transaction, Unset):
            first_transaction = self.first_transaction.isoformat()

        hide_beta_states = self.hide_beta_states

        hide_all_hints = self.hide_all_hints

        hostingservice: str | Unset = UNSET
        if not isinstance(self.hostingservice, Unset):
            hostingservice = self.hostingservice.value

        https_only: str | Unset = UNSET
        if not isinstance(self.https_only, Unset):
            https_only = self.https_only.value

        image_extension = self.image_extension

        impressum_external = self.impressum_external

        impressum_external_link = self.impressum_external_link

        impressum_internal = self.impressum_internal

        imprint_wiki_link = self.imprint_wiki_link

        installation_verification_code = self.installation_verification_code

        invite_email_text = self.invite_email_text

        is_saml_active = self.is_saml_active

        is_churchtools_blog_widget_active = self.is_churchtools_blog_widget_active

        is_churchtools_onboarding_widget_active = (
            self.is_churchtools_onboarding_widget_active
        )

        is_pr_widget_active = self.is_pr_widget_active

        is_rss_widget_active = self.is_rss_widget_active

        language: str | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        last_cron = self.last_cron

        last_cron_finished = self.last_cron_finished

        last_import_clear = self.last_import_clear

        last_translation_update = self.last_translation_update

        ldap_otp_enabled = self.ldap_otp_enabled

        license_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.license_settings, Unset):
            license_settings = self.license_settings.to_dict()

        log_debug: str | Unset = UNSET
        if not isinstance(self.log_debug, Unset):
            log_debug = self.log_debug.value

        login_message = self.login_message

        mail_enabled = self.mail_enabled

        mail_sending_in_background: str | Unset = UNSET
        if not isinstance(self.mail_sending_in_background, Unset):
            mail_sending_in_background = self.mail_sending_in_background.value

        mail_sending_starttime = self.mail_sending_starttime

        mail_smtp_args_host = self.mail_smtp_args_host

        mail_smtp_args_password = self.mail_smtp_args_password

        mail_smtp_args_port = self.mail_smtp_args_port

        mail_smtp_args_smtpsecure = self.mail_smtp_args_smtpsecure

        mail_smtp_args_username = self.mail_smtp_args_username

        max_uploadfile_size_kb = self.max_uploadfile_size_kb

        memberlist_birthday_full: str | Unset = UNSET
        if not isinstance(self.memberlist_birthday_full, Unset):
            memberlist_birthday_full = self.memberlist_birthday_full.value

        memberlist_email: str | Unset = UNSET
        if not isinstance(self.memberlist_email, Unset):
            memberlist_email = self.memberlist_email.value

        memberlist_fax: str | Unset = UNSET
        if not isinstance(self.memberlist_fax, Unset):
            memberlist_fax = self.memberlist_fax.value

        memberlist_group_couples: str | Unset = UNSET
        if not isinstance(self.memberlist_group_couples, Unset):
            memberlist_group_couples = self.memberlist_group_couples.value

        memberlist_picture: str | Unset = UNSET
        if not isinstance(self.memberlist_picture, Unset):
            memberlist_picture = self.memberlist_picture.value

        memberlist_salutation: str | Unset = UNSET
        if not isinstance(self.memberlist_salutation, Unset):
            memberlist_salutation = self.memberlist_salutation.value

        memberlist_telefongeschaeftlich: str | Unset = UNSET
        if not isinstance(self.memberlist_telefongeschaeftlich, Unset):
            memberlist_telefongeschaeftlich = self.memberlist_telefongeschaeftlich.value

        memberlist_telefonhandy: str | Unset = UNSET
        if not isinstance(self.memberlist_telefonhandy, Unset):
            memberlist_telefonhandy = self.memberlist_telefonhandy.value

        memberlist_telefonprivat: str | Unset = UNSET
        if not isinstance(self.memberlist_telefonprivat, Unset):
            memberlist_telefonprivat = self.memberlist_telefonprivat.value

        onboarding_start: str | Unset = UNSET
        if not isinstance(self.onboarding_start, Unset):
            onboarding_start = self.onboarding_start.isoformat()

        openstreetmaps_enabled = self.openstreetmaps_enabled

        orderstatus: str | Unset = UNSET
        if not isinstance(self.orderstatus, Unset):
            orderstatus = self.orderstatus.value

        orderstatus_since_date: str | Unset = UNSET
        if not isinstance(self.orderstatus_since_date, Unset):
            orderstatus_since_date = self.orderstatus_since_date.isoformat()

        package = self.package

        post_active = self.post_active

        post_edit_time_limited = self.post_edit_time_limited

        post_email_summary_default_enabled = self.post_email_summary_default_enabled

        post_featured_groups = self.post_featured_groups

        post_name = self.post_name

        post_sortcode = self.post_sortcode

        post_wizard_completed = self.post_wizard_completed

        post_wizard_groups = self.post_wizard_groups

        prevent_change_security_settings: str | Unset = UNSET
        if not isinstance(self.prevent_change_security_settings, Unset):
            prevent_change_security_settings = (
                self.prevent_change_security_settings.value
            )

        prevent_export = self.prevent_export

        prevent_manual_finance_account_creation = (
            self.prevent_manual_finance_account_creation
        )

        privacy_policy_external = self.privacy_policy_external

        privacy_policy_external_link = self.privacy_policy_external_link

        privacy_policy_fields_mandatory = self.privacy_policy_fields_mandatory

        privacy_policy_fields_mandatory_api = self.privacy_policy_fields_mandatory_api

        privacy_policy_internal = self.privacy_policy_internal

        privacy_policy_relationships = self.privacy_policy_relationships

        profile = self.profile

        public_channel_registry_url = self.public_channel_registry_url

        rabbitmq_config_host = self.rabbitmq_config_host

        rabbitmq_config_password = self.rabbitmq_config_password

        rabbitmq_config_port = self.rabbitmq_config_port

        rabbitmq_config_user = self.rabbitmq_config_user

        rss_widget_link = self.rss_widget_link

        safe_mode_enable_authorized_persons: str | Unset = UNSET
        if not isinstance(self.safe_mode_enable_authorized_persons, Unset):
            safe_mode_enable_authorized_persons = (
                self.safe_mode_enable_authorized_persons.value
            )

        safe_mode_enable_chat_sync: str | Unset = UNSET
        if not isinstance(self.safe_mode_enable_chat_sync, Unset):
            safe_mode_enable_chat_sync = self.safe_mode_enable_chat_sync.value

        safe_mode_enable_consolidation: str | Unset = UNSET
        if not isinstance(self.safe_mode_enable_consolidation, Unset):
            safe_mode_enable_consolidation = self.safe_mode_enable_consolidation.value

        safe_mode_enable_guid_sync: str | Unset = UNSET
        if not isinstance(self.safe_mode_enable_guid_sync, Unset):
            safe_mode_enable_guid_sync = self.safe_mode_enable_guid_sync.value

        safe_mode_enable_job_queueing: str | Unset = UNSET
        if not isinstance(self.safe_mode_enable_job_queueing, Unset):
            safe_mode_enable_job_queueing = self.safe_mode_enable_job_queueing.value

        safe_mode_enable_mail: str | Unset = UNSET
        if not isinstance(self.safe_mode_enable_mail, Unset):
            safe_mode_enable_mail = self.safe_mode_enable_mail.value

        safe_mode_enable_newsletter: str | Unset = UNSET
        if not isinstance(self.safe_mode_enable_newsletter, Unset):
            safe_mode_enable_newsletter = self.safe_mode_enable_newsletter.value

        safe_mode_enable_notification: str | Unset = UNSET
        if not isinstance(self.safe_mode_enable_notification, Unset):
            safe_mode_enable_notification = self.safe_mode_enable_notification.value

        send_data_security_mails = self.send_data_security_mails

        short_name = self.short_name

        show_ai_assistant = self.show_ai_assistant

        show_remember_me = self.show_remember_me

        site_language = self.site_language

        site_licensekey = self.site_licensekey

        site_logo = self.site_logo

        site_mail = self.site_mail

        site_name = self.site_name

        site_offline = self.site_offline

        site_startpage = self.site_startpage

        site_url = self.site_url

        support_user_active_since: str | Unset = UNSET
        if not isinstance(self.support_user_active_since, Unset):
            support_user_active_since = self.support_user_active_since.isoformat()

        test: str | Unset = UNSET
        if not isinstance(self.test, Unset):
            test = self.test.value

        timezone = self.timezone

        version = self.version

        website_order_status = self.website_order_status

        website_sync_user_id = self.website_sync_user_id

        website_testphase_date = self.website_testphase_date

        website_trial_user_id = self.website_trial_user_id

        website_url = self.website_url

        welcome = self.welcome

        welcome_subtext = self.welcome_subtext

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brand": brand,
                "chatServer": chat_server,
                "finderUrl": finder_url,
                "isPostsActive": is_posts_active,
                "verificationStatus": verification_status,
                "webchatLink": webchat_link,
            }
        )
        if field_current_config_file is not UNSET:
            field_dict["_current_config_file"] = field_current_config_file
        if accept_datasecurity is not UNSET:
            field_dict["accept_datasecurity"] = accept_datasecurity
        if access_control_allow_credentials is not UNSET:
            field_dict["access_control_allow_credentials"] = (
                access_control_allow_credentials
            )
        if access_control_allow_origins is not UNSET:
            field_dict["access_control_allow_origins"] = access_control_allow_origins
        if admin_ids is not UNSET:
            field_dict["admin_ids"] = admin_ids
        if admin_mail is not UNSET:
            field_dict["admin_mail"] = admin_mail
        if admin_message is not UNSET:
            field_dict["admin_message"] = admin_message
        if ai_assistant_available is not UNSET:
            field_dict["aiAssistantAvailable"] = ai_assistant_available
        if ai_description_available_generation_count is not UNSET:
            field_dict["ai_description_available_generation_count"] = (
                ai_description_available_generation_count
            )
        if ai_description_available_generation_tests is not UNSET:
            field_dict["ai_description_available_generation_tests"] = (
                ai_description_available_generation_tests
            )
        if ai_description_generation_count is not UNSET:
            field_dict["ai_description_generation_count"] = (
                ai_description_generation_count
            )
        if ai_description_generation_enabled is not UNSET:
            field_dict["ai_description_generation_enabled"] = (
                ai_description_generation_enabled
            )
        if ai_description_total_generation_count is not UNSET:
            field_dict["ai_description_total_generation_count"] = (
                ai_description_total_generation_count
            )
        if allowaiassistant is not UNSET:
            field_dict["allowaiassistant"] = allowaiassistant
        if allowcheckin is not UNSET:
            field_dict["allowcheckin"] = allowcheckin
        if allowedcals is not UNSET:
            field_dict["allowedcals"] = allowedcals
        if allowedclients is not UNSET:
            field_dict["allowedclients"] = allowedclients
        if allowedcwbusers is not UNSET:
            field_dict["allowedcwbusers"] = allowedcwbusers
        if allowedresources is not UNSET:
            field_dict["allowedresources"] = allowedresources
        if allowedservices is not UNSET:
            field_dict["allowedservices"] = allowedservices
        if allowedstations is not UNSET:
            field_dict["allowedstations"] = allowedstations
        if allowedsyncconnections is not UNSET:
            field_dict["allowedsyncconnections"] = allowedsyncconnections
        if allowedsyncjobs is not UNSET:
            field_dict["allowedsyncjobs"] = allowedsyncjobs
        if alloweduser is not UNSET:
            field_dict["alloweduser"] = alloweduser
        if allowfinance is not UNSET:
            field_dict["allowfinance"] = allowfinance
        if allowldap is not UNSET:
            field_dict["allowldap"] = allowldap
        if allowoptigemsync is not UNSET:
            field_dict["allowoptigemsync"] = allowoptigemsync
        if allowsync is not UNSET:
            field_dict["allowsync"] = allowsync
        if alpha_book_affiliate_id is not UNSET:
            field_dict["alpha_book_affiliate_id"] = alpha_book_affiliate_id
        if alpha_book_enabled is not UNSET:
            field_dict["alpha_book_enabled"] = alpha_book_enabled
        if app_security_request is not UNSET:
            field_dict["app_security_request"] = app_security_request
        if authorized_persons is not UNSET:
            field_dict["authorized_persons"] = authorized_persons
        if build is not UNSET:
            field_dict["build"] = build
        if ccli_access_token is not UNSET:
            field_dict["ccli_access_token"] = ccli_access_token
        if ccli_auto_reporting_enabled is not UNSET:
            field_dict["ccli_auto_reporting_enabled"] = ccli_auto_reporting_enabled
        if ccli_last_token_refresh is not UNSET:
            field_dict["ccli_last_token_refresh"] = ccli_last_token_refresh
        if ccli_refresh_token is not UNSET:
            field_dict["ccli_refresh_token"] = ccli_refresh_token
        if chrome_active is not UNSET:
            field_dict["chrome_active"] = chrome_active
        if chrome_binary is not UNSET:
            field_dict["chrome_binary"] = chrome_binary
        if churchcal_active is not UNSET:
            field_dict["churchcal_active"] = churchcal_active
        if churchcal_css is not UNSET:
            field_dict["churchcal_css"] = churchcal_css
        if churchcal_entries_last_days is not UNSET:
            field_dict["churchcal_entries_last_days"] = churchcal_entries_last_days
        if churchcal_firstdayinweek is not UNSET:
            field_dict["churchcal_firstdayinweek"] = churchcal_firstdayinweek
        if churchcal_maincalname is not UNSET:
            field_dict["churchcal_maincalname"] = churchcal_maincalname
        if churchcal_name is not UNSET:
            field_dict["churchcal_name"] = churchcal_name
        if churchcal_name_default is not UNSET:
            field_dict["churchcal_name_default"] = churchcal_name_default
        if churchcal_sortcode is not UNSET:
            field_dict["churchcal_sortcode"] = churchcal_sortcode
        if churchchat_allow_event_chat is not UNSET:
            field_dict["churchchat_allow_event_chat"] = churchchat_allow_event_chat
        if churchchat_allow_group_chat is not UNSET:
            field_dict["churchchat_allow_group_chat"] = churchchat_allow_group_chat
        if churchchat_allow_person_chat is not UNSET:
            field_dict["churchchat_allow_person_chat"] = churchchat_allow_person_chat
        if churchchat_delete_event_chat_after_x_days is not UNSET:
            field_dict["churchchat_delete_event_chat_after_x_days"] = (
                churchchat_delete_event_chat_after_x_days
            )
        if churchchat_invite_ct_event_chat is not UNSET:
            field_dict["churchchat_invite_ct_event_chat"] = (
                churchchat_invite_ct_event_chat
            )
        if churchchat_invite_ct_group_chat is not UNSET:
            field_dict["churchchat_invite_ct_group_chat"] = (
                churchchat_invite_ct_group_chat
            )
        if churchchat_name is not UNSET:
            field_dict["churchchat_name"] = churchchat_name
        if churchchat_name_default is not UNSET:
            field_dict["churchchat_name_default"] = churchchat_name_default
        if churchchat_sortcode is not UNSET:
            field_dict["churchchat_sortcode"] = churchchat_sortcode
        if churchchat_start_event_chat_before_x_days is not UNSET:
            field_dict["churchchat_start_event_chat_before_x_days"] = (
                churchchat_start_event_chat_before_x_days
            )
        if churchchat_start_event_chat_for_calendars is not UNSET:
            field_dict["churchchat_start_event_chat_for_calendars"] = (
                churchchat_start_event_chat_for_calendars
            )
        if churchchat_sync_user_id is not UNSET:
            field_dict["churchchat_sync_user_id"] = churchchat_sync_user_id
        if churchcheckin_active is not UNSET:
            field_dict["churchcheckin_active"] = churchcheckin_active
        if churchcheckin_label_child is not UNSET:
            field_dict["churchcheckin_label_child"] = churchcheckin_label_child
        if churchcheckin_label_parent is not UNSET:
            field_dict["churchcheckin_label_parent"] = churchcheckin_label_parent
        if churchcheckin_label_standard is not UNSET:
            field_dict["churchcheckin_label_standard"] = churchcheckin_label_standard
        if churchcheckin_name is not UNSET:
            field_dict["churchcheckin_name"] = churchcheckin_name
        if churchcheckin_name_default is not UNSET:
            field_dict["churchcheckin_name_default"] = churchcheckin_name_default
        if churchcheckin_sortcode is not UNSET:
            field_dict["churchcheckin_sortcode"] = churchcheckin_sortcode
        if churchcheckin_tags is not UNSET:
            field_dict["churchcheckin_tags"] = churchcheckin_tags
        if churchcustommodule_active is not UNSET:
            field_dict["churchcustommodule_active"] = churchcustommodule_active
        if churchcustommodule_name is not UNSET:
            field_dict["churchcustommodule_name"] = churchcustommodule_name
        if churchcustommodule_name_default is not UNSET:
            field_dict["churchcustommodule_name_default"] = (
                churchcustommodule_name_default
            )
        if churchdb_active is not UNSET:
            field_dict["churchdb_active"] = churchdb_active
        if churchdb_archivedeletehistory is not UNSET:
            field_dict["churchdb_archivedeletehistory"] = churchdb_archivedeletehistory
        if churchdb_birthdaylist_station is not UNSET:
            field_dict["churchdb_birthdaylist_station"] = churchdb_birthdaylist_station
        if churchdb_birthdaylist_status is not UNSET:
            field_dict["churchdb_birthdaylist_status"] = churchdb_birthdaylist_status
        if churchdb_cleverreach_client_id is not UNSET:
            field_dict["churchdb_cleverreach_client_id"] = (
                churchdb_cleverreach_client_id
            )
        if churchdb_cleverreach_client_secret is not UNSET:
            field_dict["churchdb_cleverreach_client_secret"] = (
                churchdb_cleverreach_client_secret
            )
        if churchdb_cleverreach_connected is not UNSET:
            field_dict["churchdb_cleverreach_connected"] = (
                churchdb_cleverreach_connected
            )
        if churchdb_emailseparator is not UNSET:
            field_dict["churchdb_emailseparator"] = churchdb_emailseparator
        if churchdb_groupnotchoosable is not UNSET:
            field_dict["churchdb_groupnotchoosable"] = churchdb_groupnotchoosable
        if churchdb_home_lat is not UNSET:
            field_dict["churchdb_home_lat"] = churchdb_home_lat
        if churchdb_home_lng is not UNSET:
            field_dict["churchdb_home_lng"] = churchdb_home_lng
        if churchdb_mailchimp_apikey is not UNSET:
            field_dict["churchdb_mailchimp_apikey"] = churchdb_mailchimp_apikey
        if churchdb_mailchimp_connected is not UNSET:
            field_dict["churchdb_mailchimp_connected"] = churchdb_mailchimp_connected
        if churchdb_mailjet_apikey is not UNSET:
            field_dict["churchdb_mailjet_apikey"] = churchdb_mailjet_apikey
        if churchdb_mailjet_apisecret is not UNSET:
            field_dict["churchdb_mailjet_apisecret"] = churchdb_mailjet_apisecret
        if churchdb_mailjet_connected is not UNSET:
            field_dict["churchdb_mailjet_connected"] = churchdb_mailjet_connected
        if churchdb_memberlist_station is not UNSET:
            field_dict["churchdb_memberlist_station"] = churchdb_memberlist_station
        if churchdb_memberlist_status is not UNSET:
            field_dict["churchdb_memberlist_status"] = churchdb_memberlist_status
        if churchdb_name is not UNSET:
            field_dict["churchdb_name"] = churchdb_name
        if churchdb_name_default is not UNSET:
            field_dict["churchdb_name_default"] = churchdb_name_default
        if churchdb_sendgroupmails is not UNSET:
            field_dict["churchdb_sendgroupmails"] = churchdb_sendgroupmails
        if churchdb_smscmtelecom_apikey is not UNSET:
            field_dict["churchdb_smscmtelecom_apikey"] = churchdb_smscmtelecom_apikey
        if churchdb_smspromote_apikey is not UNSET:
            field_dict["churchdb_smspromote_apikey"] = churchdb_smspromote_apikey
        if churchdb_sortcode is not UNSET:
            field_dict["churchdb_sortcode"] = churchdb_sortcode
        if churchfinance_active is not UNSET:
            field_dict["churchfinance_active"] = churchfinance_active
        if churchfinance_name is not UNSET:
            field_dict["churchfinance_name"] = churchfinance_name
        if churchfinance_name_default is not UNSET:
            field_dict["churchfinance_name_default"] = churchfinance_name_default
        if churchfinance_sortcode is not UNSET:
            field_dict["churchfinance_sortcode"] = churchfinance_sortcode
        if churchgroup_active is not UNSET:
            field_dict["churchgroup_active"] = churchgroup_active
        if churchgroup_inmenu is not UNSET:
            field_dict["churchgroup_inmenu"] = churchgroup_inmenu
        if churchgroup_name is not UNSET:
            field_dict["churchgroup_name"] = churchgroup_name
        if churchgroup_name_default is not UNSET:
            field_dict["churchgroup_name_default"] = churchgroup_name_default
        if churchgroup_sortcode is not UNSET:
            field_dict["churchgroup_sortcode"] = churchgroup_sortcode
        if churchreport_active is not UNSET:
            field_dict["churchreport_active"] = churchreport_active
        if churchreport_name is not UNSET:
            field_dict["churchreport_name"] = churchreport_name
        if churchreport_name_default is not UNSET:
            field_dict["churchreport_name_default"] = churchreport_name_default
        if churchreport_sortcode is not UNSET:
            field_dict["churchreport_sortcode"] = churchreport_sortcode
        if churchresource_active is not UNSET:
            field_dict["churchresource_active"] = churchresource_active
        if churchresource_anonymize_for_public_user is not UNSET:
            field_dict["churchresource_anonymize_for_public_user"] = (
                churchresource_anonymize_for_public_user
            )
        if churchresource_entries_last_days is not UNSET:
            field_dict["churchresource_entries_last_days"] = (
                churchresource_entries_last_days
            )
        if churchresource_name is not UNSET:
            field_dict["churchresource_name"] = churchresource_name
        if churchresource_name_default is not UNSET:
            field_dict["churchresource_name_default"] = churchresource_name_default
        if churchresource_send_emails is not UNSET:
            field_dict["churchresource_send_emails"] = churchresource_send_emails
        if churchresource_sortcode is not UNSET:
            field_dict["churchresource_sortcode"] = churchresource_sortcode
        if churchservice_active is not UNSET:
            field_dict["churchservice_active"] = churchservice_active
        if churchservice_agendashowenumeration is not UNSET:
            field_dict["churchservice_agendashowenumeration"] = (
                churchservice_agendashowenumeration
            )
        if churchservice_ccli_token is not UNSET:
            field_dict["churchservice_ccli_token"] = churchservice_ccli_token
        if churchservice_ccli_token_secret is not UNSET:
            field_dict["churchservice_ccli_token_secret"] = (
                churchservice_ccli_token_secret
            )
        if churchservice_entries_last_days is not UNSET:
            field_dict["churchservice_entries_last_days"] = (
                churchservice_entries_last_days
            )
        if churchservice_invite_persons is not UNSET:
            field_dict["churchservice_invite_persons"] = churchservice_invite_persons
        if churchservice_name is not UNSET:
            field_dict["churchservice_name"] = churchservice_name
        if churchservice_name_default is not UNSET:
            field_dict["churchservice_name_default"] = churchservice_name_default
        if churchservice_openservice_rememberdays is not UNSET:
            field_dict["churchservice_openservice_rememberdays"] = (
                churchservice_openservice_rememberdays
            )
        if churchservice_reminderhours is not UNSET:
            field_dict["churchservice_reminderhours"] = churchservice_reminderhours
        if churchservice_songwithcategoryasdir is not UNSET:
            field_dict["churchservice_songwithcategoryasdir"] = (
                churchservice_songwithcategoryasdir
            )
        if churchservice_sortcode is not UNSET:
            field_dict["churchservice_sortcode"] = churchservice_sortcode
        if churchsync_active is not UNSET:
            field_dict["churchsync_active"] = churchsync_active
        if churchsync_inmenu is not UNSET:
            field_dict["churchsync_inmenu"] = churchsync_inmenu
        if churchsync_name is not UNSET:
            field_dict["churchsync_name"] = churchsync_name
        if churchsync_name_default is not UNSET:
            field_dict["churchsync_name_default"] = churchsync_name_default
        if churchsync_sortcode is not UNSET:
            field_dict["churchsync_sortcode"] = churchsync_sortcode
        if churchwiki_active is not UNSET:
            field_dict["churchwiki_active"] = churchwiki_active
        if churchwiki_name is not UNSET:
            field_dict["churchwiki_name"] = churchwiki_name
        if churchwiki_name_default is not UNSET:
            field_dict["churchwiki_name_default"] = churchwiki_name_default
        if churchwiki_sortcode is not UNSET:
            field_dict["churchwiki_sortcode"] = churchwiki_sortcode
        if cron_daily is not UNSET:
            field_dict["cron_daily"] = cron_daily
        if cron_hour_8 is not UNSET:
            field_dict["cron_hour_8"] = cron_hour_8
        if cronjob_delay is not UNSET:
            field_dict["cronjob_delay"] = cronjob_delay
        if csrf_enabled is not UNSET:
            field_dict["csrf_enabled"] = csrf_enabled
        if currently_mail_sending is not UNSET:
            field_dict["currently_mail_sending"] = currently_mail_sending
        if datasecurity_privacy_declaration_wiki_link is not UNSET:
            field_dict["datasecurityPrivacyDeclarationWikiLink"] = (
                datasecurity_privacy_declaration_wiki_link
            )
        if datasecurity_banner_enabled is not UNSET:
            field_dict["datasecurity_banner_enabled"] = datasecurity_banner_enabled
        if datasecurity_privacy_agreement_hint is not UNSET:
            field_dict["datasecurity_privacy_agreement_hint"] = (
                datasecurity_privacy_agreement_hint
            )
        if datasecurity_privacy_agreement_text is not UNSET:
            field_dict["datasecurity_privacy_agreement_text"] = (
                datasecurity_privacy_agreement_text
            )
        if datasecurity_privacy_agreement_text_for_children is not UNSET:
            field_dict["datasecurity_privacy_agreement_text_for_children"] = (
                datasecurity_privacy_agreement_text_for_children
            )
        if db_name is not UNSET:
            field_dict["db_name"] = db_name
        if db_password is not UNSET:
            field_dict["db_password"] = db_password
        if db_server is not UNSET:
            field_dict["db_server"] = db_server
        if db_user is not UNSET:
            field_dict["db_user"] = db_user
        if default_phone_area_code is not UNSET:
            field_dict["default_phone_area_code"] = default_phone_area_code
        if email_server is not UNSET:
            field_dict["emailServer"] = email_server
        if encryptionkey is not UNSET:
            field_dict["encryptionkey"] = encryptionkey
        if env is not UNSET:
            field_dict["env"] = env
        if evangelische_termine_api_key is not UNSET:
            field_dict["evangelische_termine_api_key"] = evangelische_termine_api_key
        if evangelische_termine_enabled is not UNSET:
            field_dict["evangelische_termine_enabled"] = evangelische_termine_enabled
        if evangelische_termine_name is not UNSET:
            field_dict["evangelische_termine_name"] = evangelische_termine_name
        if evangelische_termine_url is not UNSET:
            field_dict["evangelische_termine_url"] = evangelische_termine_url
        if evangelische_termine_vid is not UNSET:
            field_dict["evangelische_termine_vid"] = evangelische_termine_vid
        if feature_custommodule is not UNSET:
            field_dict["feature_custommodule"] = feature_custommodule
        if finance_active is not UNSET:
            field_dict["finance_active"] = finance_active
        if finance_inmenu is not UNSET:
            field_dict["finance_inmenu"] = finance_inmenu
        if finance_name is not UNSET:
            field_dict["finance_name"] = finance_name
        if finance_name_default is not UNSET:
            field_dict["finance_name_default"] = finance_name_default
        if finance_sortcode is not UNSET:
            field_dict["finance_sortcode"] = finance_sortcode
        if first_sync_job is not UNSET:
            field_dict["first_sync_job"] = first_sync_job
        if first_transaction is not UNSET:
            field_dict["first_transaction"] = first_transaction
        if hide_beta_states is not UNSET:
            field_dict["hideBetaStates"] = hide_beta_states
        if hide_all_hints is not UNSET:
            field_dict["hide_all_hints"] = hide_all_hints
        if hostingservice is not UNSET:
            field_dict["hostingservice"] = hostingservice
        if https_only is not UNSET:
            field_dict["https_only"] = https_only
        if image_extension is not UNSET:
            field_dict["image_extension"] = image_extension
        if impressum_external is not UNSET:
            field_dict["impressum_external"] = impressum_external
        if impressum_external_link is not UNSET:
            field_dict["impressum_external_link"] = impressum_external_link
        if impressum_internal is not UNSET:
            field_dict["impressum_internal"] = impressum_internal
        if imprint_wiki_link is not UNSET:
            field_dict["imprintWikiLink"] = imprint_wiki_link
        if installation_verification_code is not UNSET:
            field_dict["installation_verification_code"] = (
                installation_verification_code
            )
        if invite_email_text is not UNSET:
            field_dict["invite_email_text"] = invite_email_text
        if is_saml_active is not UNSET:
            field_dict["isSamlActive"] = is_saml_active
        if is_churchtools_blog_widget_active is not UNSET:
            field_dict["is_churchtools_blog_widget_active"] = (
                is_churchtools_blog_widget_active
            )
        if is_churchtools_onboarding_widget_active is not UNSET:
            field_dict["is_churchtools_onboarding_widget_active"] = (
                is_churchtools_onboarding_widget_active
            )
        if is_pr_widget_active is not UNSET:
            field_dict["is_pr_widget_active"] = is_pr_widget_active
        if is_rss_widget_active is not UNSET:
            field_dict["is_rss_widget_active"] = is_rss_widget_active
        if language is not UNSET:
            field_dict["language"] = language
        if last_cron is not UNSET:
            field_dict["last_cron"] = last_cron
        if last_cron_finished is not UNSET:
            field_dict["last_cron_finished"] = last_cron_finished
        if last_import_clear is not UNSET:
            field_dict["last_import_clear"] = last_import_clear
        if last_translation_update is not UNSET:
            field_dict["last_translation_update"] = last_translation_update
        if ldap_otp_enabled is not UNSET:
            field_dict["ldap_otp_enabled"] = ldap_otp_enabled
        if license_settings is not UNSET:
            field_dict["licenseSettings"] = license_settings
        if log_debug is not UNSET:
            field_dict["log_debug"] = log_debug
        if login_message is not UNSET:
            field_dict["login_message"] = login_message
        if mail_enabled is not UNSET:
            field_dict["mail_enabled"] = mail_enabled
        if mail_sending_in_background is not UNSET:
            field_dict["mail_sending_in_background"] = mail_sending_in_background
        if mail_sending_starttime is not UNSET:
            field_dict["mail_sending_starttime"] = mail_sending_starttime
        if mail_smtp_args_host is not UNSET:
            field_dict["mail_smtp_args_host"] = mail_smtp_args_host
        if mail_smtp_args_password is not UNSET:
            field_dict["mail_smtp_args_password"] = mail_smtp_args_password
        if mail_smtp_args_port is not UNSET:
            field_dict["mail_smtp_args_port"] = mail_smtp_args_port
        if mail_smtp_args_smtpsecure is not UNSET:
            field_dict["mail_smtp_args_smtpsecure"] = mail_smtp_args_smtpsecure
        if mail_smtp_args_username is not UNSET:
            field_dict["mail_smtp_args_username"] = mail_smtp_args_username
        if max_uploadfile_size_kb is not UNSET:
            field_dict["max_uploadfile_size_kb"] = max_uploadfile_size_kb
        if memberlist_birthday_full is not UNSET:
            field_dict["memberlist_birthday_full"] = memberlist_birthday_full
        if memberlist_email is not UNSET:
            field_dict["memberlist_email"] = memberlist_email
        if memberlist_fax is not UNSET:
            field_dict["memberlist_fax"] = memberlist_fax
        if memberlist_group_couples is not UNSET:
            field_dict["memberlist_group_couples"] = memberlist_group_couples
        if memberlist_picture is not UNSET:
            field_dict["memberlist_picture"] = memberlist_picture
        if memberlist_salutation is not UNSET:
            field_dict["memberlist_salutation"] = memberlist_salutation
        if memberlist_telefongeschaeftlich is not UNSET:
            field_dict["memberlist_telefongeschaeftlich"] = (
                memberlist_telefongeschaeftlich
            )
        if memberlist_telefonhandy is not UNSET:
            field_dict["memberlist_telefonhandy"] = memberlist_telefonhandy
        if memberlist_telefonprivat is not UNSET:
            field_dict["memberlist_telefonprivat"] = memberlist_telefonprivat
        if onboarding_start is not UNSET:
            field_dict["onboarding_start"] = onboarding_start
        if openstreetmaps_enabled is not UNSET:
            field_dict["openstreetmaps_enabled"] = openstreetmaps_enabled
        if orderstatus is not UNSET:
            field_dict["orderstatus"] = orderstatus
        if orderstatus_since_date is not UNSET:
            field_dict["orderstatus_since_date"] = orderstatus_since_date
        if package is not UNSET:
            field_dict["package"] = package
        if post_active is not UNSET:
            field_dict["post_active"] = post_active
        if post_edit_time_limited is not UNSET:
            field_dict["post_edit_time_limited"] = post_edit_time_limited
        if post_email_summary_default_enabled is not UNSET:
            field_dict["post_email_summary_default_enabled"] = (
                post_email_summary_default_enabled
            )
        if post_featured_groups is not UNSET:
            field_dict["post_featured_groups"] = post_featured_groups
        if post_name is not UNSET:
            field_dict["post_name"] = post_name
        if post_sortcode is not UNSET:
            field_dict["post_sortcode"] = post_sortcode
        if post_wizard_completed is not UNSET:
            field_dict["post_wizard_completed"] = post_wizard_completed
        if post_wizard_groups is not UNSET:
            field_dict["post_wizard_groups"] = post_wizard_groups
        if prevent_change_security_settings is not UNSET:
            field_dict["prevent_change_security_settings"] = (
                prevent_change_security_settings
            )
        if prevent_export is not UNSET:
            field_dict["prevent_export"] = prevent_export
        if prevent_manual_finance_account_creation is not UNSET:
            field_dict["prevent_manual_finance_account_creation"] = (
                prevent_manual_finance_account_creation
            )
        if privacy_policy_external is not UNSET:
            field_dict["privacy_policy_external"] = privacy_policy_external
        if privacy_policy_external_link is not UNSET:
            field_dict["privacy_policy_external_link"] = privacy_policy_external_link
        if privacy_policy_fields_mandatory is not UNSET:
            field_dict["privacy_policy_fields_mandatory"] = (
                privacy_policy_fields_mandatory
            )
        if privacy_policy_fields_mandatory_api is not UNSET:
            field_dict["privacy_policy_fields_mandatory_api"] = (
                privacy_policy_fields_mandatory_api
            )
        if privacy_policy_internal is not UNSET:
            field_dict["privacy_policy_internal"] = privacy_policy_internal
        if privacy_policy_relationships is not UNSET:
            field_dict["privacy_policy_relationships"] = privacy_policy_relationships
        if profile is not UNSET:
            field_dict["profile"] = profile
        if public_channel_registry_url is not UNSET:
            field_dict["public_channel_registry_url"] = public_channel_registry_url
        if rabbitmq_config_host is not UNSET:
            field_dict["rabbitmq_config_host"] = rabbitmq_config_host
        if rabbitmq_config_password is not UNSET:
            field_dict["rabbitmq_config_password"] = rabbitmq_config_password
        if rabbitmq_config_port is not UNSET:
            field_dict["rabbitmq_config_port"] = rabbitmq_config_port
        if rabbitmq_config_user is not UNSET:
            field_dict["rabbitmq_config_user"] = rabbitmq_config_user
        if rss_widget_link is not UNSET:
            field_dict["rss_widget_link"] = rss_widget_link
        if safe_mode_enable_authorized_persons is not UNSET:
            field_dict["safe_mode_enable_authorized_persons"] = (
                safe_mode_enable_authorized_persons
            )
        if safe_mode_enable_chat_sync is not UNSET:
            field_dict["safe_mode_enable_chat_sync"] = safe_mode_enable_chat_sync
        if safe_mode_enable_consolidation is not UNSET:
            field_dict["safe_mode_enable_consolidation"] = (
                safe_mode_enable_consolidation
            )
        if safe_mode_enable_guid_sync is not UNSET:
            field_dict["safe_mode_enable_guid_sync"] = safe_mode_enable_guid_sync
        if safe_mode_enable_job_queueing is not UNSET:
            field_dict["safe_mode_enable_job_queueing"] = safe_mode_enable_job_queueing
        if safe_mode_enable_mail is not UNSET:
            field_dict["safe_mode_enable_mail"] = safe_mode_enable_mail
        if safe_mode_enable_newsletter is not UNSET:
            field_dict["safe_mode_enable_newsletter"] = safe_mode_enable_newsletter
        if safe_mode_enable_notification is not UNSET:
            field_dict["safe_mode_enable_notification"] = safe_mode_enable_notification
        if send_data_security_mails is not UNSET:
            field_dict["send_data_security_mails"] = send_data_security_mails
        if short_name is not UNSET:
            field_dict["short_name"] = short_name
        if show_ai_assistant is not UNSET:
            field_dict["showAIAssistant"] = show_ai_assistant
        if show_remember_me is not UNSET:
            field_dict["show_remember_me"] = show_remember_me
        if site_language is not UNSET:
            field_dict["site_language"] = site_language
        if site_licensekey is not UNSET:
            field_dict["site_licensekey"] = site_licensekey
        if site_logo is not UNSET:
            field_dict["site_logo"] = site_logo
        if site_mail is not UNSET:
            field_dict["site_mail"] = site_mail
        if site_name is not UNSET:
            field_dict["site_name"] = site_name
        if site_offline is not UNSET:
            field_dict["site_offline"] = site_offline
        if site_startpage is not UNSET:
            field_dict["site_startpage"] = site_startpage
        if site_url is not UNSET:
            field_dict["site_url"] = site_url
        if support_user_active_since is not UNSET:
            field_dict["support-user-active-since"] = support_user_active_since
        if test is not UNSET:
            field_dict["test"] = test
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if version is not UNSET:
            field_dict["version"] = version
        if website_order_status is not UNSET:
            field_dict["website_order_status"] = website_order_status
        if website_sync_user_id is not UNSET:
            field_dict["website_sync_user_id"] = website_sync_user_id
        if website_testphase_date is not UNSET:
            field_dict["website_testphase_date"] = website_testphase_date
        if website_trial_user_id is not UNSET:
            field_dict["website_trial_user_id"] = website_trial_user_id
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if welcome is not UNSET:
            field_dict["welcome"] = welcome
        if welcome_subtext is not UNSET:
            field_dict["welcome_subtext"] = welcome_subtext

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_config_response_200_license_settings import (
            PutConfigResponse200LicenseSettings,
        )

        d = dict(src_dict)
        brand = PutConfigResponse200Brand(d.pop("brand"))

        chat_server = d.pop("chatServer")

        finder_url = d.pop("finderUrl")

        is_posts_active = d.pop("isPostsActive")

        verification_status = PutConfigResponse200VerificationStatus(
            d.pop("verificationStatus")
        )

        webchat_link = d.pop("webchatLink")

        field_current_config_file = d.pop("_current_config_file", UNSET)

        accept_datasecurity = d.pop("accept_datasecurity", UNSET)

        access_control_allow_credentials = d.pop(
            "access_control_allow_credentials", UNSET
        )

        access_control_allow_origins = d.pop("access_control_allow_origins", UNSET)

        admin_ids = cast(list[str], d.pop("admin_ids", UNSET))

        admin_mail = d.pop("admin_mail", UNSET)

        admin_message = d.pop("admin_message", UNSET)

        ai_assistant_available = d.pop("aiAssistantAvailable", UNSET)

        ai_description_available_generation_count = d.pop(
            "ai_description_available_generation_count", UNSET
        )

        ai_description_available_generation_tests = d.pop(
            "ai_description_available_generation_tests", UNSET
        )

        ai_description_generation_count = d.pop(
            "ai_description_generation_count", UNSET
        )

        ai_description_generation_enabled = d.pop(
            "ai_description_generation_enabled", UNSET
        )

        ai_description_total_generation_count = d.pop(
            "ai_description_total_generation_count", UNSET
        )

        allowaiassistant = d.pop("allowaiassistant", UNSET)

        _allowcheckin = d.pop("allowcheckin", UNSET)
        allowcheckin: PutConfigResponse200Allowcheckin | Unset
        if isinstance(_allowcheckin, Unset):
            allowcheckin = UNSET
        else:
            allowcheckin = PutConfigResponse200Allowcheckin(_allowcheckin)

        allowedcals = d.pop("allowedcals", UNSET)

        allowedclients = d.pop("allowedclients", UNSET)

        allowedcwbusers = d.pop("allowedcwbusers", UNSET)

        allowedresources = d.pop("allowedresources", UNSET)

        allowedservices = d.pop("allowedservices", UNSET)

        allowedstations = d.pop("allowedstations", UNSET)

        allowedsyncconnections = d.pop("allowedsyncconnections", UNSET)

        allowedsyncjobs = d.pop("allowedsyncjobs", UNSET)

        alloweduser = d.pop("alloweduser", UNSET)

        _allowfinance = d.pop("allowfinance", UNSET)
        allowfinance: PutConfigResponse200Allowfinance | Unset
        if isinstance(_allowfinance, Unset):
            allowfinance = UNSET
        else:
            allowfinance = PutConfigResponse200Allowfinance(_allowfinance)

        _allowldap = d.pop("allowldap", UNSET)
        allowldap: PutConfigResponse200Allowldap | Unset
        if isinstance(_allowldap, Unset):
            allowldap = UNSET
        else:
            allowldap = PutConfigResponse200Allowldap(_allowldap)

        _allowoptigemsync = d.pop("allowoptigemsync", UNSET)
        allowoptigemsync: PutConfigResponse200Allowoptigemsync | Unset
        if isinstance(_allowoptigemsync, Unset):
            allowoptigemsync = UNSET
        else:
            allowoptigemsync = PutConfigResponse200Allowoptigemsync(_allowoptigemsync)

        _allowsync = d.pop("allowsync", UNSET)
        allowsync: PutConfigResponse200Allowsync | Unset
        if isinstance(_allowsync, Unset):
            allowsync = UNSET
        else:
            allowsync = PutConfigResponse200Allowsync(_allowsync)

        alpha_book_affiliate_id = d.pop("alpha_book_affiliate_id", UNSET)

        alpha_book_enabled = d.pop("alpha_book_enabled", UNSET)

        app_security_request = d.pop("app_security_request", UNSET)

        authorized_persons = d.pop("authorized_persons", UNSET)

        build = d.pop("build", UNSET)

        ccli_access_token = d.pop("ccli_access_token", UNSET)

        ccli_auto_reporting_enabled = d.pop("ccli_auto_reporting_enabled", UNSET)

        ccli_last_token_refresh = d.pop("ccli_last_token_refresh", UNSET)

        ccli_refresh_token = d.pop("ccli_refresh_token", UNSET)

        _chrome_active = d.pop("chrome_active", UNSET)
        chrome_active: PutConfigResponse200ChromeActive | Unset
        if isinstance(_chrome_active, Unset):
            chrome_active = UNSET
        else:
            chrome_active = PutConfigResponse200ChromeActive(_chrome_active)

        chrome_binary = d.pop("chrome_binary", UNSET)

        churchcal_active = d.pop("churchcal_active", UNSET)

        churchcal_css = d.pop("churchcal_css", UNSET)

        churchcal_entries_last_days = d.pop("churchcal_entries_last_days", UNSET)

        churchcal_firstdayinweek = d.pop("churchcal_firstdayinweek", UNSET)

        churchcal_maincalname = d.pop("churchcal_maincalname", UNSET)

        churchcal_name = d.pop("churchcal_name", UNSET)

        churchcal_name_default = d.pop("churchcal_name_default", UNSET)

        churchcal_sortcode = d.pop("churchcal_sortcode", UNSET)

        churchchat_allow_event_chat = d.pop("churchchat_allow_event_chat", UNSET)

        churchchat_allow_group_chat = d.pop("churchchat_allow_group_chat", UNSET)

        churchchat_allow_person_chat = d.pop("churchchat_allow_person_chat", UNSET)

        churchchat_delete_event_chat_after_x_days = d.pop(
            "churchchat_delete_event_chat_after_x_days", UNSET
        )

        churchchat_invite_ct_event_chat = d.pop(
            "churchchat_invite_ct_event_chat", UNSET
        )

        churchchat_invite_ct_group_chat = d.pop(
            "churchchat_invite_ct_group_chat", UNSET
        )

        churchchat_name = d.pop("churchchat_name", UNSET)

        churchchat_name_default = d.pop("churchchat_name_default", UNSET)

        churchchat_sortcode = d.pop("churchchat_sortcode", UNSET)

        churchchat_start_event_chat_before_x_days = d.pop(
            "churchchat_start_event_chat_before_x_days", UNSET
        )

        churchchat_start_event_chat_for_calendars = d.pop(
            "churchchat_start_event_chat_for_calendars", UNSET
        )

        churchchat_sync_user_id = d.pop("churchchat_sync_user_id", UNSET)

        churchcheckin_active = d.pop("churchcheckin_active", UNSET)

        churchcheckin_label_child = d.pop("churchcheckin_label_child", UNSET)

        churchcheckin_label_parent = d.pop("churchcheckin_label_parent", UNSET)

        churchcheckin_label_standard = d.pop("churchcheckin_label_standard", UNSET)

        churchcheckin_name = d.pop("churchcheckin_name", UNSET)

        churchcheckin_name_default = d.pop("churchcheckin_name_default", UNSET)

        churchcheckin_sortcode = d.pop("churchcheckin_sortcode", UNSET)

        churchcheckin_tags = d.pop("churchcheckin_tags", UNSET)

        _churchcustommodule_active = d.pop("churchcustommodule_active", UNSET)
        churchcustommodule_active: PutConfigResponse200ChurchcustommoduleActive | Unset
        if isinstance(_churchcustommodule_active, Unset):
            churchcustommodule_active = UNSET
        else:
            churchcustommodule_active = PutConfigResponse200ChurchcustommoduleActive(
                _churchcustommodule_active
            )

        churchcustommodule_name = d.pop("churchcustommodule_name", UNSET)

        churchcustommodule_name_default = d.pop(
            "churchcustommodule_name_default", UNSET
        )

        churchdb_active = d.pop("churchdb_active", UNSET)

        churchdb_archivedeletehistory = d.pop("churchdb_archivedeletehistory", UNSET)

        churchdb_birthdaylist_station = d.pop("churchdb_birthdaylist_station", UNSET)

        churchdb_birthdaylist_status = d.pop("churchdb_birthdaylist_status", UNSET)

        churchdb_cleverreach_client_id = d.pop("churchdb_cleverreach_client_id", UNSET)

        churchdb_cleverreach_client_secret = d.pop(
            "churchdb_cleverreach_client_secret", UNSET
        )

        churchdb_cleverreach_connected = d.pop("churchdb_cleverreach_connected", UNSET)

        churchdb_emailseparator = d.pop("churchdb_emailseparator", UNSET)

        churchdb_groupnotchoosable = d.pop("churchdb_groupnotchoosable", UNSET)

        churchdb_home_lat = d.pop("churchdb_home_lat", UNSET)

        churchdb_home_lng = d.pop("churchdb_home_lng", UNSET)

        churchdb_mailchimp_apikey = d.pop("churchdb_mailchimp_apikey", UNSET)

        churchdb_mailchimp_connected = d.pop("churchdb_mailchimp_connected", UNSET)

        churchdb_mailjet_apikey = d.pop("churchdb_mailjet_apikey", UNSET)

        churchdb_mailjet_apisecret = d.pop("churchdb_mailjet_apisecret", UNSET)

        churchdb_mailjet_connected = d.pop("churchdb_mailjet_connected", UNSET)

        churchdb_memberlist_station = d.pop("churchdb_memberlist_station", UNSET)

        churchdb_memberlist_status = d.pop("churchdb_memberlist_status", UNSET)

        churchdb_name = d.pop("churchdb_name", UNSET)

        churchdb_name_default = d.pop("churchdb_name_default", UNSET)

        churchdb_sendgroupmails = d.pop("churchdb_sendgroupmails", UNSET)

        churchdb_smscmtelecom_apikey = d.pop("churchdb_smscmtelecom_apikey", UNSET)

        churchdb_smspromote_apikey = d.pop("churchdb_smspromote_apikey", UNSET)

        churchdb_sortcode = d.pop("churchdb_sortcode", UNSET)

        churchfinance_active = d.pop("churchfinance_active", UNSET)

        churchfinance_name = d.pop("churchfinance_name", UNSET)

        churchfinance_name_default = d.pop("churchfinance_name_default", UNSET)

        churchfinance_sortcode = d.pop("churchfinance_sortcode", UNSET)

        churchgroup_active = d.pop("churchgroup_active", UNSET)

        churchgroup_inmenu = d.pop("churchgroup_inmenu", UNSET)

        churchgroup_name = d.pop("churchgroup_name", UNSET)

        churchgroup_name_default = d.pop("churchgroup_name_default", UNSET)

        churchgroup_sortcode = d.pop("churchgroup_sortcode", UNSET)

        churchreport_active = d.pop("churchreport_active", UNSET)

        churchreport_name = d.pop("churchreport_name", UNSET)

        churchreport_name_default = d.pop("churchreport_name_default", UNSET)

        churchreport_sortcode = d.pop("churchreport_sortcode", UNSET)

        churchresource_active = d.pop("churchresource_active", UNSET)

        churchresource_anonymize_for_public_user = d.pop(
            "churchresource_anonymize_for_public_user", UNSET
        )

        churchresource_entries_last_days = d.pop(
            "churchresource_entries_last_days", UNSET
        )

        churchresource_name = d.pop("churchresource_name", UNSET)

        churchresource_name_default = d.pop("churchresource_name_default", UNSET)

        churchresource_send_emails = d.pop("churchresource_send_emails", UNSET)

        churchresource_sortcode = d.pop("churchresource_sortcode", UNSET)

        churchservice_active = d.pop("churchservice_active", UNSET)

        churchservice_agendashowenumeration = d.pop(
            "churchservice_agendashowenumeration", UNSET
        )

        churchservice_ccli_token = d.pop("churchservice_ccli_token", UNSET)

        churchservice_ccli_token_secret = d.pop(
            "churchservice_ccli_token_secret", UNSET
        )

        churchservice_entries_last_days = d.pop(
            "churchservice_entries_last_days", UNSET
        )

        churchservice_invite_persons = d.pop("churchservice_invite_persons", UNSET)

        churchservice_name = d.pop("churchservice_name", UNSET)

        churchservice_name_default = d.pop("churchservice_name_default", UNSET)

        churchservice_openservice_rememberdays = d.pop(
            "churchservice_openservice_rememberdays", UNSET
        )

        churchservice_reminderhours = d.pop("churchservice_reminderhours", UNSET)

        churchservice_songwithcategoryasdir = d.pop(
            "churchservice_songwithcategoryasdir", UNSET
        )

        churchservice_sortcode = d.pop("churchservice_sortcode", UNSET)

        churchsync_active = d.pop("churchsync_active", UNSET)

        churchsync_inmenu = d.pop("churchsync_inmenu", UNSET)

        churchsync_name = d.pop("churchsync_name", UNSET)

        churchsync_name_default = d.pop("churchsync_name_default", UNSET)

        churchsync_sortcode = d.pop("churchsync_sortcode", UNSET)

        churchwiki_active = d.pop("churchwiki_active", UNSET)

        churchwiki_name = d.pop("churchwiki_name", UNSET)

        churchwiki_name_default = d.pop("churchwiki_name_default", UNSET)

        churchwiki_sortcode = d.pop("churchwiki_sortcode", UNSET)

        _cron_daily = d.pop("cron_daily", UNSET)
        cron_daily: datetime.datetime | Unset
        if isinstance(_cron_daily, Unset):
            cron_daily = UNSET
        else:
            cron_daily = isoparse(_cron_daily)

        _cron_hour_8 = d.pop("cron_hour_8", UNSET)
        cron_hour_8: datetime.datetime | Unset
        if isinstance(_cron_hour_8, Unset):
            cron_hour_8 = UNSET
        else:
            cron_hour_8 = isoparse(_cron_hour_8)

        cronjob_delay = d.pop("cronjob_delay", UNSET)

        csrf_enabled = d.pop("csrf_enabled", UNSET)

        _currently_mail_sending = d.pop("currently_mail_sending", UNSET)
        currently_mail_sending: PutConfigResponse200CurrentlyMailSending | Unset
        if isinstance(_currently_mail_sending, Unset):
            currently_mail_sending = UNSET
        else:
            currently_mail_sending = PutConfigResponse200CurrentlyMailSending(
                _currently_mail_sending
            )

        datasecurity_privacy_declaration_wiki_link = d.pop(
            "datasecurityPrivacyDeclarationWikiLink", UNSET
        )

        datasecurity_banner_enabled = d.pop("datasecurity_banner_enabled", UNSET)

        datasecurity_privacy_agreement_hint = d.pop(
            "datasecurity_privacy_agreement_hint", UNSET
        )

        datasecurity_privacy_agreement_text = d.pop(
            "datasecurity_privacy_agreement_text", UNSET
        )

        datasecurity_privacy_agreement_text_for_children = d.pop(
            "datasecurity_privacy_agreement_text_for_children", UNSET
        )

        db_name = d.pop("db_name", UNSET)

        db_password = d.pop("db_password", UNSET)

        db_server = d.pop("db_server", UNSET)

        db_user = d.pop("db_user", UNSET)

        default_phone_area_code = d.pop("default_phone_area_code", UNSET)

        _email_server = d.pop("emailServer", UNSET)
        email_server: PutConfigResponse200EmailServer | Unset
        if isinstance(_email_server, Unset):
            email_server = UNSET
        else:
            email_server = PutConfigResponse200EmailServer(_email_server)

        encryptionkey = d.pop("encryptionkey", UNSET)

        env = d.pop("env", UNSET)

        evangelische_termine_api_key = d.pop("evangelische_termine_api_key", UNSET)

        evangelische_termine_enabled = d.pop("evangelische_termine_enabled", UNSET)

        evangelische_termine_name = d.pop("evangelische_termine_name", UNSET)

        evangelische_termine_url = d.pop("evangelische_termine_url", UNSET)

        evangelische_termine_vid = d.pop("evangelische_termine_vid", UNSET)

        _feature_custommodule = d.pop("feature_custommodule", UNSET)
        feature_custommodule: PutConfigResponse200FeatureCustommodule | Unset
        if isinstance(_feature_custommodule, Unset):
            feature_custommodule = UNSET
        else:
            feature_custommodule = PutConfigResponse200FeatureCustommodule(
                _feature_custommodule
            )

        finance_active = d.pop("finance_active", UNSET)

        _finance_inmenu = d.pop("finance_inmenu", UNSET)
        finance_inmenu: PutConfigResponse200FinanceInmenu | Unset
        if isinstance(_finance_inmenu, Unset):
            finance_inmenu = UNSET
        else:
            finance_inmenu = PutConfigResponse200FinanceInmenu(_finance_inmenu)

        finance_name = d.pop("finance_name", UNSET)

        finance_name_default = d.pop("finance_name_default", UNSET)

        finance_sortcode = d.pop("finance_sortcode", UNSET)

        _first_sync_job = d.pop("first_sync_job", UNSET)
        first_sync_job: datetime.datetime | Unset
        if isinstance(_first_sync_job, Unset):
            first_sync_job = UNSET
        else:
            first_sync_job = isoparse(_first_sync_job)

        _first_transaction = d.pop("first_transaction", UNSET)
        first_transaction: datetime.datetime | Unset
        if isinstance(_first_transaction, Unset):
            first_transaction = UNSET
        else:
            first_transaction = isoparse(_first_transaction)

        hide_beta_states = d.pop("hideBetaStates", UNSET)

        hide_all_hints = d.pop("hide_all_hints", UNSET)

        _hostingservice = d.pop("hostingservice", UNSET)
        hostingservice: PutConfigResponse200Hostingservice | Unset
        if isinstance(_hostingservice, Unset):
            hostingservice = UNSET
        else:
            hostingservice = PutConfigResponse200Hostingservice(_hostingservice)

        _https_only = d.pop("https_only", UNSET)
        https_only: PutConfigResponse200HttpsOnly | Unset
        if isinstance(_https_only, Unset):
            https_only = UNSET
        else:
            https_only = PutConfigResponse200HttpsOnly(_https_only)

        image_extension = d.pop("image_extension", UNSET)

        impressum_external = d.pop("impressum_external", UNSET)

        impressum_external_link = d.pop("impressum_external_link", UNSET)

        impressum_internal = d.pop("impressum_internal", UNSET)

        imprint_wiki_link = d.pop("imprintWikiLink", UNSET)

        installation_verification_code = d.pop("installation_verification_code", UNSET)

        invite_email_text = d.pop("invite_email_text", UNSET)

        is_saml_active = d.pop("isSamlActive", UNSET)

        is_churchtools_blog_widget_active = d.pop(
            "is_churchtools_blog_widget_active", UNSET
        )

        is_churchtools_onboarding_widget_active = d.pop(
            "is_churchtools_onboarding_widget_active", UNSET
        )

        is_pr_widget_active = d.pop("is_pr_widget_active", UNSET)

        is_rss_widget_active = d.pop("is_rss_widget_active", UNSET)

        _language = d.pop("language", UNSET)
        language: PutConfigResponse200Language | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = PutConfigResponse200Language(_language)

        last_cron = d.pop("last_cron", UNSET)

        last_cron_finished = d.pop("last_cron_finished", UNSET)

        last_import_clear = d.pop("last_import_clear", UNSET)

        last_translation_update = d.pop("last_translation_update", UNSET)

        ldap_otp_enabled = d.pop("ldap_otp_enabled", UNSET)

        _license_settings = d.pop("licenseSettings", UNSET)
        license_settings: PutConfigResponse200LicenseSettings | Unset
        if isinstance(_license_settings, Unset):
            license_settings = UNSET
        else:
            license_settings = PutConfigResponse200LicenseSettings.from_dict(
                _license_settings
            )

        _log_debug = d.pop("log_debug", UNSET)
        log_debug: PutConfigResponse200LogDebug | Unset
        if isinstance(_log_debug, Unset):
            log_debug = UNSET
        else:
            log_debug = PutConfigResponse200LogDebug(_log_debug)

        login_message = d.pop("login_message", UNSET)

        mail_enabled = d.pop("mail_enabled", UNSET)

        _mail_sending_in_background = d.pop("mail_sending_in_background", UNSET)
        mail_sending_in_background: PutConfigResponse200MailSendingInBackground | Unset
        if isinstance(_mail_sending_in_background, Unset):
            mail_sending_in_background = UNSET
        else:
            mail_sending_in_background = PutConfigResponse200MailSendingInBackground(
                _mail_sending_in_background
            )

        mail_sending_starttime = d.pop("mail_sending_starttime", UNSET)

        mail_smtp_args_host = d.pop("mail_smtp_args_host", UNSET)

        mail_smtp_args_password = d.pop("mail_smtp_args_password", UNSET)

        mail_smtp_args_port = d.pop("mail_smtp_args_port", UNSET)

        mail_smtp_args_smtpsecure = d.pop("mail_smtp_args_smtpsecure", UNSET)

        mail_smtp_args_username = d.pop("mail_smtp_args_username", UNSET)

        max_uploadfile_size_kb = d.pop("max_uploadfile_size_kb", UNSET)

        _memberlist_birthday_full = d.pop("memberlist_birthday_full", UNSET)
        memberlist_birthday_full: PutConfigResponse200MemberlistBirthdayFull | Unset
        if isinstance(_memberlist_birthday_full, Unset):
            memberlist_birthday_full = UNSET
        else:
            memberlist_birthday_full = PutConfigResponse200MemberlistBirthdayFull(
                _memberlist_birthday_full
            )

        _memberlist_email = d.pop("memberlist_email", UNSET)
        memberlist_email: PutConfigResponse200MemberlistEmail | Unset
        if isinstance(_memberlist_email, Unset):
            memberlist_email = UNSET
        else:
            memberlist_email = PutConfigResponse200MemberlistEmail(_memberlist_email)

        _memberlist_fax = d.pop("memberlist_fax", UNSET)
        memberlist_fax: PutConfigResponse200MemberlistFax | Unset
        if isinstance(_memberlist_fax, Unset):
            memberlist_fax = UNSET
        else:
            memberlist_fax = PutConfigResponse200MemberlistFax(_memberlist_fax)

        _memberlist_group_couples = d.pop("memberlist_group_couples", UNSET)
        memberlist_group_couples: PutConfigResponse200MemberlistGroupCouples | Unset
        if isinstance(_memberlist_group_couples, Unset):
            memberlist_group_couples = UNSET
        else:
            memberlist_group_couples = PutConfigResponse200MemberlistGroupCouples(
                _memberlist_group_couples
            )

        _memberlist_picture = d.pop("memberlist_picture", UNSET)
        memberlist_picture: PutConfigResponse200MemberlistPicture | Unset
        if isinstance(_memberlist_picture, Unset):
            memberlist_picture = UNSET
        else:
            memberlist_picture = PutConfigResponse200MemberlistPicture(
                _memberlist_picture
            )

        _memberlist_salutation = d.pop("memberlist_salutation", UNSET)
        memberlist_salutation: PutConfigResponse200MemberlistSalutation | Unset
        if isinstance(_memberlist_salutation, Unset):
            memberlist_salutation = UNSET
        else:
            memberlist_salutation = PutConfigResponse200MemberlistSalutation(
                _memberlist_salutation
            )

        _memberlist_telefongeschaeftlich = d.pop(
            "memberlist_telefongeschaeftlich", UNSET
        )
        memberlist_telefongeschaeftlich: (
            PutConfigResponse200MemberlistTelefongeschaeftlich | Unset
        )
        if isinstance(_memberlist_telefongeschaeftlich, Unset):
            memberlist_telefongeschaeftlich = UNSET
        else:
            memberlist_telefongeschaeftlich = (
                PutConfigResponse200MemberlistTelefongeschaeftlich(
                    _memberlist_telefongeschaeftlich
                )
            )

        _memberlist_telefonhandy = d.pop("memberlist_telefonhandy", UNSET)
        memberlist_telefonhandy: PutConfigResponse200MemberlistTelefonhandy | Unset
        if isinstance(_memberlist_telefonhandy, Unset):
            memberlist_telefonhandy = UNSET
        else:
            memberlist_telefonhandy = PutConfigResponse200MemberlistTelefonhandy(
                _memberlist_telefonhandy
            )

        _memberlist_telefonprivat = d.pop("memberlist_telefonprivat", UNSET)
        memberlist_telefonprivat: PutConfigResponse200MemberlistTelefonprivat | Unset
        if isinstance(_memberlist_telefonprivat, Unset):
            memberlist_telefonprivat = UNSET
        else:
            memberlist_telefonprivat = PutConfigResponse200MemberlistTelefonprivat(
                _memberlist_telefonprivat
            )

        _onboarding_start = d.pop("onboarding_start", UNSET)
        onboarding_start: datetime.datetime | Unset
        if isinstance(_onboarding_start, Unset):
            onboarding_start = UNSET
        else:
            onboarding_start = isoparse(_onboarding_start)

        openstreetmaps_enabled = d.pop("openstreetmaps_enabled", UNSET)

        _orderstatus = d.pop("orderstatus", UNSET)
        orderstatus: PutConfigResponse200Orderstatus | Unset
        if isinstance(_orderstatus, Unset):
            orderstatus = UNSET
        else:
            orderstatus = PutConfigResponse200Orderstatus(_orderstatus)

        _orderstatus_since_date = d.pop("orderstatus_since_date", UNSET)
        orderstatus_since_date: datetime.datetime | Unset
        if isinstance(_orderstatus_since_date, Unset):
            orderstatus_since_date = UNSET
        else:
            orderstatus_since_date = isoparse(_orderstatus_since_date)

        package = d.pop("package", UNSET)

        post_active = d.pop("post_active", UNSET)

        post_edit_time_limited = d.pop("post_edit_time_limited", UNSET)

        post_email_summary_default_enabled = d.pop(
            "post_email_summary_default_enabled", UNSET
        )

        post_featured_groups = d.pop("post_featured_groups", UNSET)

        post_name = d.pop("post_name", UNSET)

        post_sortcode = d.pop("post_sortcode", UNSET)

        post_wizard_completed = d.pop("post_wizard_completed", UNSET)

        post_wizard_groups = d.pop("post_wizard_groups", UNSET)

        _prevent_change_security_settings = d.pop(
            "prevent_change_security_settings", UNSET
        )
        prevent_change_security_settings: (
            PutConfigResponse200PreventChangeSecuritySettings | Unset
        )
        if isinstance(_prevent_change_security_settings, Unset):
            prevent_change_security_settings = UNSET
        else:
            prevent_change_security_settings = (
                PutConfigResponse200PreventChangeSecuritySettings(
                    _prevent_change_security_settings
                )
            )

        prevent_export = d.pop("prevent_export", UNSET)

        prevent_manual_finance_account_creation = d.pop(
            "prevent_manual_finance_account_creation", UNSET
        )

        privacy_policy_external = d.pop("privacy_policy_external", UNSET)

        privacy_policy_external_link = d.pop("privacy_policy_external_link", UNSET)

        privacy_policy_fields_mandatory = d.pop(
            "privacy_policy_fields_mandatory", UNSET
        )

        privacy_policy_fields_mandatory_api = d.pop(
            "privacy_policy_fields_mandatory_api", UNSET
        )

        privacy_policy_internal = d.pop("privacy_policy_internal", UNSET)

        privacy_policy_relationships = d.pop("privacy_policy_relationships", UNSET)

        profile = d.pop("profile", UNSET)

        public_channel_registry_url = d.pop("public_channel_registry_url", UNSET)

        rabbitmq_config_host = d.pop("rabbitmq_config_host", UNSET)

        rabbitmq_config_password = d.pop("rabbitmq_config_password", UNSET)

        rabbitmq_config_port = d.pop("rabbitmq_config_port", UNSET)

        rabbitmq_config_user = d.pop("rabbitmq_config_user", UNSET)

        rss_widget_link = d.pop("rss_widget_link", UNSET)

        _safe_mode_enable_authorized_persons = d.pop(
            "safe_mode_enable_authorized_persons", UNSET
        )
        safe_mode_enable_authorized_persons: (
            PutConfigResponse200SafeModeEnableAuthorizedPersons | Unset
        )
        if isinstance(_safe_mode_enable_authorized_persons, Unset):
            safe_mode_enable_authorized_persons = UNSET
        else:
            safe_mode_enable_authorized_persons = (
                PutConfigResponse200SafeModeEnableAuthorizedPersons(
                    _safe_mode_enable_authorized_persons
                )
            )

        _safe_mode_enable_chat_sync = d.pop("safe_mode_enable_chat_sync", UNSET)
        safe_mode_enable_chat_sync: PutConfigResponse200SafeModeEnableChatSync | Unset
        if isinstance(_safe_mode_enable_chat_sync, Unset):
            safe_mode_enable_chat_sync = UNSET
        else:
            safe_mode_enable_chat_sync = PutConfigResponse200SafeModeEnableChatSync(
                _safe_mode_enable_chat_sync
            )

        _safe_mode_enable_consolidation = d.pop("safe_mode_enable_consolidation", UNSET)
        safe_mode_enable_consolidation: (
            PutConfigResponse200SafeModeEnableConsolidation | Unset
        )
        if isinstance(_safe_mode_enable_consolidation, Unset):
            safe_mode_enable_consolidation = UNSET
        else:
            safe_mode_enable_consolidation = (
                PutConfigResponse200SafeModeEnableConsolidation(
                    _safe_mode_enable_consolidation
                )
            )

        _safe_mode_enable_guid_sync = d.pop("safe_mode_enable_guid_sync", UNSET)
        safe_mode_enable_guid_sync: PutConfigResponse200SafeModeEnableGuidSync | Unset
        if isinstance(_safe_mode_enable_guid_sync, Unset):
            safe_mode_enable_guid_sync = UNSET
        else:
            safe_mode_enable_guid_sync = PutConfigResponse200SafeModeEnableGuidSync(
                _safe_mode_enable_guid_sync
            )

        _safe_mode_enable_job_queueing = d.pop("safe_mode_enable_job_queueing", UNSET)
        safe_mode_enable_job_queueing: (
            PutConfigResponse200SafeModeEnableJobQueueing | Unset
        )
        if isinstance(_safe_mode_enable_job_queueing, Unset):
            safe_mode_enable_job_queueing = UNSET
        else:
            safe_mode_enable_job_queueing = (
                PutConfigResponse200SafeModeEnableJobQueueing(
                    _safe_mode_enable_job_queueing
                )
            )

        _safe_mode_enable_mail = d.pop("safe_mode_enable_mail", UNSET)
        safe_mode_enable_mail: PutConfigResponse200SafeModeEnableMail | Unset
        if isinstance(_safe_mode_enable_mail, Unset):
            safe_mode_enable_mail = UNSET
        else:
            safe_mode_enable_mail = PutConfigResponse200SafeModeEnableMail(
                _safe_mode_enable_mail
            )

        _safe_mode_enable_newsletter = d.pop("safe_mode_enable_newsletter", UNSET)
        safe_mode_enable_newsletter: (
            PutConfigResponse200SafeModeEnableNewsletter | Unset
        )
        if isinstance(_safe_mode_enable_newsletter, Unset):
            safe_mode_enable_newsletter = UNSET
        else:
            safe_mode_enable_newsletter = PutConfigResponse200SafeModeEnableNewsletter(
                _safe_mode_enable_newsletter
            )

        _safe_mode_enable_notification = d.pop("safe_mode_enable_notification", UNSET)
        safe_mode_enable_notification: (
            PutConfigResponse200SafeModeEnableNotification | Unset
        )
        if isinstance(_safe_mode_enable_notification, Unset):
            safe_mode_enable_notification = UNSET
        else:
            safe_mode_enable_notification = (
                PutConfigResponse200SafeModeEnableNotification(
                    _safe_mode_enable_notification
                )
            )

        send_data_security_mails = d.pop("send_data_security_mails", UNSET)

        short_name = d.pop("short_name", UNSET)

        show_ai_assistant = d.pop("showAIAssistant", UNSET)

        show_remember_me = d.pop("show_remember_me", UNSET)

        site_language = d.pop("site_language", UNSET)

        site_licensekey = d.pop("site_licensekey", UNSET)

        site_logo = d.pop("site_logo", UNSET)

        site_mail = d.pop("site_mail", UNSET)

        site_name = d.pop("site_name", UNSET)

        site_offline = d.pop("site_offline", UNSET)

        site_startpage = d.pop("site_startpage", UNSET)

        site_url = d.pop("site_url", UNSET)

        _support_user_active_since = d.pop("support-user-active-since", UNSET)
        support_user_active_since: datetime.datetime | Unset
        if isinstance(_support_user_active_since, Unset):
            support_user_active_since = UNSET
        else:
            support_user_active_since = isoparse(_support_user_active_since)

        _test = d.pop("test", UNSET)
        test: PutConfigResponse200Test | Unset
        if isinstance(_test, Unset):
            test = UNSET
        else:
            test = PutConfigResponse200Test(_test)

        timezone = d.pop("timezone", UNSET)

        version = d.pop("version", UNSET)

        website_order_status = d.pop("website_order_status", UNSET)

        website_sync_user_id = d.pop("website_sync_user_id", UNSET)

        website_testphase_date = d.pop("website_testphase_date", UNSET)

        website_trial_user_id = d.pop("website_trial_user_id", UNSET)

        website_url = d.pop("website_url", UNSET)

        welcome = d.pop("welcome", UNSET)

        welcome_subtext = d.pop("welcome_subtext", UNSET)

        put_config_response_200 = cls(
            brand=brand,
            chat_server=chat_server,
            finder_url=finder_url,
            is_posts_active=is_posts_active,
            verification_status=verification_status,
            webchat_link=webchat_link,
            field_current_config_file=field_current_config_file,
            accept_datasecurity=accept_datasecurity,
            access_control_allow_credentials=access_control_allow_credentials,
            access_control_allow_origins=access_control_allow_origins,
            admin_ids=admin_ids,
            admin_mail=admin_mail,
            admin_message=admin_message,
            ai_assistant_available=ai_assistant_available,
            ai_description_available_generation_count=ai_description_available_generation_count,
            ai_description_available_generation_tests=ai_description_available_generation_tests,
            ai_description_generation_count=ai_description_generation_count,
            ai_description_generation_enabled=ai_description_generation_enabled,
            ai_description_total_generation_count=ai_description_total_generation_count,
            allowaiassistant=allowaiassistant,
            allowcheckin=allowcheckin,
            allowedcals=allowedcals,
            allowedclients=allowedclients,
            allowedcwbusers=allowedcwbusers,
            allowedresources=allowedresources,
            allowedservices=allowedservices,
            allowedstations=allowedstations,
            allowedsyncconnections=allowedsyncconnections,
            allowedsyncjobs=allowedsyncjobs,
            alloweduser=alloweduser,
            allowfinance=allowfinance,
            allowldap=allowldap,
            allowoptigemsync=allowoptigemsync,
            allowsync=allowsync,
            alpha_book_affiliate_id=alpha_book_affiliate_id,
            alpha_book_enabled=alpha_book_enabled,
            app_security_request=app_security_request,
            authorized_persons=authorized_persons,
            build=build,
            ccli_access_token=ccli_access_token,
            ccli_auto_reporting_enabled=ccli_auto_reporting_enabled,
            ccli_last_token_refresh=ccli_last_token_refresh,
            ccli_refresh_token=ccli_refresh_token,
            chrome_active=chrome_active,
            chrome_binary=chrome_binary,
            churchcal_active=churchcal_active,
            churchcal_css=churchcal_css,
            churchcal_entries_last_days=churchcal_entries_last_days,
            churchcal_firstdayinweek=churchcal_firstdayinweek,
            churchcal_maincalname=churchcal_maincalname,
            churchcal_name=churchcal_name,
            churchcal_name_default=churchcal_name_default,
            churchcal_sortcode=churchcal_sortcode,
            churchchat_allow_event_chat=churchchat_allow_event_chat,
            churchchat_allow_group_chat=churchchat_allow_group_chat,
            churchchat_allow_person_chat=churchchat_allow_person_chat,
            churchchat_delete_event_chat_after_x_days=churchchat_delete_event_chat_after_x_days,
            churchchat_invite_ct_event_chat=churchchat_invite_ct_event_chat,
            churchchat_invite_ct_group_chat=churchchat_invite_ct_group_chat,
            churchchat_name=churchchat_name,
            churchchat_name_default=churchchat_name_default,
            churchchat_sortcode=churchchat_sortcode,
            churchchat_start_event_chat_before_x_days=churchchat_start_event_chat_before_x_days,
            churchchat_start_event_chat_for_calendars=churchchat_start_event_chat_for_calendars,
            churchchat_sync_user_id=churchchat_sync_user_id,
            churchcheckin_active=churchcheckin_active,
            churchcheckin_label_child=churchcheckin_label_child,
            churchcheckin_label_parent=churchcheckin_label_parent,
            churchcheckin_label_standard=churchcheckin_label_standard,
            churchcheckin_name=churchcheckin_name,
            churchcheckin_name_default=churchcheckin_name_default,
            churchcheckin_sortcode=churchcheckin_sortcode,
            churchcheckin_tags=churchcheckin_tags,
            churchcustommodule_active=churchcustommodule_active,
            churchcustommodule_name=churchcustommodule_name,
            churchcustommodule_name_default=churchcustommodule_name_default,
            churchdb_active=churchdb_active,
            churchdb_archivedeletehistory=churchdb_archivedeletehistory,
            churchdb_birthdaylist_station=churchdb_birthdaylist_station,
            churchdb_birthdaylist_status=churchdb_birthdaylist_status,
            churchdb_cleverreach_client_id=churchdb_cleverreach_client_id,
            churchdb_cleverreach_client_secret=churchdb_cleverreach_client_secret,
            churchdb_cleverreach_connected=churchdb_cleverreach_connected,
            churchdb_emailseparator=churchdb_emailseparator,
            churchdb_groupnotchoosable=churchdb_groupnotchoosable,
            churchdb_home_lat=churchdb_home_lat,
            churchdb_home_lng=churchdb_home_lng,
            churchdb_mailchimp_apikey=churchdb_mailchimp_apikey,
            churchdb_mailchimp_connected=churchdb_mailchimp_connected,
            churchdb_mailjet_apikey=churchdb_mailjet_apikey,
            churchdb_mailjet_apisecret=churchdb_mailjet_apisecret,
            churchdb_mailjet_connected=churchdb_mailjet_connected,
            churchdb_memberlist_station=churchdb_memberlist_station,
            churchdb_memberlist_status=churchdb_memberlist_status,
            churchdb_name=churchdb_name,
            churchdb_name_default=churchdb_name_default,
            churchdb_sendgroupmails=churchdb_sendgroupmails,
            churchdb_smscmtelecom_apikey=churchdb_smscmtelecom_apikey,
            churchdb_smspromote_apikey=churchdb_smspromote_apikey,
            churchdb_sortcode=churchdb_sortcode,
            churchfinance_active=churchfinance_active,
            churchfinance_name=churchfinance_name,
            churchfinance_name_default=churchfinance_name_default,
            churchfinance_sortcode=churchfinance_sortcode,
            churchgroup_active=churchgroup_active,
            churchgroup_inmenu=churchgroup_inmenu,
            churchgroup_name=churchgroup_name,
            churchgroup_name_default=churchgroup_name_default,
            churchgroup_sortcode=churchgroup_sortcode,
            churchreport_active=churchreport_active,
            churchreport_name=churchreport_name,
            churchreport_name_default=churchreport_name_default,
            churchreport_sortcode=churchreport_sortcode,
            churchresource_active=churchresource_active,
            churchresource_anonymize_for_public_user=churchresource_anonymize_for_public_user,
            churchresource_entries_last_days=churchresource_entries_last_days,
            churchresource_name=churchresource_name,
            churchresource_name_default=churchresource_name_default,
            churchresource_send_emails=churchresource_send_emails,
            churchresource_sortcode=churchresource_sortcode,
            churchservice_active=churchservice_active,
            churchservice_agendashowenumeration=churchservice_agendashowenumeration,
            churchservice_ccli_token=churchservice_ccli_token,
            churchservice_ccli_token_secret=churchservice_ccli_token_secret,
            churchservice_entries_last_days=churchservice_entries_last_days,
            churchservice_invite_persons=churchservice_invite_persons,
            churchservice_name=churchservice_name,
            churchservice_name_default=churchservice_name_default,
            churchservice_openservice_rememberdays=churchservice_openservice_rememberdays,
            churchservice_reminderhours=churchservice_reminderhours,
            churchservice_songwithcategoryasdir=churchservice_songwithcategoryasdir,
            churchservice_sortcode=churchservice_sortcode,
            churchsync_active=churchsync_active,
            churchsync_inmenu=churchsync_inmenu,
            churchsync_name=churchsync_name,
            churchsync_name_default=churchsync_name_default,
            churchsync_sortcode=churchsync_sortcode,
            churchwiki_active=churchwiki_active,
            churchwiki_name=churchwiki_name,
            churchwiki_name_default=churchwiki_name_default,
            churchwiki_sortcode=churchwiki_sortcode,
            cron_daily=cron_daily,
            cron_hour_8=cron_hour_8,
            cronjob_delay=cronjob_delay,
            csrf_enabled=csrf_enabled,
            currently_mail_sending=currently_mail_sending,
            datasecurity_privacy_declaration_wiki_link=datasecurity_privacy_declaration_wiki_link,
            datasecurity_banner_enabled=datasecurity_banner_enabled,
            datasecurity_privacy_agreement_hint=datasecurity_privacy_agreement_hint,
            datasecurity_privacy_agreement_text=datasecurity_privacy_agreement_text,
            datasecurity_privacy_agreement_text_for_children=datasecurity_privacy_agreement_text_for_children,
            db_name=db_name,
            db_password=db_password,
            db_server=db_server,
            db_user=db_user,
            default_phone_area_code=default_phone_area_code,
            email_server=email_server,
            encryptionkey=encryptionkey,
            env=env,
            evangelische_termine_api_key=evangelische_termine_api_key,
            evangelische_termine_enabled=evangelische_termine_enabled,
            evangelische_termine_name=evangelische_termine_name,
            evangelische_termine_url=evangelische_termine_url,
            evangelische_termine_vid=evangelische_termine_vid,
            feature_custommodule=feature_custommodule,
            finance_active=finance_active,
            finance_inmenu=finance_inmenu,
            finance_name=finance_name,
            finance_name_default=finance_name_default,
            finance_sortcode=finance_sortcode,
            first_sync_job=first_sync_job,
            first_transaction=first_transaction,
            hide_beta_states=hide_beta_states,
            hide_all_hints=hide_all_hints,
            hostingservice=hostingservice,
            https_only=https_only,
            image_extension=image_extension,
            impressum_external=impressum_external,
            impressum_external_link=impressum_external_link,
            impressum_internal=impressum_internal,
            imprint_wiki_link=imprint_wiki_link,
            installation_verification_code=installation_verification_code,
            invite_email_text=invite_email_text,
            is_saml_active=is_saml_active,
            is_churchtools_blog_widget_active=is_churchtools_blog_widget_active,
            is_churchtools_onboarding_widget_active=is_churchtools_onboarding_widget_active,
            is_pr_widget_active=is_pr_widget_active,
            is_rss_widget_active=is_rss_widget_active,
            language=language,
            last_cron=last_cron,
            last_cron_finished=last_cron_finished,
            last_import_clear=last_import_clear,
            last_translation_update=last_translation_update,
            ldap_otp_enabled=ldap_otp_enabled,
            license_settings=license_settings,
            log_debug=log_debug,
            login_message=login_message,
            mail_enabled=mail_enabled,
            mail_sending_in_background=mail_sending_in_background,
            mail_sending_starttime=mail_sending_starttime,
            mail_smtp_args_host=mail_smtp_args_host,
            mail_smtp_args_password=mail_smtp_args_password,
            mail_smtp_args_port=mail_smtp_args_port,
            mail_smtp_args_smtpsecure=mail_smtp_args_smtpsecure,
            mail_smtp_args_username=mail_smtp_args_username,
            max_uploadfile_size_kb=max_uploadfile_size_kb,
            memberlist_birthday_full=memberlist_birthday_full,
            memberlist_email=memberlist_email,
            memberlist_fax=memberlist_fax,
            memberlist_group_couples=memberlist_group_couples,
            memberlist_picture=memberlist_picture,
            memberlist_salutation=memberlist_salutation,
            memberlist_telefongeschaeftlich=memberlist_telefongeschaeftlich,
            memberlist_telefonhandy=memberlist_telefonhandy,
            memberlist_telefonprivat=memberlist_telefonprivat,
            onboarding_start=onboarding_start,
            openstreetmaps_enabled=openstreetmaps_enabled,
            orderstatus=orderstatus,
            orderstatus_since_date=orderstatus_since_date,
            package=package,
            post_active=post_active,
            post_edit_time_limited=post_edit_time_limited,
            post_email_summary_default_enabled=post_email_summary_default_enabled,
            post_featured_groups=post_featured_groups,
            post_name=post_name,
            post_sortcode=post_sortcode,
            post_wizard_completed=post_wizard_completed,
            post_wizard_groups=post_wizard_groups,
            prevent_change_security_settings=prevent_change_security_settings,
            prevent_export=prevent_export,
            prevent_manual_finance_account_creation=prevent_manual_finance_account_creation,
            privacy_policy_external=privacy_policy_external,
            privacy_policy_external_link=privacy_policy_external_link,
            privacy_policy_fields_mandatory=privacy_policy_fields_mandatory,
            privacy_policy_fields_mandatory_api=privacy_policy_fields_mandatory_api,
            privacy_policy_internal=privacy_policy_internal,
            privacy_policy_relationships=privacy_policy_relationships,
            profile=profile,
            public_channel_registry_url=public_channel_registry_url,
            rabbitmq_config_host=rabbitmq_config_host,
            rabbitmq_config_password=rabbitmq_config_password,
            rabbitmq_config_port=rabbitmq_config_port,
            rabbitmq_config_user=rabbitmq_config_user,
            rss_widget_link=rss_widget_link,
            safe_mode_enable_authorized_persons=safe_mode_enable_authorized_persons,
            safe_mode_enable_chat_sync=safe_mode_enable_chat_sync,
            safe_mode_enable_consolidation=safe_mode_enable_consolidation,
            safe_mode_enable_guid_sync=safe_mode_enable_guid_sync,
            safe_mode_enable_job_queueing=safe_mode_enable_job_queueing,
            safe_mode_enable_mail=safe_mode_enable_mail,
            safe_mode_enable_newsletter=safe_mode_enable_newsletter,
            safe_mode_enable_notification=safe_mode_enable_notification,
            send_data_security_mails=send_data_security_mails,
            short_name=short_name,
            show_ai_assistant=show_ai_assistant,
            show_remember_me=show_remember_me,
            site_language=site_language,
            site_licensekey=site_licensekey,
            site_logo=site_logo,
            site_mail=site_mail,
            site_name=site_name,
            site_offline=site_offline,
            site_startpage=site_startpage,
            site_url=site_url,
            support_user_active_since=support_user_active_since,
            test=test,
            timezone=timezone,
            version=version,
            website_order_status=website_order_status,
            website_sync_user_id=website_sync_user_id,
            website_testphase_date=website_testphase_date,
            website_trial_user_id=website_trial_user_id,
            website_url=website_url,
            welcome=welcome,
            welcome_subtext=welcome_subtext,
        )

        put_config_response_200.additional_properties = d
        return put_config_response_200

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
