from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_post_reports_body_domain_type import PostPostReportsBodyDomainType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_post_reports_body_reporter import PostPostReportsBodyReporter


T = TypeVar("T", bound="PostPostReportsBody")


@_attrs_define
class PostPostReportsBody:
    """
    Attributes:
        domain_id (int):
        domain_type (PostPostReportsBodyDomainType):
        captcha (str | Unset):
        comment (str | Unset):
        reporter (PostPostReportsBodyReporter | Unset):
    """

    domain_id: int
    domain_type: PostPostReportsBodyDomainType
    captcha: str | Unset = UNSET
    comment: str | Unset = UNSET
    reporter: PostPostReportsBodyReporter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_id = self.domain_id

        domain_type = self.domain_type.value

        captcha = self.captcha

        comment = self.comment

        reporter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reporter, Unset):
            reporter = self.reporter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainId": domain_id,
                "domainType": domain_type,
            }
        )
        if captcha is not UNSET:
            field_dict["captcha"] = captcha
        if comment is not UNSET:
            field_dict["comment"] = comment
        if reporter is not UNSET:
            field_dict["reporter"] = reporter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_post_reports_body_reporter import PostPostReportsBodyReporter

        d = dict(src_dict)
        domain_id = d.pop("domainId")

        domain_type = PostPostReportsBodyDomainType(d.pop("domainType"))

        captcha = d.pop("captcha", UNSET)

        comment = d.pop("comment", UNSET)

        _reporter = d.pop("reporter", UNSET)
        reporter: PostPostReportsBodyReporter | Unset
        if isinstance(_reporter, Unset):
            reporter = UNSET
        else:
            reporter = PostPostReportsBodyReporter.from_dict(_reporter)

        post_post_reports_body = cls(
            domain_id=domain_id,
            domain_type=domain_type,
            captcha=captcha,
            comment=comment,
            reporter=reporter,
        )

        post_post_reports_body.additional_properties = d
        return post_post_reports_body

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
