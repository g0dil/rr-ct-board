from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_global_permissions_response_200_data_additional_property import (
        GetGlobalPermissionsResponse200DataAdditionalProperty,
    )
    from ..models.get_global_permissions_response_200_data_churchcal import (
        GetGlobalPermissionsResponse200DataChurchcal,
    )
    from ..models.get_global_permissions_response_200_data_churchcheckin import (
        GetGlobalPermissionsResponse200DataChurchcheckin,
    )
    from ..models.get_global_permissions_response_200_data_churchcore import (
        GetGlobalPermissionsResponse200DataChurchcore,
    )
    from ..models.get_global_permissions_response_200_data_churchdb import (
        GetGlobalPermissionsResponse200DataChurchdb,
    )
    from ..models.get_global_permissions_response_200_data_churchgroup import (
        GetGlobalPermissionsResponse200DataChurchgroup,
    )
    from ..models.get_global_permissions_response_200_data_churchreport import (
        GetGlobalPermissionsResponse200DataChurchreport,
    )
    from ..models.get_global_permissions_response_200_data_churchresource import (
        GetGlobalPermissionsResponse200DataChurchresource,
    )
    from ..models.get_global_permissions_response_200_data_churchservice import (
        GetGlobalPermissionsResponse200DataChurchservice,
    )
    from ..models.get_global_permissions_response_200_data_churchsync import (
        GetGlobalPermissionsResponse200DataChurchsync,
    )
    from ..models.get_global_permissions_response_200_data_churchwiki import (
        GetGlobalPermissionsResponse200DataChurchwiki,
    )
    from ..models.get_global_permissions_response_200_data_finance import (
        GetGlobalPermissionsResponse200DataFinance,
    )
    from ..models.get_global_permissions_response_200_data_post import (
        GetGlobalPermissionsResponse200DataPost,
    )


T = TypeVar("T", bound="GetGlobalPermissionsResponse200Data")


