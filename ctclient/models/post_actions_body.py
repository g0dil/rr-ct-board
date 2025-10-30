from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_actions_body_filter import PostActionsBodyFilter


T = TypeVar("T", bound="PostActionsBody")


@_attrs_define
class PostActionsBody:
    """
    Attributes:
        domain_type (list[str]):
        filter_ (PostActionsBodyFilter | Unset):
    """

    domain_type: list[str]
    filter_: PostActionsBodyFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_type = self.domain_type

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_type": domain_type,
            }
        )
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_actions_body_filter import PostActionsBodyFilter

        d = dict(src_dict)
        domain_type = cast(list[str], d.pop("domain_type"))

        _filter_ = d.pop("filter", UNSET)
        filter_: PostActionsBodyFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = PostActionsBodyFilter.from_dict(_filter_)

        post_actions_body = cls(
            domain_type=domain_type,
            filter_=filter_,
        )

        post_actions_body.additional_properties = d
        return post_actions_body

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
