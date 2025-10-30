from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.global_permissions_additional_property import (
        GlobalPermissionsAdditionalProperty,
    )
    from ..models.global_permissions_churchcal import GlobalPermissionsChurchcal
    from ..models.global_permissions_churchcheckin import GlobalPermissionsChurchcheckin
    from ..models.global_permissions_churchcore import GlobalPermissionsChurchcore
    from ..models.global_permissions_churchdb import GlobalPermissionsChurchdb
    from ..models.global_permissions_churchgroup import GlobalPermissionsChurchgroup
    from ..models.global_permissions_churchreport import GlobalPermissionsChurchreport
    from ..models.global_permissions_churchresource import (
        GlobalPermissionsChurchresource,
    )
    from ..models.global_permissions_churchservice import GlobalPermissionsChurchservice
    from ..models.global_permissions_churchsync import GlobalPermissionsChurchsync
    from ..models.global_permissions_churchwiki import GlobalPermissionsChurchwiki
    from ..models.global_permissions_finance import GlobalPermissionsFinance
    from ..models.global_permissions_post import GlobalPermissionsPost


T = TypeVar("T", bound="GlobalPermissions")


@_attrs_define
class GlobalPermissions:
    """Permissions grouped by known modules and user-defined modules.

    Attributes:
        churchcal (GlobalPermissionsChurchcal | Unset):
        churchcheckin (GlobalPermissionsChurchcheckin | Unset):
        churchcore (GlobalPermissionsChurchcore | Unset):
        churchdb (GlobalPermissionsChurchdb | Unset):
        churchgroup (GlobalPermissionsChurchgroup | Unset):
        churchreport (GlobalPermissionsChurchreport | Unset):
        churchresource (GlobalPermissionsChurchresource | Unset):
        churchservice (GlobalPermissionsChurchservice | Unset):
        churchsync (GlobalPermissionsChurchsync | Unset):
        churchwiki (GlobalPermissionsChurchwiki | Unset):
        finance (GlobalPermissionsFinance | Unset):
        post (GlobalPermissionsPost | Unset):
    """

    churchcal: GlobalPermissionsChurchcal | Unset = UNSET
    churchcheckin: GlobalPermissionsChurchcheckin | Unset = UNSET
    churchcore: GlobalPermissionsChurchcore | Unset = UNSET
    churchdb: GlobalPermissionsChurchdb | Unset = UNSET
    churchgroup: GlobalPermissionsChurchgroup | Unset = UNSET
    churchreport: GlobalPermissionsChurchreport | Unset = UNSET
    churchresource: GlobalPermissionsChurchresource | Unset = UNSET
    churchservice: GlobalPermissionsChurchservice | Unset = UNSET
    churchsync: GlobalPermissionsChurchsync | Unset = UNSET
    churchwiki: GlobalPermissionsChurchwiki | Unset = UNSET
    finance: GlobalPermissionsFinance | Unset = UNSET
    post: GlobalPermissionsPost | Unset = UNSET
    additional_properties: dict[str, GlobalPermissionsAdditionalProperty] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:
        churchcal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.churchcal, Unset):
            churchcal = self.churchcal.to_dict()

        churchcheckin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.churchcheckin, Unset):
            churchcheckin = self.churchcheckin.to_dict()

        churchcore: dict[str, Any] | Unset = UNSET
        if not isinstance(self.churchcore, Unset):
            churchcore = self.churchcore.to_dict()

        churchdb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.churchdb, Unset):
            churchdb = self.churchdb.to_dict()

        churchgroup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.churchgroup, Unset):
            churchgroup = self.churchgroup.to_dict()

        churchreport: dict[str, Any] | Unset = UNSET
        if not isinstance(self.churchreport, Unset):
            churchreport = self.churchreport.to_dict()

        churchresource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.churchresource, Unset):
            churchresource = self.churchresource.to_dict()

        churchservice: dict[str, Any] | Unset = UNSET
        if not isinstance(self.churchservice, Unset):
            churchservice = self.churchservice.to_dict()

        churchsync: dict[str, Any] | Unset = UNSET
        if not isinstance(self.churchsync, Unset):
            churchsync = self.churchsync.to_dict()

        churchwiki: dict[str, Any] | Unset = UNSET
        if not isinstance(self.churchwiki, Unset):
            churchwiki = self.churchwiki.to_dict()

        finance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.finance, Unset):
            finance = self.finance.to_dict()

        post: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post, Unset):
            post = self.post.to_dict()

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})
        if churchcal is not UNSET:
            field_dict["churchcal"] = churchcal
        if churchcheckin is not UNSET:
            field_dict["churchcheckin"] = churchcheckin
        if churchcore is not UNSET:
            field_dict["churchcore"] = churchcore
        if churchdb is not UNSET:
            field_dict["churchdb"] = churchdb
        if churchgroup is not UNSET:
            field_dict["churchgroup"] = churchgroup
        if churchreport is not UNSET:
            field_dict["churchreport"] = churchreport
        if churchresource is not UNSET:
            field_dict["churchresource"] = churchresource
        if churchservice is not UNSET:
            field_dict["churchservice"] = churchservice
        if churchsync is not UNSET:
            field_dict["churchsync"] = churchsync
        if churchwiki is not UNSET:
            field_dict["churchwiki"] = churchwiki
        if finance is not UNSET:
            field_dict["finance"] = finance
        if post is not UNSET:
            field_dict["post"] = post

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_permissions_additional_property import (
            GlobalPermissionsAdditionalProperty,
        )
        from ..models.global_permissions_churchcal import GlobalPermissionsChurchcal
        from ..models.global_permissions_churchcheckin import (
            GlobalPermissionsChurchcheckin,
        )
        from ..models.global_permissions_churchcore import GlobalPermissionsChurchcore
        from ..models.global_permissions_churchdb import GlobalPermissionsChurchdb
        from ..models.global_permissions_churchgroup import GlobalPermissionsChurchgroup
        from ..models.global_permissions_churchreport import (
            GlobalPermissionsChurchreport,
        )
        from ..models.global_permissions_churchresource import (
            GlobalPermissionsChurchresource,
        )
        from ..models.global_permissions_churchservice import (
            GlobalPermissionsChurchservice,
        )
        from ..models.global_permissions_churchsync import GlobalPermissionsChurchsync
        from ..models.global_permissions_churchwiki import GlobalPermissionsChurchwiki
        from ..models.global_permissions_finance import GlobalPermissionsFinance
        from ..models.global_permissions_post import GlobalPermissionsPost

        d = dict(src_dict)
        _churchcal = d.pop("churchcal", UNSET)
        churchcal: GlobalPermissionsChurchcal | Unset
        if isinstance(_churchcal, Unset):
            churchcal = UNSET
        else:
            churchcal = GlobalPermissionsChurchcal.from_dict(_churchcal)

        _churchcheckin = d.pop("churchcheckin", UNSET)
        churchcheckin: GlobalPermissionsChurchcheckin | Unset
        if isinstance(_churchcheckin, Unset):
            churchcheckin = UNSET
        else:
            churchcheckin = GlobalPermissionsChurchcheckin.from_dict(_churchcheckin)

        _churchcore = d.pop("churchcore", UNSET)
        churchcore: GlobalPermissionsChurchcore | Unset
        if isinstance(_churchcore, Unset):
            churchcore = UNSET
        else:
            churchcore = GlobalPermissionsChurchcore.from_dict(_churchcore)

        _churchdb = d.pop("churchdb", UNSET)
        churchdb: GlobalPermissionsChurchdb | Unset
        if isinstance(_churchdb, Unset):
            churchdb = UNSET
        else:
            churchdb = GlobalPermissionsChurchdb.from_dict(_churchdb)

        _churchgroup = d.pop("churchgroup", UNSET)
        churchgroup: GlobalPermissionsChurchgroup | Unset
        if isinstance(_churchgroup, Unset):
            churchgroup = UNSET
        else:
            churchgroup = GlobalPermissionsChurchgroup.from_dict(_churchgroup)

        _churchreport = d.pop("churchreport", UNSET)
        churchreport: GlobalPermissionsChurchreport | Unset
        if isinstance(_churchreport, Unset):
            churchreport = UNSET
        else:
            churchreport = GlobalPermissionsChurchreport.from_dict(_churchreport)

        _churchresource = d.pop("churchresource", UNSET)
        churchresource: GlobalPermissionsChurchresource | Unset
        if isinstance(_churchresource, Unset):
            churchresource = UNSET
        else:
            churchresource = GlobalPermissionsChurchresource.from_dict(_churchresource)

        _churchservice = d.pop("churchservice", UNSET)
        churchservice: GlobalPermissionsChurchservice | Unset
        if isinstance(_churchservice, Unset):
            churchservice = UNSET
        else:
            churchservice = GlobalPermissionsChurchservice.from_dict(_churchservice)

        _churchsync = d.pop("churchsync", UNSET)
        churchsync: GlobalPermissionsChurchsync | Unset
        if isinstance(_churchsync, Unset):
            churchsync = UNSET
        else:
            churchsync = GlobalPermissionsChurchsync.from_dict(_churchsync)

        _churchwiki = d.pop("churchwiki", UNSET)
        churchwiki: GlobalPermissionsChurchwiki | Unset
        if isinstance(_churchwiki, Unset):
            churchwiki = UNSET
        else:
            churchwiki = GlobalPermissionsChurchwiki.from_dict(_churchwiki)

        _finance = d.pop("finance", UNSET)
        finance: GlobalPermissionsFinance | Unset
        if isinstance(_finance, Unset):
            finance = UNSET
        else:
            finance = GlobalPermissionsFinance.from_dict(_finance)

        _post = d.pop("post", UNSET)
        post: GlobalPermissionsPost | Unset
        if isinstance(_post, Unset):
            post = UNSET
        else:
            post = GlobalPermissionsPost.from_dict(_post)

        global_permissions = cls(
            churchcal=churchcal,
            churchcheckin=churchcheckin,
            churchcore=churchcore,
            churchdb=churchdb,
            churchgroup=churchgroup,
            churchreport=churchreport,
            churchresource=churchresource,
            churchservice=churchservice,
            churchsync=churchsync,
            churchwiki=churchwiki,
            finance=finance,
            post=post,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GlobalPermissionsAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        global_permissions.additional_properties = additional_properties
        return global_permissions

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GlobalPermissionsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: GlobalPermissionsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
