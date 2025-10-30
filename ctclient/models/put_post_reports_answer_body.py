from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_post_reports_answer_body_domain_type import (
    PutPostReportsAnswerBodyDomainType,
)
from ..models.put_post_reports_answer_body_response import (
    PutPostReportsAnswerBodyResponse,
)

T = TypeVar("T", bound="PutPostReportsAnswerBody")


@_attrs_define
class PutPostReportsAnswerBody:
    """
    Attributes:
        domain_id (int):
        domain_type (PutPostReportsAnswerBodyDomainType):
        response (PutPostReportsAnswerBodyResponse):
    """

    domain_id: int
    domain_type: PutPostReportsAnswerBodyDomainType
    response: PutPostReportsAnswerBodyResponse
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_id = self.domain_id

        domain_type = self.domain_type.value

        response = self.response.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domainId": domain_id,
                "domainType": domain_type,
                "response": response,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_id = d.pop("domainId")

        domain_type = PutPostReportsAnswerBodyDomainType(d.pop("domainType"))

        response = PutPostReportsAnswerBodyResponse(d.pop("response"))

        put_post_reports_answer_body = cls(
            domain_id=domain_id,
            domain_type=domain_type,
            response=response,
        )

        put_post_reports_answer_body.additional_properties = d
        return put_post_reports_answer_body

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