@_attrs_define
class GetGlobalPermissionsResponse200Data:
    """Permissions grouped by known modules and user-defined modules.

    Attributes:
        churchcal (GetGlobalPermissionsResponse200DataChurchcal | Unset):
        churchcheckin (GetGlobalPermissionsResponse200DataChurchcheckin | Unset):
        churchcore (GetGlobalPermissionsResponse200DataChurchcore | Unset):
        churchdb (GetGlobalPermissionsResponse200DataChurchdb | Unset):
        churchgroup (GetGlobalPermissionsResponse200DataChurchgroup | Unset):
        churchreport (GetGlobalPermissionsResponse200DataChurchreport | Unset):
        churchresource (GetGlobalPermissionsResponse200DataChurchresource | Unset):
        churchservice (GetGlobalPermissionsResponse200DataChurchservice | Unset):
        churchsync (GetGlobalPermissionsResponse200DataChurchsync | Unset):
        churchwiki (GetGlobalPermissionsResponse200DataChurchwiki | Unset):
        finance (GetGlobalPermissionsResponse200DataFinance | Unset):
        post (GetGlobalPermissionsResponse200DataPost | Unset):
    """

    churchcal: GetGlobalPermissionsResponse200DataChurchcal | Unset = UNSET
    churchcheckin: GetGlobalPermissionsResponse200DataChurchcheckin | Unset = UNSET
    churchcore: GetGlobalPermissionsResponse200DataChurchcore | Unset = UNSET
    churchdb: GetGlobalPermissionsResponse200DataChurchdb | Unset = UNSET
    churchgroup: GetGlobalPermissionsResponse200DataChurchgroup | Unset = UNSET
    churchreport: GetGlobalPermissionsResponse200DataChurchreport | Unset = UNSET
    churchresource: GetGlobalPermissionsResponse200DataChurchresource | Unset = UNSET
    churchservice: GetGlobalPermissionsResponse200DataChurchservice | Unset = UNSET
    churchsync: GetGlobalPermissionsResponse200DataChurchsync | Unset = UNSET
    churchwiki: GetGlobalPermissionsResponse200DataChurchwiki | Unset = UNSET
    finance: GetGlobalPermissionsResponse200DataFinance | Unset = UNSET
    post: GetGlobalPermissionsResponse200DataPost | Unset = UNSET
    additional_properties: dict[
        str, GetGlobalPermissionsResponse200DataAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

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
        from ..models.get_global_permissions_response_200_data_additional_property import (
            GetGlobalPermissionsResponse200DataAdditionalProperty,
        )
        from ..models.get_global_permissions_response_200_data_churchcal import (
            GetGlobalPermissionsResponse200DataChurchcal,
        )
        from ..models.get_global_permissions_response_200_data_churchcheckin import (
            GetGlobalPermissionsResponse200DataChurchcheckin,
        )
        from ..models.get_global_permissions_response_200_data_churchcore import (
            GetGlobalPermissionsResponse200DataChurchcore,
        )
        from ..models.get_global_permissions_response_200_data_churchdb import (
            GetGlobalPermissionsResponse200DataChurchdb,
        )
        from ..models.get_global_permissions_response_200_data_churchgroup import (
            GetGlobalPermissionsResponse200DataChurchgroup,
        )
        from ..models.get_global_permissions_response_200_data_churchreport import (
            GetGlobalPermissionsResponse200DataChurchreport,
        )
        from ..models.get_global_permissions_response_200_data_churchresource import (
            GetGlobalPermissionsResponse200DataChurchresource,
        )
        from ..models.get_global_permissions_response_200_data_churchservice import (
            GetGlobalPermissionsResponse200DataChurchservice,
        )
        from ..models.get_global_permissions_response_200_data_churchsync import (
            GetGlobalPermissionsResponse200DataChurchsync,
        )
        from ..models.get_global_permissions_response_200_data_churchwiki import (
            GetGlobalPermissionsResponse200DataChurchwiki,
        )
        from ..models.get_global_permissions_response_200_data_finance import (
            GetGlobalPermissionsResponse200DataFinance,
        )
        from ..models.get_global_permissions_response_200_data_post import (
            GetGlobalPermissionsResponse200DataPost,
        )

        d = dict(src_dict)
        _churchcal = d.pop("churchcal", UNSET)
        churchcal: GetGlobalPermissionsResponse200DataChurchcal | Unset
        if isinstance(_churchcal, Unset):
            churchcal = UNSET
        else:
            churchcal = GetGlobalPermissionsResponse200DataChurchcal.from_dict(
                _churchcal
            )

        _churchcheckin = d.pop("churchcheckin", UNSET)
        churchcheckin: GetGlobalPermissionsResponse200DataChurchcheckin | Unset
        if isinstance(_churchcheckin, Unset):
            churchcheckin = UNSET
        else:
            churchcheckin = GetGlobalPermissionsResponse200DataChurchcheckin.from_dict(
                _churchcheckin
            )

        _churchcore = d.pop("churchcore", UNSET)
        churchcore: GetGlobalPermissionsResponse200DataChurchcore | Unset
        if isinstance(_churchcore, Unset):
            churchcore = UNSET
        else:
            churchcore = GetGlobalPermissionsResponse200DataChurchcore.from_dict(
                _churchcore
            )

        _churchdb = d.pop("churchdb", UNSET)
        churchdb: GetGlobalPermissionsResponse200DataChurchdb | Unset
        if isinstance(_churchdb, Unset):
            churchdb = UNSET
        else:
            churchdb = GetGlobalPermissionsResponse200DataChurchdb.from_dict(_churchdb)

        _churchgroup = d.pop("churchgroup", UNSET)
        churchgroup: GetGlobalPermissionsResponse200DataChurchgroup | Unset
        if isinstance(_churchgroup, Unset):
            churchgroup = UNSET
        else:
            churchgroup = GetGlobalPermissionsResponse200DataChurchgroup.from_dict(
                _churchgroup
            )

        _churchreport = d.pop("churchreport", UNSET)
        churchreport: GetGlobalPermissionsResponse200DataChurchreport | Unset
        if isinstance(_churchreport, Unset):
            churchreport = UNSET
        else:
            churchreport = GetGlobalPermissionsResponse200DataChurchreport.from_dict(
                _churchreport
            )

        _churchresource = d.pop("churchresource", UNSET)
        churchresource: GetGlobalPermissionsResponse200DataChurchresource | Unset
        if isinstance(_churchresource, Unset):
            churchresource = UNSET
        else:
            churchresource = (
                GetGlobalPermissionsResponse200DataChurchresource.from_dict(
                    _churchresource
                )
            )

        _churchservice = d.pop("churchservice", UNSET)
        churchservice: GetGlobalPermissionsResponse200DataChurchservice | Unset
        if isinstance(_churchservice, Unset):
            churchservice = UNSET
        else:
            churchservice = GetGlobalPermissionsResponse200DataChurchservice.from_dict(
                _churchservice
            )

        _churchsync = d.pop("churchsync", UNSET)
        churchsync: GetGlobalPermissionsResponse200DataChurchsync | Unset
        if isinstance(_churchsync, Unset):
            churchsync = UNSET
        else:
            churchsync = GetGlobalPermissionsResponse200DataChurchsync.from_dict(
                _churchsync
            )

        _churchwiki = d.pop("churchwiki", UNSET)
        churchwiki: GetGlobalPermissionsResponse200DataChurchwiki | Unset
        if isinstance(_churchwiki, Unset):
            churchwiki = UNSET
        else:
            churchwiki = GetGlobalPermissionsResponse200DataChurchwiki.from_dict(
                _churchwiki
            )

        _finance = d.pop("finance", UNSET)
        finance: GetGlobalPermissionsResponse200DataFinance | Unset
        if isinstance(_finance, Unset):
            finance = UNSET
        else:
            finance = GetGlobalPermissionsResponse200DataFinance.from_dict(_finance)

        _post = d.pop("post", UNSET)
        post: GetGlobalPermissionsResponse200DataPost | Unset
        if isinstance(_post, Unset):
            post = UNSET
        else:
            post = GetGlobalPermissionsResponse200DataPost.from_dict(_post)

        get_global_permissions_response_200_data = cls(
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
            additional_property = (
                GetGlobalPermissionsResponse200DataAdditionalProperty.from_dict(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        get_global_permissions_response_200_data.additional_properties = (
            additional_properties
        )
        return get_global_permissions_response_200_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> GetGlobalPermissionsResponse200DataAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: GetGlobalPermissionsResponse200DataAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
